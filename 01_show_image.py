import cv2 as cv

if __name__ == "__main__":
    image = cv.imread("0-kpi.jpg")
    assert image is not None, "failed to read image"

    cv.imshow("Show Image", image)

    _ = cv.waitKey(0)

    cv.destroyAllWindows()
