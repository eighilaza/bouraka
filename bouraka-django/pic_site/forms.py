from django import forms
from newsletter.models import Subscription

class SubscriptionForm(forms.ModelForm):

	class Meta :
		model = Subscription
		widgets = { 'email_field' : forms.TextInput(attrs={'class':'form-control'}), 
		}
		labels = {'email_field' : '',}
		fields=('email_field',)
