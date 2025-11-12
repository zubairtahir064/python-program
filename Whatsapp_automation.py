from twilio.rest import Client
from datetime import datetime,timedelta
import time

account_sid = 'ACa1a8d99f305dc8483ff3cde993e029a3'
auth_token = 'b9421e9809960076a29da21742f30eb0'
client = Client(account_sid,auth_token)

def send_whatsapp_msg(recipent_number,message_body):
    try:
        message = client.messages.create(
            from_='Whatsapp:+14155238886',
            body=message_body,
            to=f'Whatsapp:{recipent_number}'
        )
        print(f'Message Send Successfully! Message SID{message.sid}')
    except Exception as e:
        print("An error occured!")
       

name = input("Enter the Recipient Name: ")
reipient_number = input("Enter the Recipient Whatsapp Number With Country Code (e.g,+12345): ")
message_body = input(f"Enter the Message you want to send to {name}: ")
date_str = input("Enter the date to send the massage (YYYY-MM-DD): ")
print(datetime.now())
time_str = input("Enter the time to send the message (HH:MM in 24hours format): ")

shedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
current_datetime = datetime.now()
time_diference = shedule_datetime-current_datetime
delay_seconds = time_diference.total_seconds()
print(delay_seconds)
if delay_seconds <= 0:
    print("The specified time is in the past. Please enter future date and time: ")
else:
    print(f'Message Scheduled to be send to {name} at {shedule_datetime}.')
    time.sleep(delay_seconds)
    send_whatsapp_msg(reipient_number,message_body)
