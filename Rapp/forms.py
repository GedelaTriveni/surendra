from django.contrib.auth.forms import UserCreationForm 
from django import forms
from . models import User,Slot,Table

class UsrForm(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control my-2","placeholder":"Password Again"}))
	class Meta:
		model = User
		fields = ["username","email"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Username",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Mailid",
			}),
		}

class SlotForm(forms.ModelForm):
	class Meta:
		model = Slot
		fields = ["name","mail"]
		widgets = {
		"name":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter name",
			}),
		"mail":forms.EmailInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Mailid",
			}),
		}

class TableForm(forms.ModelForm):
	class Meta:
		model = Table
		fields = ["usrname","number","mobile","date","time"]
		widgets = {
		"usrname":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter name",
			}),
		"number":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Number of Chairs",
			}),
		"mobile":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Mobile Number",
			}),
		"date":forms.DateInput(attrs={"type":"date",
			"class":"form-control my-2",
			"placeholder":"Enter date",
			}),
		"time":forms.DateInput(attrs={"type":"time",
			"class":"form-control my-2",
			"placeholder":"Enter time",
			}),
		}

