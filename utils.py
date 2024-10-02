import cv2

def show_frame(window_name, frame):
    cv2.imshow(window_name, frame)

def wait_for_exit(key='q'):
    return cv2.waitKey(1) & 0xFF == ord(key)
