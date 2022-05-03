from twilio.rest import Client

account_sid = 'ACefa4304355db724e03dce9953cf63d6c'
auth_token = '8afaa3e1deb8c45766472c8f5d3eddae'
client = Client(account_sid, auth_token)
for i in range(1):
    message = client.calls \
            .create(
                     twiml='<Response><Say></Say></Response>',
                     from_='+12563048896',
                     to='+919075516408'
                 )

print(message.sid)