from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import TextInput, PasswordInput, CharField, Form

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username',)
        widgets = {
            'username': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Nom d'utilisateur"
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs.update({
            "class": "form-control my-3",
            "placeholder": "Mot de passe",
        })
        self.fields["password2"].widget.attrs.update({
            "class": "form-control my-3",
            "placeholder" : "Confirmer",
        })

class LoginForm(Form):
    username = CharField(max_length=150, label='Nom d’utilisateur')
    password = CharField(max_length=150, widget=PasswordInput, label='Mot de passe')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            "class": "form-control my-3",
            "placeholder": "Nom d'utilisateur",
        })
        self.fields["password"].widget.attrs.update({
            "class": "form-control my-3",
            "placeholder": "Mot de passe",
        })