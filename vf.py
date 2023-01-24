import cv2
import os

path = 'C:/Users/livcr/OneDrive/Pictures/projects/105/imagefile'

image = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.png', '.jpg']:
       file_name = path + '/' + file
       image.append(file_name)
count = len(image)
frame = cv2.imread(image[0])
size = (663, 402)

out = cv2.VideoWriter('o0o.avi', cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)

for i in range(count, -1):
    a = cv2.imread(image[i])
    out.write(a)

out.release() 
print("Done")

print(len(image))
print(frame.shape)
print(size)
