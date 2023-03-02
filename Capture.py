# Import opencv to access Webcam for taking pictures.
import cv2 

# Import uuid to give each image a unique id as name
import uuid

# Import Operating System to use os utilities for more accessibility over system
import os

# Import time to use sleep() method for taking break in between taking pictures of objects.
import time

labels = ['thumbsup', 'thumbsdown', 'thankyou', 'livelong']

number_imgs = 5

directory = r"C:\\Users\\ayush\\Downloads\\TensorFlow Object Detection\\Tensorflow\\workspace\\images\\collectedimages"

if not os.path.exists(directory):
    if os.name == 'posix':
        os.makedirs(directory,0o777)
    if os.name == 'nt':
         os.makedirs(directory,0o777)


for label in labels:
    path = os.path.join(directory, label)
    if not os.path.exists(path):
        os.makedirs(path)
        

# Capturing Images using OpenCV

# for label in labels:
#     cap = cv2.VideoCapture(0)
#     print('Collecting images for {}'.format(label))
#     time.sleep(5)
#     for imgnum in range(number_imgs):
#         print('Collecting image {}'.format(imgnum))
#         ret, frame = cap.read()
#         imgname = os.path.join(directory,label,label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
#         cv2.imwrite(imgname, frame)
#         cv2.imshow('frame', frame)
#         time.sleep(2)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
# cap.release()
# cv2.destroyAllWindows()