import cv2 as cv
import numpy

if __name__ == "__main__":
    cap = cv.VideoCapture(0)

    while(True):
        ok, frame = cap.read()

        if not ok:
            print("failed to read frame")
            break

        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        # define range of blue color in HSV
        lower_blue = numpy.array([110, 50, 50])
        upper_blue = numpy.array([130, 255, 255])

        # threshold the HSV image to get only blue colors
        mask = cv.inRange(hsv, lower_blue, upper_blue)

        # bitwise-and mask and original image
        bitwise = cv.bitwise_and(frame, frame, mask = mask)

        cv.imshow("frame", frame)
        cv.imshow("mask", mask)
        cv.imshow("bitwise", bitwise)

        k = cv.waitKey(5) & 0xFF
        if k == 27:
            break
            
    cv.destroyAllWindows()
