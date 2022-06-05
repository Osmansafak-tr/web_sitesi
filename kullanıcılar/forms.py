from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import VarsayılanKullanıcı

class KullanıcıCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = VarsayılanKullanıcı
        fields = UserCreationForm.Meta.fields+('unvan',)

class KullanıcıChangeForm(UserChangeForm):
    class Meta:
        model = VarsayılanKullanıcı
        fields = UserChangeForm.Meta.fields