from django.core.mail import EmailMultiAlternatives

from mynews.settings import DEFAULT_FROM_EMAIL
from mynews.celery import app
 
 
@app.task
def send_email_to_author(email, post):
    subject = "Hello, its MYNEWS"
    text_content = f'You have received a new message in your publication: {post}'
    html_content = f'<p>You have received a new message in your publication:</p> \
                    <p><strong>{post}</strong></p>'
    sender = DEFAULT_FROM_EMAIL
    receipient = email
    msg = EmailMultiAlternatives(subject, text_content, sender, [receipient])
    msg.attach_alternative(html_content, "text/html")
    respone = msg.send()
