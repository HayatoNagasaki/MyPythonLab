# login check
import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "my@gmail.com"
#password = input("Type your password and press enter: ")
password=r"my password"

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
def main():
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    print("login")
    # TODO: Send email here

    server.quit() 

main()
