import sendgrid
import json

SENDGRID_API_KEY = "<your_sendgrid_key>"
EMAIL_FROM = "no-reply@test.com"

def make_email_to(emails):
    email_to = []
    for e in emails:
        email_to.append({"email": e})
    return email_to


def send_email_handler(event, context):
    print(event['Records'][0]['Sns']['Message'])
    template_id = event['Records'][0]['Sns']['Message']['TemplateId']
    subject = event['Records'][0]['Sns']['Message']['Subject']
    emails = event['Records'][0]['Sns']['Message']['EmailTo']
    substitutions = event['Records'][0]['Sns']['Message']['Substitude']
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