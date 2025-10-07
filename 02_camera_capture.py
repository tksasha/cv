import cv2 as cv

if __name__ == "__main__":
    cap = cv.VideoCapture(0)

    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    while True:
        ok, frame = cap.read()

        if not ok:
            print("failed to read a frame")
            break

        # frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        cv.imshow("frame", frame)

        if cv.waitKey(1) == ord("q"):
            break

    cap.release()
    cv.destroyAllWindows()
