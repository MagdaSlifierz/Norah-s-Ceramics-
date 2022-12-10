from django import forms

from reviews.models import ProductReview


class ProductReviewForm(forms.ModelForm):
    TYPE_SELECT = (
        (1, "☆"),
        (2, "☆"),
        (3, "☆"),
        (4, "☆"),
        (5, "☆"),
    )
    description = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                "class": "rev-description",
                "rows": 4,
                "maxlength": "1500",
                "style": "resize:none",
                "placeholder": "write your review here...",
            }
        ),
    )
    stars = forms.TypedChoiceField(
        required=True,
        choices=TYPE_SELECT,
        coerce=int,
        widget=forms.RadioSelect(),
    )

    class Meta:
        model = ProductReview
        fields = ["description", "stars"]
