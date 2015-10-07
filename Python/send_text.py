from twilio import rest
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC47252981cf8b7b0e06e4cc893e16bcb0"
auth_token  = "992edc2ad2b6a00931c0c1ea8da8fac0"
client = rest.TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Jenny please?! I love you <3",
    to="+917506081105",    # Replace with your phone number
    from_="+12015140272") # Replace with your Twilio number
print message.sid