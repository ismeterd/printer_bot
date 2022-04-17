# importing OpenCV library
import cv2


class CaptureImage():

    def __init__(self, cam_port):
        self.cam_port = cam_port
        self.cam = cv2.VideoCapture(self.cam_port)
        self.result, self.image = self.cam.read()

    def capture(self):
        self.result, self.image = self.cam.read()

    def show(self):
        cv2.imshow("CapturedImage", self.image)
        cv2.waitKey()
        cv2.destroyWindow("CapturedImage")

    def save(self):
        cv2.imwrite("images/captured_image.png", self.image)


if __name__ == "__main__":

    image = CaptureImage(1)  # cam_port is selected 1 for my webcam

    while (True):
        valid = input("Do you want to capture and save image(yes): ")

        if valid == "yes":
            image.capture()
            image.save()

        else:
            print("quitting the program...")
            break
