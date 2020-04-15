from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
class UserCreateform(UserCreationForm):

    address = forms.CharField(max_length=150, required=True)
    phone_number = forms.IntegerField(required=True)

    class Meta(UserCreationForm.Meta):

        model = get_user_model()
        fields = ('username','email','password1','password2')


        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            self.fields['username'].label = 'Display Name'
