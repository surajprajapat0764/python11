import smtplib 
try:
    server = smtplib.SMTP("smtp.gmail.com",port=587)
    server.starttls()

    ##receiver email
    receiver_mail = input("Enter the receiver email : ")
     
     ##mail credentials
    sender_mail = "surajprajapat0764@gmail.com"
    password = "znoz deoc nnig agnh"

    ##login
    server.login(sender_mail,password)

    ##sending email
    subject = input("Enter the subject :")
    body = input("Enter the body :")
    message = f"subject : {subject} \n \n {body}"
    server.sendmail(sender_mail,receiver_mail,message)
    print("mail sent successfully")

    server.quit()
except Exception as e :
    print("An Error occured",e)
