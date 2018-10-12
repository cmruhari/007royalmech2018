import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
#Next, log in to the server
server.login("haripramod92@gmail.com", "hari560066")
#Send the mail
msg = "undaaaa" # The /n separates the message from the headers
server.sendmail("haripramod92@gmail.com", "viraaat786@gmail.com", msg)
server.quit()