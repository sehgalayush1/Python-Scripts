import smtplib

server= smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("jain.rishabh170895@gmail.com","rishabh170895")
msg=str(raw_input("Enter your Message:"))
e_mail=str(raw_input("Enter Receiver's email address:"))
server.sendmail("jain.rishabh170895@gmail.com",e_mail,msg)
server.quit()
