from django.contrib.auth.models import User
from django.forms import ModelForm


# this is for extends the User form, but i'm lazy
class userForm(ModelForm):
    class Meta:
        model = User
