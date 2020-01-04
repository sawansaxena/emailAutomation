#Importing required libraries
import email
from bs4 import BeautifulSoup

def getMsgFromEmail(data):
    for response in data:
        if(isinstance(response,tuple)):
            msg = email.message_from_string(response[1].decode('ISO-8859-1'))
            return msg
        
def readEmailBody(msg):
    for part in msg.walk():
        body = part.get_payload(decode = True)
        soup = BeautifulSoup(body)
        
        for script in soup(["script", "style"]):
            script.extract()    # rip it out
            
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        
        return text
    
        