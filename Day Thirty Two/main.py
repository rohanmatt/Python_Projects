
import smtplib
my_email = "alwaysgamesbro01@gmail.com"
password = "whatthehell@123"

connection= smtplib.SMTP("smtp.gmail.com") 
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="rohanroymathew0001@gmail.com",msg="Subject:Hello\n\nThis is the body of my email." )