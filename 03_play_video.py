import cv2 as cv

if __name__ == "__main__":
    cap = cv.VideoCapture("0-people-on-the-steet.mp4")

    while cap.isOpened():
        ok, frame = cap.read()

        if not ok:
            print("failed to read a frame")
            break

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        cv.imshow("frame", gray)

        if cv.waitKey(1) == ord("q"):
            break

    cap.release()
    cv.destroyAllWindows()
