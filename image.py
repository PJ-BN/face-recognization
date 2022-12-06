

import cv2 as cv
import os


class clickImage:

    def click(self, parent_dir, dir_names):

        # create a directory to store the images
        path = self.make_dir(parent_dir, dir_names)
        # initialize the camera
        # If you have multiple camera connected with
        # current device, assign a value in cam_port
        # variable according to that
        for i in range(10):

            cam_port = 0
            cam = cv.VideoCapture(cam_port)

            # reading the input using the camera
            result, image = cam.read()

            # If image will detected without any error,
            # show result
            if result:

                # showing result, it take frame name and image
                # output
                # cv.imshow("Image", image)
                img_path = os.path.join(path, f"{i}.png")

                # saving image in local storage
                cv.imwrite(img_path, image)

                # If keyboard interrupt occurs, destroy image
                # window
                # cv.waitKey(0)
                # cv.destroyWindow(img_path)

            # If captured image is corrupted, moving to else part
            else:
                print("No image detected. Please! try again")

            cam.release()

            if i == 10:
                cv.destroyAllWindows()

    def make_dir(self, parent_dir, dir_name):
        path = os.path.join(parent_dir, dir_name)
        os.mkdir(path)
        return path



# parent_path = "/home/zoro/PycharmProjects/attandencesys/images"
# dir_name = "new"
# images = clickImage()
# images.click(parent_dir=parent_path, dir_names=dir_name)
