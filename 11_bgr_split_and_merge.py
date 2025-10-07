import cv2 as cv

if __name__ == "__main__":
    image = cv.imread("0-parrot.webp")
    assert image is not None, "failed to read image"

    b, g, r = cv.split(image)

    cv.imshow("Original", image)
    _ = cv.waitKey(0)

    cv.imshow("Blue", b)
    _ = cv.waitKey(0)

    cv.imshow("Green", g)
    _ = cv.waitKey(0)

    cv.imshow("Red", r)
    _ = cv.waitKey(0)

    merged = cv.merge([b, g, r])

    cv.imshow("Merged", merged)
    _ = cv.waitKey(0)

    cv.destroyAllWindows()
