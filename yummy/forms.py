from django import forms
from person.models import Person

class Personform(forms.Form):
    gender = forms.ChoiceField(required=True,choices=((u'男', u'男'), (u'女', u'女')))
    city = forms.CharField(required=True,label=u'城市',max_length=50)
    class Meta:
       model = Person
       fields = ('gender', 'city',)


class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField(required=False,label='Your e-mail address')
    message = forms.CharField(widget=forms.Textarea)
    
    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message)
        if num_words < 10:
            raise forms.ValidationError("Not enough words!")
        return message