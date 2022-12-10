from django.core.mail import BadHeaderError, send_mail


def send_email(
    recipient_emails: list[str], sender_email: str, body: str, subject: str
) -> bool:
    """Send email wrapper function. Function will try to send email to given

    Args:
        recipient_emails (list[str]): List of recipients emails
        sender_email (str): Sender email address
        body (str): Email body content
        subject (str): Email subject

    Returns:
        bool: `True` if email was sent successfully, else `False`
    """
    try:
        send_mail(subject, body, sender_email, recipient_emails)
        return True
    except BadHeaderError:
        return False
