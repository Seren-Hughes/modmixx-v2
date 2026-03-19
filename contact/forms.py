from django import forms
from django import forms
from captcha.fields import ReCaptchaField  # type: ignore
from captcha.widgets import ReCaptchaV3  # type: ignore


class ContactForm(forms.Form):
    """
    Contact form with honeypot spam detection.

    Allows users to send messages to site administrators with built-in
    spam protection via hidden honeypot field that bots typically fill.

    Fields:
        name: CharField max 100 chars (user's full name)
        email: EmailField (user's email for response)
        subject: CharField max 200 chars (message subject)
        message: TextField (main message content)
        website: HiddenInput honeypot field (spam detection)

    Spam Protection:
        Hidden 'website' field that legitimate users won't fill but
        spam bots will. Form validation rejects if honeypot is filled.

    Validation:
        - All fields except honeypot are required
        - Email field validates format automatically
        - Honeypot field triggers ValidationError if filled
    """

    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=200, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    website = forms.CharField(
        required=False, widget=forms.HiddenInput
    )  # Honeypot field to catch spam bots
    captcha = ReCaptchaField(widget=ReCaptchaV3())

    def clean_website(self):
        data = self.cleaned_data["website"]
        if data:
            raise forms.ValidationError("Spam detected.")
        return data
