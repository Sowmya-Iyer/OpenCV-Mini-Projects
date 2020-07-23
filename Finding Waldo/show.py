import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
def show(name,image):
    plt.figure()
    print(name)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.show()
