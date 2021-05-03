import cv2
import numpy as np 
 
i = 0
while True:
   img = cv2.imread('./data_img/yoonji/{}.jpg'.format(i))
   rows,cols = img.shape[0:2]  # 영상의 크기 
 
   m0 = cv2.getRotationMatrix2D((cols/2,rows/2),0,2) 
   m1 = cv2.getRotationMatrix2D((cols/2,rows/2),25,1.5)
   m2 = cv2.getRotationMatrix2D((cols/2,rows/2),360-25,1.5)
   m3 = cv2.getRotationMatrix2D((cols/2,rows/2),0,0.5)    
 
   #---② 변환 행렬 적용
   img0 = cv2.warpAffine(img, m0,(cols, rows))
   img1 = cv2.warpAffine(img, m1,(cols, rows))
   img2 = cv2.warpAffine(img, m2,(cols, rows)) 
   img3 = cv2.warpAffine(img, m3,(cols, rows)) 
 
   #cv2.imshow('origin',img)
   #cv2.imshow('zoom',img0)
   #cv2.imshow("25", img25)
   #cv2.imshow("45", img45)
   #cv2.waitKey(0)
   #cv2.destroyAllWindows() 
 
   # outfilename = 'C:/Temp/test/data_img/SangJun00000-{}.jpg'.format(i)
   outfilename = './processed__img/yoonji/{}-1.jpg'.format(i)
   cv2.imwrite(outfilename, img0)
   outfilename = './processed__img/yoonji/{}-2.jpg'.format(i)
   cv2.imwrite(outfilename, img1)
   outfilename = './processed__img/yoonji/{}-3.jpg'.format(i)
   cv2.imwrite(outfilename, img2)
   outfilename = './processed__img/yoonji/{}-4.jpg'.format(i)
   cv2.imwrite(outfilename, img3)
   i=i+1

   if i == 300 :
       break