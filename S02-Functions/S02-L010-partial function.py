import smtplib
import functools

def SendInfoEmail(user, password, mailFrom, mailTo, mailSubject, mailBody):
    message = '''From: {}
    Subject: {}
    
    {}
    '''.format(mailFrom, mailSubject, mailBody)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(user, password)
        server.sendmail(user, mailTo, message)
        server.close()
        print('mail sent')
    except:
        print('error sending email')

mailFrom = 'Your automation system'
mailTo = ['robixxo.76@gmail.com']
mailSubject = 'Processing finished successfully'
mailBody = '''Hello

This mail confirms that processing has finished without problems,

Have a nice day!'''

user = 'robixxo.76@gmail.com'
password = 'x3e&hVj6bjqLUV'

SendInfoEmail(user, password, mailFrom, mailTo, mailSubject, mailBody)


SendInfoEmailFromGmail = functools.partial(SendInfoEmail, user, password)

#wywołuje oryginalną funkcję, nie musimy pamiętać o dodaniu w w funkcji usera i password
SendInfoEmailFromGmail(mailFrom, mailTo, mailSubject, mailBody)
