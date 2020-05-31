from twilio.rest import Client
 
account_sid = 'ACc02ebe530aa975f0b4f13e2120736236' 
auth_token = '7b6d5c25370dd83ce6838447c3558435' 
client = Client(account_sid, auth_token) 
def send_love():
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Good Morning Janu😇😇',      
                              to='whatsapp:+916353385060' 
                          ) 
 
    print(message.sid)