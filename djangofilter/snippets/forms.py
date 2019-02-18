from django import forms


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(label='E-mail')
    category = forms.ChoiceField(choices[('question', 'Question'), ('other', 'Other')])
    subject = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea)
    # Textarea gives more space than a regular CharField
