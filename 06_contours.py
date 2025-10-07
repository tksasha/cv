import cv2 as cv

#
# TODO: how does it work?
#
if __name__ == "__main__":
    image = cv.imread("0-kpi.jpg")
    assert image is not None, "failed to read image"

    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    _, threshold = cv.threshold(gray, 127, 255, 0)

    contours, hierarchy = cv.findContours(threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    _ = cv.drawContours(image, contours, -1, (0, 255, 0), 3)
