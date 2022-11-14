import os
from sendgrid import SendGridAPIClient

message = {
    'personalizations': [
        {
            'to': [
                {
                    'email': 'test@example.com'
                }
            ],
            'subject': 'Sending with Twilio SendGrid is Fun'
        }
    ],
    'from': {
        'email': 'test@example.com'
    },
    'content': [
        {
            'type': 'text/plain',
            'value': 'and easy to do anywhere, even with Python'
        }
    ]
}
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(str(e))
