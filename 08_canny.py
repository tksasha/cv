import cv2 as cv

if __name__ == "__main__":
    image = cv.imread("0-kpi.jpg", cv.IMREAD_GRAYSCALE)
    assert image is not None, "failed to read image"

    canny = cv.Canny(image, 100, 200)

    cv.imshow("Canny", canny)

    _ = cv.waitKey(0)

    cv.destroyAllWindows()
