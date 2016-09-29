import sendgrid
import json

SENDGRID_API_KEY = "your_api_key"
EMAIL_FROM = "no-reply@test.com"

def make_email_to(emails):
    email_to = []

    for e in emails:
        email_to.append({"email": e})

    return email_to


def send_email_handler(event, context):
    json_message = eval(event['Records'][0]['Sns']['Message'])
    print(json_message)
    template_id = json_message['TemplateId']
    subject = json_message['Subject']
    emails = json_message['EmailTo']
    substitutions = json_message['Substitude']
    data = {
        "personalizations": [
            {
                "to": make_email_to(emails),
                "subject": subject,
                "substitutions": substitutions,
            }
        ],
        "from": {
            "email": EMAIL_FROM
        },
        "template_id": template_id
    }
    sg = sendgrid.SendGridAPIClient(apikey=SENDGRID_API_KEY)
    response = sg.client.mail.send.post(request_body=data)
    print(response.status_code)
    print(response.body)
    print(response.headers)