from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

def sending_sms(text='Wake up Neo...', receiver=None):
    try:
        account_sid = os.getenv('SID')
        auth_token = os.getenv('AUTH_TOKEN')

        if not account_sid or not auth_token:
            raise ValueError('Twilio credentials are missing!')

        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=text,
            from_='+15138981827',
            to=receiver
        )
        return 'Сообщение успешно отправлено!'
    except Exception as ex:
        return 'Что-то пошло не так... :(', ex

def main():
    text = input('Пожалуйста введите ваше сообщение: ')
    receiver = os.getenv('RECEIVER_PHONE')
    print(sending_sms(text=text, receiver=receiver))

if __name__ == '__main__':
    main()
