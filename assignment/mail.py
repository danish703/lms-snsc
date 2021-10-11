from django.template import context
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.conf.global_settings import EMAIL_HOST_USER
def sendMail(email=None,name=None,message=None):
    ctx = {
        'name':name,
        'message':message,
    }
    message = get_template('mail/email.html').render(ctx)
    msg = EmailMessage(
        'Assignment created',
        message,
        EMAIL_HOST_USER,
        [email,]
    )
    msg.content_subtype="html"
    try:
        msg.send()
        return "success"
    except Exception as e:
        return e