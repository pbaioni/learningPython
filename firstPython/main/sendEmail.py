import smtplib

msg = "\r\n".join([
  "From: paolobaionitoulouse@gmail.com",
  "To: baioni2002@yahoo.fr",
  "Subject: Hello from python script",
  "",
  "This is the text of the email: hello!"
  ])

server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()

#the login can be successful only if the "less secure apps" option is turned on
#you can set the option here: https://myaccount.google.com/lesssecureapps
server.login("paolobaionitoulouse@gmail.com", "putTheRightPassword")

server.sendmail("paolobaionitoulouse@gmail.com", "baioni2002@yahoo.fr", msg)
server.close()