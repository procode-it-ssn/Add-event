from django import forms

class EventForm(forms.Form):
    eventName = forms.CharField(label = 'Event Name',max_length=100,widget = forms.TextInput(attrs={'class':'border-solid border border-gray-600'}))
    speaker = forms.CharField(label = 'Speaker',max_length = 100,widget = forms.TextInput(attrs={'class':'border-solid border border-gray-600'}))
    regLink = forms.URLField(widget = forms.TextInput(attrs={'class':'border-solid border border-gray-600'}))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class':'border-solid border border-gray-600'
    }), required=False)
