import smtplib
server = smtplib.SMTP('smtp.mail.yahoo.com', 587)

#Next, log in to the server
server.login("login", "pwd")

#Send the mail
msg = '\nHello!' 
server.sendmail("sender@gmail.com", "target@gmail.com", msg)
