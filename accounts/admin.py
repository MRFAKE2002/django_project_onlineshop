from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm

@admin.register(CustomUser)
class CustomAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserChangeForm
    FORM = CustomUserChangeForm
    list_display = ('email', 'username',)
    
