from django import forms
from django.core.validators import RegexValidator, validate_email
from phonenumber_field.formfields import PhoneNumberField


class PersonalInformationForm(forms.Form):
    """
    Regex validator doesn't allow special characters but it will allow also
    special French, German, Polish, Italian, Spanish, Swedish, Norvegian,
    Danish, Russian, Ukrainian, Serbian, Bulgarian, Belarusian
    letters.
    """

    only_letters = RegexValidator(
        (
            "^[a-zA-ZąćęłńóśźżĄĆĘŁŃÓŚŹŻ"
            "a-zA-ZàâäôéèëêïîçùûüÿæœÀÂÄÔÉÈËÊÏÎŸÇÙÛÜÆŒ"
            "a-zA-ZäöüßÄÖÜ"
            "a-zA-ZàèéìíîòóùúÀÈÉÌÍÎÒÓÙÚ"
            "a-zA-ZáéíñóúüÁÉÍÑÓÚÜ"
            "a-zA-ZäöåÄÖÅ"
            "a-zA-ZæøåÆØÅ"
            "а-яА-ЯёЁ"
            "а-щА-ЩЬьЮюЯяЇїІіЄєҐґ"
            "А-ИК-ШЂЈ-ЋЏа-ик-шђј-ћџ"
            "а-ъьюяА-ЪЬЮЯ"
            "ёа-зй-шы-яЁА-ЗЙ-ШЫІіЎў"
            "a-zA-ZĂÂÎȘȚăâîșț]*$"
        ),
        "No special characters and numbers allowed!",
    )

    p_phone_number = PhoneNumberField()
    p_first_name = forms.CharField(
        max_length=100, required=True, validators=[only_letters]
    )
    p_last_name = forms.CharField(
        max_length=100, required=True, validators=[only_letters]
    )
    p_email = forms.EmailField(
        max_length=254, required=True, validators=[validate_email]
    )


class ShippingAddressForm(forms.Form):
    s_address_1 = forms.CharField(max_length=50, required=True)
    s_address_2 = forms.CharField(max_length=100, required=True)
    s_town = forms.CharField(max_length=85, required=True)
    s_postcode = forms.CharField(max_length=8, required=True)
    s_county = forms.CharField(max_length=100, required=True)
    s_country = forms.CharField(max_length=100, required=True)
