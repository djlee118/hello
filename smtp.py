import smtplib
from email.message import EmailMessage

smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtp.ehlo()
smtp.login('leedj118@gmail.com', 'xxxx')
msg = EmailMessage()
msg['SubJect'] = '안녕하세요'
msg['From'] = ''
msg['To'] = 'djlee118@nate.com'
msg.set_content('반갑습니다. 처음으로 보내는 메시지 입니다. \n좋은 하루 되세요')
smtp.send_message(msg)
smtp.quit()


