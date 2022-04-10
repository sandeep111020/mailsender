import smtplib
  
# list of email_id to send the mail
# here i changes mail def to defi beacause it matches with the def keyword
li = [ghi@hotmail.com, defi@yahoo.com, ghi@gmail.com, abc@channelier.com, abc@hotmail.com, defi@hotmail.com, abc@gmail.com, abc@yahoo.com, defi@channelier.com,jkl@hotmail.com, ghi@yahoo.com, defi@gmail.com ]
li.sort()
for dest in li:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("sender_email", "sender_password")
    message = "Message_you_need_to_send"
    s.sendmail("sender_password", dest, message)
    s.quit()