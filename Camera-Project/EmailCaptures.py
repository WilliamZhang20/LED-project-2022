import smtplib, ssl
import time
from email import encoders
from picamera import PiCamera
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage

camera = PiCamera()
camera.rotation = 180 # the camera I used had to be placed upside down, so I flipped it over 

for i in range(5): # take 5 times
        print "Take number", i+1
        time.sleep(5) # time for camera self-orientation
        camera.start_preview()
        camera.capture('/home/pi/project2022/cameraProject/projectPhotos/image%s.jpg' % i) # stores the photo
        camera.stop_preview()

        toaddr = 'wzhang20@yahoo.com'
        email = 'wzhang20@yahoo.com'
        password = '***************' # enter yahoo app password (not email password, generated from yahoo.com account settings)
        me = 'wzhang20@yahoo.com'
        subject = "Raspberry Pi Cam"
                       
        msg = MIMEMultipart() # object of type instance
        msg['Subject'] = subject
        msg['From'] = me
        msg['To'] = toaddr
        msg.preamble = "Test"

        part = MIMEBase('application', "octet-stream")  
        part.set_payload(open("projectPhotos/image%s.jpg"%i, "rb").read())  
        encoders.encode_base64(part)  
        part.add_header('Content-Disposition', 'attachment; filename="projectPhotos/image%s.jpg"%i') 
        msg.attach(part)
                        
        s = smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465) # yahoo mail protocol -> (server address, port number) **Note: I used port number 465 because I also used SSL
        s.ehlo()
        s.login(email, password)
        s.sendmail(me, toaddr, msg.as_string())
        s.quit()
        time.sleep(5)  # since 1 photo is taken every 10 seconds, I give it another 5                       
