import os
from sendgrid import SendGridAPIClient

sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
response = sg.client.suppression.bounces.get()
print(response.status_code)
print(response.body)
print(response.headers)
