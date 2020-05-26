import smtplib
a=" Welcome To E-mail Sender Tool "
print(a.center(100,'*'))
print()
m="Please enable third-party access in your emails security settings.In case of gmail visit : https://myaccount.google.com/security  then enable less secure apps"
print(m)
print()

sender_email=input(str("Enter your Email : "))
password=input(str("Enter your Password : "))
rec_email=input(str("Enter recepient Email : "))
message=input("Enter your Text-message : ")

server=smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()

server.login(sender_email,password)
print("LogIn Successfull")

server.sendmail(sender_email,rec_email,message)
print("Email has been sent successfully to "+rec_email)
