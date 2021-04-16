import glob
img_path=glob.glob("VOC2007/JPEGImages/*.png")
import cv2
for path in img_path:
	img=cv2.imread(path)
	img=cv2.resize(img,(256,256))
	cv2.imwrite(path,img)
