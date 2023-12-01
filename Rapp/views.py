from django.shortcuts import render,redirect
from . models import User,Slot,Table
from .forms import UsrForm,SlotForm,TableForm
from django.core.mail import send_mail
from Rport import settings
from django.contrib import messages
# Create your views here.

def home(request):
	return render(request,'html/home.html')
	
def about(request):
	return render(request,'html/about.html')

def menu(request):
	return render(request,'html/menu.html')

def shop(request):
	return render(request,'html/shop.html')
	
def registration(request):
	if request.method == "POST":
		g = UsrForm(request.POST)
		if g.is_valid():
			g.save()
			return redirect('/login')
	g = UsrForm()
	return render(request,'html/registration.html',{'t':g})

def upload(request):
	return render(request,'html/upload.html')
def contact(request):
	if request.method == "POST":
		e = request.POST['em'].split(',')
		s = request.POST['sb']
		d = request.POST['des']
		y = settings.EMAIL_HOST_USER
		z = send_mail(s,d,y,e)
		if z==1:
			messages.success(request,"Mail Sent Successfully")
			return redirect('/cnt')
		else:
			return HttpResponse("Not Sent")
	return render(request,'html/contact.html')

def booking(request):
	if request.method == "POST":
		t = SlotForm(request.POST)
		if t.is_valid():
			t.save()
			return redirect('/slot')
	t = SlotForm()
	return render(request,'html/slotbooking.html',{'r':t})	

def page(request):
	queryset = Slot.objects.all()
	context={
	"queryset":queryset,
	}
	return render(request,'html/slotpage.html',context)

def table(request):
	if request.method == "POST":
		b = TableForm(request.POST)
		if b.is_valid():
			b.save()
			return redirect('/table')
	b = TableForm()
	return render(request,'html/tablebooking.html',{'q':b})	
	
