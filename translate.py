import cv2
import numpy as np

img = cv2.imread('./data_img/SangJun00000.jpg')
rows,cols = img.shape[0:2]  # 영상의 크기

m0 = cv2.getRotationMatrix2D((cols/2,rows/2),0,1.5)

m25 = cv2.getRotationMatrix2D((cols/2,rows/2),25,1.5) 
# 회전축:중앙, 각도:90, 배율:1.5
m45 = cv2.getRotationMatrix2D((cols/2,rows/2),45,1.5) 

#---② 변환 행렬 적용
img0 = cv2.warpAffine(img, m0,(cols, rows))
img25 = cv2.warpAffine(img, m25,(cols, rows))
img45 = cv2.warpAffine(img, m45,(cols, rows))

cv2.imshow('origin',img)
cv2.imshow('zoom',img0)
cv2.imshow("25", img25)
cv2.imshow("45", img45)
cv2.waitKey(0)
cv2.destroyAllWindows()

# outfilename = 'C:/Temp/test/data_img/SangJun00000-{}.jpg'.format(i)
outfilename = 'C:/Temp/test/SangJun00000-1.jpg'
cv2.imwrite(outfilename, img0)
outfilename = 'C:/Temp/test/SangJun00000-2.jpg'
cv2.imwrite(outfilename, img25)
outfilename = 'C:/Temp/test/SangJun00000-3.jpg'
cv2.imwrite(outfilename, img45)