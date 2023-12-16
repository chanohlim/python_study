import cv2

import os

import imutils

import numpy as np

import pytesseract

from PIL import Image

import smtplib
from email.mime.text import MIMEText

smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.starttls()
smtp.login('panopticam3@gmail.com','jpghjgpugitsaibl')


os.system("libcamera-still -o /home/chan/Desktop/4.jpg ")

img = cv2.imread('/home/chan/Desktop/5.jpg',cv2.IMREAD_COLOR)

img = cv2.resize(img, (620,480) )



gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #그레이스캐일로 변환

gray = cv2.bilateralFilter(gray, 11, 17, 17) #노이즈 감소

edged = cv2.Canny(gray, 30, 200) #경계 찾기


#대비를 찾고, 가장 대비가 큰 것만 keep

cnts = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnts = imutils.grab_contours(cnts)

cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]

screenCnt = None


#대비 요소들에서 시퀸스 반복

for c in cnts:

 peri = cv2.arcLength(c, True)

 approx = cv2.approxPolyDP(c, 0.018 * peri, True)

 

 # if our approximated contour has four points, then

 # we can assume that we have found our screen

 if len(approx) == 4:

  screenCnt = approx

  break


 


if screenCnt is None:

 detected = 0

 print ("No contour detected")

else:

 detected = 1


if detected == 1:

 cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 3)


# Masking the part other than the number plate

mask = np.zeros(gray.shape,np.uint8)

new_image = cv2.drawContours(mask,[screenCnt],0,255,-1,)

new_image = cv2.bitwise_and(img,img,mask=mask)


# Now crop

(x, y) = np.where(mask == 255)

(topx, topy) = (np.min(x), np.min(y))

(bottomx, bottomy) = (np.max(x), np.max(y))

Cropped = gray[topx:bottomx+1, topy:bottomy+1]


 


#번호판 사진에서 텍스트 추출
text = pytesseract.image_to_string(Cropped, lang='kor', config='--psm 7 --oem 0')


t_list = []

cnt = 0
char_i = 0

for i in range(len(text)):
    if text[i].isnumeric() is False:
        if i == 0:
            continue
        else:
            cnt += 1
            char_i = i
    if i > char_i+4:
        continue
            
    t_list += text[i]
    

print("Detected Number is:",''.join(t_list))

msg = MIMEText(''.join(t_list))
msg['Subject'] = 'panopticam_과속자동신고'

smtp.sendmail('panopticam3@gmail.com','heechanny@gmail.com',msg.as_string())

print('메일 전송 완료')

smtp.quit()




cv2.imshow('image',img)

cv2.imshow('Cropped',Cropped)


cv2.waitKey(0)

cv2.destroyAllWindows()