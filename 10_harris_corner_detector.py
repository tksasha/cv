import cv2 as cv
import numpy

if __name__ == "__main__":
    image = cv.imread("0-kpi.jpg")
    assert image is not None, "failed to open image"

    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    gray = numpy.float32(gray)

    dst = cv.cornerHarris(gray, 2, 3, 0.04)

    dst = cv.dilate(dst, None)

    image[dst > 0.01 * dst.max()] = [0, 0, 255]

    cv.imshow("Corners", image)

    _ = cv.waitKey(0)

    cv.destroyAllWindows()
