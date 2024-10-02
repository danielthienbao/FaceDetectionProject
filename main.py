import cv2
from camera import Camera
from face_detection import FaceDetector
from utils import show_frame, wait_for_exit

def main():
    camera = Camera()
    face_detector = FaceDetector()

    try:
        while True:
            frame = camera.get_frame()
            faces = face_detector.detect_faces(frame)
            face_detector.draw_faces(frame, faces)

            show_frame('Live Feed', frame)

            if wait_for_exit():
                break
    finally:
        camera.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
