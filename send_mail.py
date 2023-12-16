import smtplib
from email.mime.text import MIMEText

smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.starttls()
smtp.login('panopticam3@gmail.com','jpghjgpugitsaibl')


msg = MIMEText('133가 7388')
msg['Subject'] = '과속자동신고'

smtp.sendmail('panopticam3@gmail.com','heechanny@gmail.com',msg.as_string())

smtp.quit()