from cv2.typing import MatLike
import cv2 as cv
from numpy import array
from typing import Callable

def greyscale(image: MatLike):
    return cv.cvtColor(image, cv.COLOR_BGR2GRAY)

def sepia(image: MatLike):
    sepia_kernel = array(
        [[0.272, 0.534, 0.131], [0.349, 0.686, 0.168], [0.393, 0.769, 0.189]]
    )

    return cv.transform(image, sepia_kernel)

def show(title: str, filter: Callable[[MatLike], MatLike], image: MatLike):
    cv.imshow(title, filter(image))

    _ = cv.waitKey(0)
    cv.destroyAllWindows()

def donothing(image: MatLike):
    return image

def pencilSketch(image: MatLike):
    return cv.pencilSketch(image, sigma_s = 40, sigma_r = 0.06, shade_factor = 0.05)

def detailEnhance(image: MatLike):
    return cv.detailEnhance(image, sigma_s = 10, sigma_r = 0.15)

if __name__ == "__main__":
    image = cv.imread("0-kpi.jpg")
    assert image is not None, "failed to open image"

    show("Greyscale", greyscale, image)
    show("Sepia", sepia, image)

    pencil, sketch = pencilSketch(image)

    show("Pencil", donothing, pencil)
    show("Sketch", donothing, sketch)

    show("Detail Enhance", detailEnhance, image)
