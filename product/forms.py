from django import forms

from product.models import Color

SORT_BY = [
    ("", "sort by"),
    ("name_asc", "name A-Z"),
    ("name_desc", "name Z-A"),
    ("price_asc", "price low to high"),
    ("price_desc", "price high to low"),
]

COLORS = [
    ("white", "white"),
    ("black", "black"),
    ("red", "red"),
    ("blue", "blue"),
    ("grey", "grey"),
    ("beige", "beige"),
    ("transparent", "transparent"),
]


class FilterForm(forms.Form):
    min_price = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "type": "range",
                "min": "1",
                "max": "150",
                "id": "min",
                "class": "range",
                "value": "1",
            }
        ),
        required=False,
    )

    max_price = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "type": "range",
                "min": "1",
                "max": "150",
                "id": "max",
                "class": "range",
                "value": "150",
            }
        ),
        required=False,
    )

    category = forms.CharField(widget=forms.HiddenInput())
    sub_category = forms.CharField(widget=forms.HiddenInput())

    colors = forms.MultipleChoiceField(
        choices=COLORS,
        widget=forms.RadioSelect,
        label="",
    )

    sort_by = forms.CharField(
        required=False,
        label="",
        widget=forms.Select(choices=SORT_BY),
    )
