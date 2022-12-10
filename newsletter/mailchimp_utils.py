from django.conf import settings
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError


def subscribe(email: str) -> None:
    """Contains code handling the communication to the mailchimp api
    to create a contact/member in an audience/list.

    Args:
        email (str): Subscribed email address
    """

    mailchimp = Client()
    mailchimp.set_config(
        {
            "api_key": settings.MAILCHIMP_API_KEY,
            "server": settings.MAILCHIMP_DATA_CENTER,
        }
    )

    member_info = {
        "email_address": email,
        "status": "subscribed",
    }

    try:
        response = mailchimp.lists.add_list_member(
            settings.MAILCHIMP_EMAIL_LIST_ID, member_info
        )
        print("response: {}".format(response))
    except ApiClientError as error:
        print("An exception occurred: {}".format(error.text))
