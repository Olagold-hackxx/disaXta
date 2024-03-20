import threading

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


class EmailThread(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


class Util:
    @staticmethod
    def send_email(data):
        html_message = render_to_string(data["template_name"], data["context"])
        plain_message = strip_tags(html_message)
        email = EmailMultiAlternatives(
            subject=data["email_subject"],
            body=plain_message,
            from_email=data["from_email"],
            to=[data["to_email"]],
        )
        email.attach_alternative(html_message, "text/html")
        email.send()
