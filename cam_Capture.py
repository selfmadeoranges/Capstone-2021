import cv2

scaler = 0.2
# video_file = "../img/big_buck.avi" # 동영상 파일 경로
i = 6
cap = cv2.VideoCapture('222.mp4') # webcam 캡쳐 객체 생성  ---①

if cap.isOpened():                 # 캡쳐 객체 초기화 확인
    while True:
        ret, img = cap.read()      # 다음 프레임 읽기      --- ②
        # img = cv2.resize(img, (int(img.shape[1] * scaler), int(img.shape[0] * scaler))) #사이즈 축소
        img = cv2.flip(img, 1) #w좌우 반전
        if ret:                     # 프레임 읽기 정상
            cv2.imshow('camara', img) # 화면에 표시  --- ③
            if cv2.waitKey(1) != -1:            # 아무 키나 누르면
                outfilename = './data_img/1/sangjun0000{}.jpg'.format(i)
                cv2.imwrite(outfilename, img) # 프레임을 'photo.jpg'에 저장
                i+=1
        else:                       # 다음 프레임 읽을 수 없슴,
            break                   # 재생 완료
else:
    print("can't open video.")      # 캡쳐 객체 초기화 실패
cap.release()                       # 캡쳐 자원 반납
cv2.destroyAllWindows()