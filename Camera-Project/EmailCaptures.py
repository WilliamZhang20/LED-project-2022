# Written in July 2022
# In this program, I made a Raspberry Pi Camera Module take a photo every 10 seconds. After each capture, the program sends the photo to my email as an attachment.
# To take the photo, I imported the PiCamera library, and defined a camera object. Once the photo is taken, the file is stored. 
# To send the email, I used the SMTP (Simple Mail Transfer Protocol) server to access Yahoo mail and created the message with a MIME object. 
# To login before sending the email, I use my email address and app password. The app password is not the password used to login to yahoo. 
# To get an app password, I had to go to yahoo.com, then from my profile at the top right corner, I went to settings->account security->scroll down->generate app password. 
################################################ End of Comments ###############################################################
import smtplib, ssl
import time
from email import encoders
from picamera import PiCamera
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage

camera = PiCamera()
camera.rotation = 180 # the camera I used was placed upside down, so I flipped the view over 

for i in range(5): # repeats 5 times
        print "Take number", i+1
        time.sleep(5) # time for camera's light and focus adjustment
        camera.start_preview()
        camera.capture('/home/pi/project2022/cameraProject/projectPhotos/image%s.jpg' % i) # stores the photo in a folder for photos (called "projectPhotos")
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
        part.set_payload(open("projectPhotos/image%s.jpg"%i, "rb").read())  # the code itself is in the "cameraProject" folder (see line 17) so it must change directories to pull the photo
        encoders.encode_base64(part)  
        part.add_header('Content-Disposition', 'attachment; filename="projectPhotos/image%s.jpg"%i') 
        msg.attach(part)
                        
        s = smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465) # yahoo mail protocol -> (server address, port number) **Note: I used port number 465 because I also used SSL
        s.ehlo()
        s.login(email, password)
        s.sendmail(me, toaddr, msg.as_string())
        s.quit()
        time.sleep(5)  # since 1 photo is taken every 10 seconds, I give it another 5                       
