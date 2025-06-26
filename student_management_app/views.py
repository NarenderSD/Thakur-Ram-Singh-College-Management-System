from django.shortcuts import render,HttpResponse, redirect,HttpResponseRedirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.hashers import make_password, check_password
from .models import CustomUser, Staffs, Students, AdminHOD, Courses, SessionYearModel, ContactMessage
from django.contrib import messages

def home(request):
	return render(request, 'home.html')


def contact(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		phone = request.POST.get('phone')
		desc = request.POST.get('desc')
		if name and email and phone and desc:
			ContactMessage.objects.create(name=name, email=email, phone=phone, message=desc)
			messages.success(request, 'Your message has been sent! We will get back to you soon.')
		else:
			messages.error(request, 'Please fill all fields.')
		return render(request, 'contact.html')
	return render(request, 'contact.html')


def loginUser(request):
	return render(request, 'login_page.html')

def doLogin(request):
	
	print("here")
	email_id = request.GET.get('email')
	password = request.GET.get('password')
	# user_type = request.GET.get('user_type')
	print(email_id)
	print(password)
	print(request.user)
	if not (email_id and password):
		messages.error(request, "Please provide all the details!!")
		return render(request, 'login_page.html')

	# Find user by email
	user = CustomUser.objects.filter(email=email_id).first()
	if not user:
		messages.error(request, 'Invalid Login Credentials!!')
		return render(request, 'login_page.html')
	
	# Check password
	if not check_password(password, user.password):
		messages.error(request, 'Invalid Login Credentials!!')
		return render(request, 'login_page.html')

	login(request, user)
	print(request.user)

	if user.user_type == CustomUser.STUDENT:
		return redirect('student_home/')
	elif user.user_type == CustomUser.STAFF:
		return redirect('staff_home/')
	elif user.user_type == CustomUser.HOD:
		return redirect('admin_home/')

	return render(request, 'home.html')

	
def registration(request):
	return render(request, 'registration.html')
	

def doRegistration(request):
	if request.method == 'POST':
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		email_id = request.POST.get('email')
		password = request.POST.get('password')
		confirm_password = request.POST.get('confirmPassword')

	print(email_id)
	print(password)
	print(confirm_password)
	print(first_name)
	print(last_name)
	if not (email_id and password and confirm_password):
		messages.error(request, 'Please provide all the details!!')
		return render(request, 'registration.html')
	
	if password != confirm_password:
		messages.error(request, 'Both passwords should match!!')
		return render(request, 'registration.html')

	is_user_exists = CustomUser.objects.filter(email=email_id).exists()

	if is_user_exists:
		messages.error(request, 'User with this email id already exists. Please proceed to login!!')
		return render(request, 'registration.html')

	user_type = get_user_type_from_email(email_id)

	if user_type is None:
		messages.error(request, "Please use valid format for the email id: '<username>.<staff|student|hod>@<college_domain>'")
		return render(request, 'registration.html')

	username = email_id.split('@')[0].split('.')[0]

	if CustomUser.objects.filter(username=username).exists():
		messages.error(request, 'User with this username already exists. Please use different username')
		return render(request, 'registration.html')

	user = CustomUser()
	user.username = username
	user.email = email_id
	user.password = make_password(password)
	user.user_type = user_type
	user.first_name = first_name
	user.last_name = last_name
	user.save()
	messages.success(request, 'Registration successful! Please login.')
	return redirect('login')

	
def logout_user(request):
	logout(request)
	return HttpResponseRedirect('/')


def get_user_type_from_email(email_id):
	"""
	Returns CustomUser.user_type corresponding to the given email address
	email_id should be in following format:
	'<username>.<staff|student|hod>@<college_domain>'
	eg.: 'abhishek.staff@jecrc.com'
	"""

	try:
		email_id = email_id.split('@')[0]
		email_user_type = email_id.split('.')[1]
		return CustomUser.EMAIL_TO_USER_TYPE_MAP[email_user_type]
	except:
		return None

def student_home(request):
	try:
		student_obj = Students.objects.get(admin=request.user.id)
		context = {
			"user": request.user,
			"student": student_obj,
		}
		return render(request, 'student_template/student_home.html', context)
	except Exception as e:
		pass

def staff_home(request):
	try:
		staff_obj = Staffs.objects.get(admin=request.user.id)
		context = {
			"user": request.user,
			"staff": staff_obj,
		}
		return render(request, 'staff_template/staff_home.html', context)
	except Exception as e:
		pass

def admin_home(request):
	try:
		user = CustomUser.objects.get(id=request.user.id)
		contact_message_count = ContactMessage.objects.count()
		context = {
			"user": user,
			"id": user.id,
			"contact_message_count": contact_message_count,
		}
		return render(request, 'hod_template/home_content.html', context)
	except Exception as e:
		pass

def hod_contact_messages(request):
	if not request.user.is_authenticated or not hasattr(request.user, 'adminhod'):
		messages.error(request, 'You are not authorized to view this page.')
		return redirect('login')
	messages_list = ContactMessage.objects.all().order_by('-created_at')
	contact_message_count = ContactMessage.objects.count()
	return render(request, 'hod_template/contact_messages.html', {'messages_list': messages_list, 'contact_message_count': contact_message_count})
