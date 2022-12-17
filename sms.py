from twilio.rest import Client
import keys


def sendSms():
    client = Client(keys.account_sid, keys.auth_token)

    message = client.messages.create(body="Unknown Faces Found", from_=keys.twilio_number, to=keys.target_number)
    print(message.body)
