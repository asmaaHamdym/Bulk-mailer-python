import smtplib
sender = "hamzawanes01@gmail.com"
receipient = ['asmahamdym@gmail.com', 'engasmamahrous@gmail.com']
first_name = 'Asma'
password = 'Semsemah1'
subject = 'test'
message = f'Hi, {first_name}'

smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
smtpObj.login(sender, password)
smtpObj.sendmail(sender, receipient, message)