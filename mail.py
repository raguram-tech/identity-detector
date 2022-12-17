import sendgrid
import base64
from sendgrid import Attachment, FileContent, FileName, FileType, Disposition
from sendgrid.helpers.mail import Mail, Email, To, Content
from python_http_client.exceptions import HTTPError


def sendMail(image):
    sg = sendgrid.SendGridAPIClient(api_key='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')
    from_email = Email("nivethavadivel.1@gmail.com")  # Change to your verified sender
    to_email = To("sayhitomouli@gmail.com")  # Change to your recipient
    subject = "Intruders Seen"
    content = Content("text/plain", "Unknown Faces found")

    file = image
    with open(file, 'rb') as f:
        data = f.read()
        f.close()
    encoded_file = base64.b64encode(data).decode()
    attachedFile = Attachment(
        FileContent(encoded_file),
        FileName(file),
        FileType(file),
        Disposition('attachment')
    )
    mail = Mail(from_email, to_email, subject, content)
    mail.attachment = attachedFile

    # Get a JSON-ready representation of the Mail object
    mail_json = mail.get()

    # Send an HTTP POST request to /mail/send
    try:
        response = sg.client.mail.send.post(request_body=mail_json)
        print(response.status_code)
        print(response.headers)
    except HTTPError as e:
        print(e.to_dict)
