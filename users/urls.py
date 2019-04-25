from django.urls import path, include
from . import views

urlpatterns = [

	path('api/',views.UserListView.as_view()),
	path('api/auth/',include('rest_auth.urls')),
	path('api/registration/',include('rest_auth.registration.urls')),

]