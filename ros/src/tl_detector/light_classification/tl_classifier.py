from styx_msgs.msg import TrafficLight
import cv2
import numpy as np

class TLClassifier(object):
    def __init__(self):
        #TODO load classifier
        pass

    def get_classification(self, image):
        """Determines the color of the traffic light in the image

        Args:
            image (cv::Mat): image containing the traffic light

        Returns:
            int: ID of traffic light color (specified in styx_msgs/TrafficLight)

        """
        #TODO implement light color prediction
        
        color = TrafficLight.UNKNOWN
        
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        
        #Detecting red light for two hue ranges and interpolating 
        
        case_1 = cv2.inRange(hsv, np.array([0,50,50]) , np.array([10,255,255]))
        
        case_2 = cv2.inRange(hsv, np.array([170,50,50]) , np.array([180,255,255]))
        
        weighted_result = cv2.addWeighted(case_1, 1.0, case_2, 1.0, 0.0)
        
        blurred = cv2.GaussianBlur(weighted_result, (15,15), 0)
        
        circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 0.5, 41, param1=70, param2=30, minRadius=5, maxRadius=150)
        
        if circles is not None:
            color = TrafficLight.RED
            #for circle in circles[0, :]:
                #cv2.circle(image, (circle[0], circle[1]), circle[2], (255, 0, 0), 2)
            return color
                
        #Detecting yellow light for yellow hue range 
        
        case_1 = cv2.inRange(hsv, np.array([20,100,100]) , np.array([30,255,255]))
        
        blurred = cv2.GaussianBlur(case_1, (15,15), 0)
        
        circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 0.5, 41, param1=70, param2=30, minRadius=5, maxRadius=150)
        
        if circles is not None:
            color = TrafficLight.YELLOW
            #for circle in circles[0, :]:
                #cv2.circle(image, (circle[0], circle[1]), circle[2], (255, 0, 0), 2)
            return color
        
        return color
