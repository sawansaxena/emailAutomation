#Importing required libraries
import imaplib

import utilities

#Parameter for reading email fro mailbox
ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "" + ORG_EMAIL #enter email ID in space
FROM_PWD    = "" # enter passwird in space
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

#Connecting to the mailbox
mail = imaplib.IMAP4_SSL(SMTP_SERVER,SMTP_PORT)
mail.login(FROM_EMAIL,FROM_PWD)
mail.select('inbox')

#Reading the latest email from inbox
type,data = mail.search(None,'ALL')
mail_ids = data[0]
id_list = mail_ids.split()
first_email_id = id_list[0]
latest_email_id = id_list[-1]
typ, data = mail.fetch(latest_email_id, '(RFC822)')

#Read message from email
msg = utilities.getMsgFromEmail(data)

email_details ={}

email_details['from'] = msg['from']
email_details['to'] = msg['to']
email_details['subject'] = msg['subject']
email_details['body'] = utilities.readEmailBody(msg) #FUnction used to convert HTML into plain text

#Saving email content in text file
file_name = "email_" + '1' + ".txt"
output_file = open(file_name, 'w')
output_file.write("From: %s\nTo: %s\nSubject: %s\n\nBody: \n\n%s" %(email_details['from'], email_details['to'], email_details['subject'], email_details['body']))
#output_file.write(body.decode('utf-8'))
output_file.close()
            

     