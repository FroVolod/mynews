from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from mynews.celery import app
 
 
@app.task
def send_email_to_author(receipient, post):
    subject = "Hello, its MYNEWS"
    text_content = f'You have received a new message in your publication: {post}'
    html_content = f'<p>You have received a new message in your publication:</p> \
                    <p><strong>{post}</strong></p>'
    msg = EmailMultiAlternatives(subject, text_content, settings.DEFAULT_FROM_EMAIL, [receipient])
    msg.attach_alternative(html_content, "text/html")
    respone = msg.send()
