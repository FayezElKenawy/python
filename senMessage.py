

from twilio.rest import Client\

account_sid = 'AC49bf4b5c1afda5f82bcd7ba7703bdb8c'
auth_token = '4ada314a417933cbcfa08ab21219b2f6'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello how are you ehab.......',
                              to='+966553891553',
                              from_='+17042282804'
                          )

print(message.sid)