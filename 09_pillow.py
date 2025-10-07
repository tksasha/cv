from PIL import Image, ImageEnhance
from matplotlib import pyplot

if __name__ == "__main__":
    image = Image.open("0-fuel-depot.jpg")
    assert image is not None, "failed to open image"

    enhancer = ImageEnhance.Sharpness(image)

    pyplot.subplot(1, 3, 1), pyplot.title(0), pyplot.imshow(enhancer.enhance(0))
    pyplot.subplot(1, 3, 2), pyplot.title(0.05), pyplot.imshow(enhancer.enhance(0.05))
    pyplot.subplot(1, 3, 3), pyplot.title(2), pyplot.imshow(enhancer.enhance(2))

    pyplot.show()
