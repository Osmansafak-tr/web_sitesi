from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .forms import KullanıcıCreationForm,KullanıcıChangeForm
from .models import VarsayılanKullanıcı

# Register your models here.
class KullanıcıAdmin(UserAdmin):
    form = KullanıcıChangeForm
    add_form = KullanıcıCreationForm
    model = VarsayılanKullanıcı

admin.site.register(VarsayılanKullanıcı,KullanıcıAdmin)
