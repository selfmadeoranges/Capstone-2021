import cv2
import numpy as np 
 
i = 0
username = 'sangjun'
while True:
   img = cv2.imread('./capture_img/{}{}.jpg'.format(username,i))
   rows,cols = img.shape[0:2]  # 영상의 크기 
 
   m0 = cv2.getRotationMatrix2D((cols/2,rows/2),0,1) 
   m1 = cv2.getRotationMatrix2D((cols/2,rows/2),25,1.5)
   m2 = cv2.getRotationMatrix2D((cols/2,rows/2),360-25,1.5)
   m3 = cv2.getRotationMatrix2D((cols/2,rows/2),0,0.5)    
 
   #---② 변환 행렬 적용
   img0 = cv2.warpAffine(img, m0,(cols, rows))
   img1 = cv2.warpAffine(img, m1,(cols, rows))
   img2 = cv2.warpAffine(img, m2,(cols, rows)) 
   img3 = cv2.warpAffine(img, m3,(cols, rows)) 
 
   outfilename = './translate_img/{}{}-1.jpg'.format(username,i)
   cv2.imwrite(outfilename, img0)
   outfilename = './translate_img/{}{}-2.jpg'.format(username,i)
   cv2.imwrite(outfilename, img1)
   outfilename = './translate_img/{}{}-3.jpg'.format(username,i)
   cv2.imwrite(outfilename, img2)
   outfilename = './translate_img/{}{}-4.jpg'.format(username,i)
   cv2.imwrite(outfilename, img3)
   i=i+1

   if i == 3000 :
       break