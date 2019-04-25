from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):

	form = CustomUserCreationForm

	change_form = CustomUserChangeForm

	list_display = ("username","email","name")

	model = CustomUser

admin.site.register(CustomUser, CustomUserAdmin)