from django.db import models

from norahs_ceramics.model_mixin import TimestapModel


class NewsletterUser(TimestapModel):
    email = models.EmailField(null=False, blank=False, primary_key=True)
    is_subscribed = models.BooleanField(null=False, default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    unsubscribed_at = models.DateTimeField(null=True)

    def subscribe(self):
        """Subscribe user"""
        if self.is_subscribed is False:
            self.is_subscribed = True
            self.save()
