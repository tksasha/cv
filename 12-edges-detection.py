import cv2 as cv
import matplotlib.pyplot as plot

if __name__ == "__main__":
    image = cv.imread("0-ganeshji.webp", cv.COLOR_BGR2RGB)
    assert image is not None, "failed to read image"

    fig, axs = plot.subplots(1, 2, figsize=(7, 4))

    axs[0].imshow(image), axs[0].set_title("Original")

    edges = cv.Canny(image, 100, 700)

    axs[1].imshow(edges), axs[1].set_title("Edges")

    for ax in axs:
        ax.set_xticks([]), ax.set_yticks([])

    # plot.tight_layout()
    plot.show()
