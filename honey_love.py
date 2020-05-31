from twilio.rest import Client
 
account_sid = 'your account sid' 
auth_token = 'and your auth token goes here' 
client = Client(account_sid, auth_token) 
def send_love():
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Good Morning😇😇',      
                              to='whatsapp:+0123123123' 
                          ) 
 
    print(message.sid)
