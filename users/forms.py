from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

	class Meta:

		fields = ("email",'username')

		model = CustomUser

class CustomUserChangeForm(UserChangeForm):

	class Meta:

		model = CustomUser

		fields = UserChangeForm.Meta.fields

