# loveAutomation
WhatsApp Automation to Send Messages to your loved ones

External Dependencies : twilio, 
                        APScheduler
                        
 Step-1: Create a free Twilio account and confirm your email and mobile number.

Also, a free tier Twilio account requires using Twilio Sandbox for WhatsApp, which means you can’t use your number and have to go through one-time permission to receive WhatsApp messages.
Both can be solved when you get your own number, which is done after WhatsApp approves Twilio to use your number. There is a form to fill out and a wait time too.

All of this is discouraging, but our free tier solution does the job fine. Also, for now, this is the only available way.
Now you have to connect the receiver’s phone to the WhatsApp Sandbox to start receiving messages.
Go to WhatsApp beta in the learn section of the console.


Save the WhatsApp number assigned to you in your contacts. You can give it any name you want. For simplicity, I saved it as Twilio Sandbox, then sent it a message from my dad’s phone, as seen above. This has to be done once and only once.
Now go to Twilio Console and get your account SSID and authentication token. This will help Twilio know it’s you when the code is executed.

Step 2: Understanding and Modifying the Code
Download the GitHub repository and extract it.

Inside this, you’ll find our code file and deployment package.



