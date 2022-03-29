import os
import time
import random
import string   
import email, smtplib, ssl
#IMPORTS FOR CREATING FAKE NAME
import json
#import firstNameListFile
#import lastNameListFile
#IMPORTS FOR SEND EMAIL
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#IMPORTS FOR TAKE SCREEN SHOT
from PIL import ImageGrab
#IMPORTS FOR EMAIL OFFER
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
#IMPORTS FOR EMULATOR
from pyautogui import *
import pyautogui
import keyboard
import win32api, win32con

####################################################################
#                        CREATE EMAIL
#                       ###############
emailLength = 10
#creates a emailLength string with random numbers and letters
emailName = ''.join(random.choices(string.ascii_lowercase + string.digits, k = emailLength))
emailDomain = '@privaterelay.appleid.com'
emailAddress = emailName + emailDomain
print("===================================================")
print("Email Addredss :", emailAddress)
print("===================================================")

#######################################################################
#                       OPEN WEBSITE
print(">> NOW TRYING $15 OFFER")
s = Service("C:\Program Files (x86)\chromedriver.exe")        #PATH to chrome driver
browser = webdriver.Chrome(service = s)

url = "https://www.thelevelup.com/c/DZKQ7TBM0F"     #gets the website 
browser.get(url)                                     #gets the website


search = browser.find_element(By.ID, "email")            #searches for "ID: email" and returns the object
search.send_keys(emailAddress)                          #types 'emailAddress' in the object
search.send_keys(Keys.RETURN)                           #hits enter key
time.sleep(1)
browser.quit()                                                    #closes browser
#######################################################################
#                       ADD EMULATOR
print("===================================================")
#create first name
#gets a random number within the list length
getRandomFirstName = random.randint(0, 1001)
with open('firstNameListFile.json', "r") as f:
    firstNameData = json.load(f)
    firstName = firstNameData["names"][getRandomFirstName]
    print("First Name: ", firstName)
    
#create last name
getRandomLastName = random.randint(0, 151671)
#opens the last names file
with open('lastNameListFile.json', "r") as g:
    #loads all last names into lastNameData
    lastNameData = json.load(g)
    #gets the last name index of randomLastName
    lastName = lastNameData["lastNames"][getRandomLastName]
    print("Last Name: ", lastName)

fullName = firstName + " " + lastName
print("Full Name: ", fullName)
#create password
passwordLength = 20;
password = ''.join(random.choices(string.ascii_lowercase + string.digits, k = passwordLength));
print("Password: ", password)
print("===================================================")
print("First Rand", getRandomFirstName)
print("Last Rand", getRandomLastName)


  
#just click shit
pyautogui.click('taskBarMultiInstanceCHECK.PNG')
time.sleep(1)
pyautogui.click('instanceImageCheck.PNG')
time.sleep(1)
pyautogui.click('cloneInstanceCheck.PNG')
time.sleep(1)
pyautogui.click('createImageCompare.PNG')
time.sleep(1)
pyautogui.click('DONT FUCK UP MY BUTTON.PNG')
time.sleep(1)    
pyautogui.click('newInstanceCompare.PNG')
time.sleep(20)   
pyautogui.click('humanBeanAPP.PNG')
time.sleep(4)   
pyautogui.click('signUpCompare.PNG')
time.sleep(2)     
pyautogui.write(emailAddress)
time.sleep(1)
pyautogui.press('tab')
time.sleep(1) 
pyautogui.press('enter')
time.sleep(1) 
pyautogui.write(firstName)
time.sleep(1)
pyautogui.press('tab')
time.sleep(1) 
pyautogui.write(lastName)
time.sleep(1)
pyautogui.press('tab')
time.sleep(1) 
pyautogui.write(password)
time.sleep(1)
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(2)  
pyautogui.click('skipALLDOB.PNG')
time.sleep(2)      
pyautogui.press('down')
pyautogui.press('left')    
pyautogui.press('enter')       
pyautogui.click('QRCODECOMPARE.PNG')      
qrCODE = pyautogui.locateOnScreen('ACTUALQRCODE.PNG')
print("===================================================")
print("===================================================")
print(qrCODE)
print("===================================================")
print("===================================================")
time.sleep(5)




#######################################################################
#                       TAKE SCREEN SHOT

printEmailAddress = emailAddress + ".png"
#find the box the qr code will be in
    #right >= left
    #lower >= upper
    #width = right - left
    #height = lower - upper
left  = 50
upper = 50
right = 1000
lower = 900
#create the box with the requred dimentions
bbox = (left, upper, right, lower)
#screenShot the box 
myscreen = ImageGrab.grab(bbox)
#save it to

myscreen.save(printEmailAddress)
print("Screenshot saved as ", printEmailAddress)

#######################################################################
#                       Quit the chrome tab
#driver.quit()  
#######################################################################
#                       SEND SCREENSHOT TO EMAIL

subject = "ADD THE SUBJECT LINE"
body = "This is an email with attachment sent from a click of a button :) \n email = " + emailAddress + "\n First Name = " + firstName + "\n Last Name = " + lastName + "\nPassword = " + str(password)

sender_email = "ENTER_THE_EMAIL_YOU_WANT_TO_USE_TO_SEND@gmail.com"                 
receiver_email = "ENTER_THE_EMAIL_YOU_WANT_TO_RECIEVE@gmail.com"
sender_email_password = "PASSWORDFORSENDEREMAIL" 


#password = input("Type your password and press enter:")
# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email  # Recommended for mass emails

# Add body to email
message.attach(MIMEText(body, "plain"))

filename = printEmailAddress  # In same directory as script

# Open PDF file in binary mode
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, sender_email_password)
    server.sendmail(sender_email, receiver_email, text)
print("PICTURE SENT TO: ", receiver_email)



















