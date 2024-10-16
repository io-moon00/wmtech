from django import forms
#from django_recaptcha.fields import ReCaptchaField
#from django_recaptcha.widgets import ReCaptchaV3


class ContactForm(forms.Form):
    prename = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'block p-3 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 shadow-sm focus:ring-main focus:border-main'}))
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'block p-3 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 shadow-sm focus:ring-main focus:border-main'}))
    email = forms.EmailField(max_length=254, required=True,  widget=forms.TextInput(attrs={'class': 'block p-3 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 shadow-sm focus:ring-main focus:border-main'}))
    phone = forms.EmailField(max_length=254, required=False,  widget=forms.TextInput(attrs={'class': 'block p-3 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 shadow-sm focus:ring-main focus:border-main'}))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg shadow-sm border border-gray-300 focus:ring-main focus:border-main'}))
    #captcha = ReCaptchaField(widget=ReCaptchaV3(), label=False, error_messages={
        #'inv': 'reCaptcha-Validierung fehlgeschlagen. Bitte versuche es später noch einmal oder kontaktiere mich via info@cams-world.de, wenn das Problem weiterhin besteht.'
    #})