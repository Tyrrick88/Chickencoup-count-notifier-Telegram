import smtplib, ssl

smtp_server = ('smtp.gmail.com')

port = 465
sender_email = input("Enter senders e-mail: ")
senderEmail_password = input("Enter the senders e-mail password: ")
reciever_email = input("Enter the recievers e-mail: ")
smtp_server = ('smtp.gmail.com')
message ="""\
Subject:Chicken Coup count

Helle there!

The chicken in your coup at the moment are {CHICKEN_COUP_COUNT} at the moment.

 """

# Creating a default context.

context = ssl.create_default_context()

# initiate the G-mail  server/client with SSL and port number

with smtplib.SMTP(smtp_server, port, context=context) as server:
    server.ehlo()
    server.login(sender_email, senderEmail_password)
    server.ehlo()
    server.starttls()
    server.sendmail(sender_email, reciever_email, message)
    server.quit()

    
                