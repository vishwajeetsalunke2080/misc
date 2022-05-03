from twilio.rest import Client

account_sid = 'AC5d1222490654e227e26b03d52f78ea58'
auth_token = 'b0677d4a41f09b4ef026e47bbd8650cb'
client = Client(account_sid, auth_token)
message = Client.messages=

print(message.sid)