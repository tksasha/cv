import cv2 as cv

#
# TODO: this code doesn't work, need to fix
#
if __name__ == "__main__":
    cap = cv.VideoCapture(0)

    # codec = cv.VideoWriter_fourcc(*"XDIV")

    writer = cv.VideoWriter(".captured-video.mp4", -1, 20.0, (640, 480))

    while cap.isOpened():
        ok, frame = cap.read()

        if not ok:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        # frame = cv.flip(frame, 0)

        writer.write(frame)

        print(frame.nbytes)

        cv.imshow("frame", frame)
        if cv.waitKey(1) == ord("q"):
            break

    cap.release()
    writer.release()
    cv.destroyAllWindows()
