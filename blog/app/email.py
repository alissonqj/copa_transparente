from flask import render_template
from app import app
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_mail(subject, sender, recipients, text_body, html_body):
    try:
        msg = Mail(
            subject=subject,
            from_email=sender,
            to_emails=recipients,
            html_content="<strong>and easy to do anywhere, even with Python</strong>",
            # plain_text_content=text_body,
        )
        sg = SendGridAPIClient(app.config["SENDGRID_API_KEY"])
        sg.send(msg)
    except Exception as e:
        raise e


def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_mail(
        "[[Microblog] Resete sua senha]",
        sender=app.config["ADMINS"][0],
        recipients=[user.email],
        text_body=render_template("email/reset_password.txt", user=user, token=token),
        html_body=render_template("email/reset_password.html", user=user, token=token),
    )
