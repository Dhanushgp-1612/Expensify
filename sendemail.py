import smtplib
from email.message import EmailMessage
def forgotemail(TEXT,tomail):
    msg = EmailMessage()
    msg['Subject'] = 'Forgot your Username/Password'
    msg['From'] = 'expensify.in@gmail.com'
    msg['To'] = tomail
    msg.set_content('')
    msg.add_alternative(TEXT,subtype='html')


    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login('expensify.in@gmail.com','Expensify123')
        smtp.send_message(msg)
        

def limitexceed(TEXT,tomail):
    msg = EmailMessage()
    msg['Subject'] = 'Alert!! Monthly Limit Exceeded'
    msg['From'] = 'expensify.in@gmail.com'
    msg['To'] = tomail
    msg.set_content('')
    msg.add_alternative(TEXT,subtype='html')


    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login('expensify.in@gmail.com','Expensify123')
        smtp.send_message(msg)

   
