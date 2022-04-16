# importing OpenCV library
import cv2

# initialize the camera
# it can be multiple camera connected with pc
# you can change the cam_port to select another camera

cam_port = 1  # my webcam port
cam = cv2.VideoCapture(cam_port)

def run():
    valid = input("Enter the 'ok' to capture a image: ")

    if (valid == "ok"):
        result, image = cam.read()
        print("Capturing the image...")
    else:
        print("quitting the program...")
        return False

    valid = input("Enter the 'show' to show capturing image: ")

    if (valid == "show" and result == True):
        print(result)
        print(image)
        cv2.imshow("CapturedImage", image)
        cv2.waitKey()
    else:
        print("quitting the program...")
        return False

    valid = input("Enter the 'save' to save capturing image: ")

    if (valid == "save"):
        cv2.imwrite("images/captured_image.png", image)

    else:
        print("quitting the program...")
        return False

    valid = input("Do you wanna capture a image again?(yes): ")

    if (valid == "yes"):
        print("Starting again...")

    else:
        cv2.destroyWindow("CapturedImage")
        print("quitting the program...")
        return False

if __name__ == "__main__":
    while(True):
        program = run()
        if program == False:
            break

