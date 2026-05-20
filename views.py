# Create your views here.

from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import CustomUser
from django.contrib.auth import logout
from jquery import $

# from .models import Booking  # Assuming you have a Booking model defined
# hotels/views.py
from django.shortcuts import render, redirect, get_object_or_404
# from .forms import CustomUserCreationForm
# from admin.models import Admin
# Register View

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,"Username already exists !")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,"Email already exists !")
                    return redirect('register')
                else:
                    user=User.objects.create_user(username=username,password=password,
                                                  email=email,first_name=first_name,last_name=last_name)
                    user.save()
                    messages.success(request,"You are now registered and can log in !")
                    return redirect('login')
        else:
            messages.error(request,"Password do not match !")
            return redirect('register')
    else:
        return render(request, 'register.html') 

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            # messages.success(request,"You are now logged in !")
            return redirect('paytutorials')
#           return render(request, 'paytutorial.html')
        else:
            messages.error(request,"Invalid credentials !")
            return redirect('login')
    else:
        return render(request, 'login.html')
    
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('home')

# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             return redirect('login')  # Redirect to login after successful registration
#     else:
#         form = CustomUserCreationForm()

#     return render(request, 'templates/register.html', {'form': form})

# Logout View

# def logout_view(request):
#     logout(request)
#     messages.success(request, 'You have successfully logged out.')
#     return redirect('index')  # Redirect to the home page or login page


# hotels/views.py


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def index(request):
    return render(request, 'index.html')


def happyvally(request):
    return render(request, 'happyvally.html')

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, 'Registration successful! You are now logged in.')
#             return redirect('index')
#         else:
#             messages.error(request, 'Registration failed. Please try again.')
#     else:
#         form = UserCreationForm()
#     return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('index')
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)  # Log the user out
    return render(request, 'logout.html')  # Render the logout template


# def dashboard(request):
#     bookings = Booking.objects.filter(user=request.user)  # Assuming there's a related booking model
#     return render(request, 'dashboard.html', {'bookings': bookings})

def booking_form(request):
    if request.method == 'POST':
        # Handle the booking form submission (this depends on your form structure)
        # Save the booking information to the database
        pass  # Replace with your logic
    return render(request, 'booking_form.html')

# # hotels/views.py


# # def register(request):
# #     if request.method == 'POST':
# #         form = CustomUserCreationForm(request.POST)
# #         if form.is_valid():
# #             form.save()  # Save the new user
# #             return redirect('login')  # Make sure 'login' matches the name in urls.py
# #     else:
# #         form = CustomUserCreationForm()

# #     return render(request, 'register.html', {'form': form})

# # hotels/views.py


# def login_view(request):
#     form = AuthenticationForm()
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')  # Redirect to a home page or dashboard after login
#     return render(request, 'templates/login.html', {'form': form})

# # hotels/views.py
# from django.shortcuts import render, redirect
# from .forms import CustomUserCreationForm

# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()  # Save the new user
#             return redirect('login')  # Adjust this redirect to your login URL name
#     else:
#         form = CustomUserCreationForm()

#     return render(request, 'templates/register.html', {'form': form})




# hotels/views.py
# from django.shortcuts import render, redirect
# from .forms import CustomUserCreationForm

# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()  # Save the new user
#             return redirect('login')  # Redirect to a login page after registration
#     else:
#         form = CustomUserCreationForm()

#     return render(request, 'templates/register.html', {'form': form})


# hotels/views.py
from .forms import CustomUserCreationForm

# def register(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()  # Save the user to the database
#             return redirect('login')  # Redirect to a login URL after registration
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'register.html', {'form': form})


def facility(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user to the database
            return redirect('home')  # Redirect to a login URL after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'facility.html', {'form': form})


def amenity(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user to the database
            return redirect('home')  # Redirect to a login URL after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'amenity.html', {'form': form})


def loan(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user to the database
            return redirect('home')  # Redirect to a login URL after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'loan.html', {'form': form})

def payment_form(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user to the database
            return redirect('home')  # Redirect to a login URL after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'payment_form.html', {'form': form})

# def room_types(request):
#     roomtypes = Roomtype.objects.order_by('-room_type')
#     context = {"roomtypes" : roomtypes}
#     return render(request, 'room_types.html', context)


def paytutorials(request):
    paytutorials = paytutorials.objects.order_by('-checkInDate').filter(email=request.user.email)
    context = {"paytutorials" : paytutorials}
    return render(request, 'paytutorial.html',context)

from django.contrib import messages

# Create your views here.
# def payments(request):
#    if request.method == 'POST':
#        roomType = request.POST["roomType"]
        # if roomType == 'singleRoom':
        #     numberOfRooms = request.POST["singleRoomCount"]
        # elif roomType == 'doubleRoom': 
        #     numberOfRooms = request.POST["doubleRoomCount"]
        # elif roomType == 'twinRoom': 
        #     numberOfRooms = request.POST["twinRoomCount"]
        # elif roomType == 'kingRoom': 
        #     numberOfRooms = request.POST["kingRoomCount"]
        # fullName = request.POST["fullName"]
        # phoneNo = request.POST["phoneNo"]
        # email = request.POST["email"]
        # creditCardType = request.POST["creditCardType"]
        # creditCard = request.POST["creditCard"]
        # validThru = request.POST["validThru"]
        # CVC = request.POST["cvc"]
        # checkInDate = request.POST["checkIn"]
        # checkOutDate = request.POST["checkOut"]
        # numberOfTutor = request.POST['numberOfTutur']
        # numberOfRooms = request.POST['numberOfRooms']
        # totalPrice = request.POST["totalPrice"]
        # if checkInDate >= checkOutDate:
            # messages.error(request,"Check In Date and Check Out Date range invalid")
            # return redirect('payments')
#           # return render(request, 'payments.html')
        # has_paid = Payment.objects.all().filter(fullName=fullName,email=email,roomType=roomType,checkInDate=checkInDate,checkOutDate=checkOutDate)
        # if has_paid:
            # messages.error(request,"You have already made a payment")
#           # return redirect('payments')
            # return render(request, 'payments.html')
        # payment = Payment(roomType=roomType,fullName=fullName,phoneNo=phoneNo,email=email,creditCardType=creditCardType,creditCard=creditCard,validThru=validThru,CVC=CVC,checkInDate=checkInDate,checkOutDate=checkOutDate,totalPrice=totalPrice)
        # payment.save()
        #messages.success(request,"Your booking has been submitted and payment received")
#    render(request, 'home.html')return redirect('payments')
    # return r
    # else:
        # return render(request, 'payments.html')
        
def paytutorials(request):
    if request.method == 'POST':
        parentName = request.POST["parentName"]
        studentName = request.POST["studentName"]
        phoneNumber = request.POST["phoneNumber"] 
        tutorial = request.POST["tutorial"]
        bookingTime = request.POST["bookingTime"]
        paymentMethod = request.POST["paymentMethod"]
        fee = request.POST["fee"] 
        comTotalFee = request.POST["comTotalFee"] 
        conTotalFee = request.POST["conTotalFee"]
        chiTotalFee = request.POST["chiTotalFee"]
        matTotalFee = request.POST["matTotalFee"]
        assistantFamily = request.POST["assistantFamily"]
        return render(request, 'home.html')
        # return redirect('paytutorials')
        # return
    else: 
        return render(request, 'paytutorial.html')
    
    
def paytutorial_wh_new(request):
    if request.method == 'POST':
        parentName = request.POST["parentName"]
        studentName = request.POST["studentName"]
        phoneNumber = request.POST["phoneNumber"] 
        tutorial = request.POST["tutorial"]
        bookingTime = request.POST["bookingTime"]
        paymentMethod = request.POST["paymentMethod"]
        fee = request.POST["fee"] 
        comTotalFee = request.POST["comTotalFee"] 
        conTotalFee = request.POST["conTotalFee"]
        chiTotalFee = request.POST["chiTotalFee"]
        matTotalFee = request.POST["matTotalFee"]
        assistantFamily = request.POST["assistantFamily"]
        return render(request, 'home.html')
        # return redirect('paytutorials')
        # return
    else: 
        return render(request, 'paytutorial_wh_new.html')
        
    
def admin(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user to the database
            return redirect('home')  # Redirect to a login URL after registration
    else:
        form = CustomUserCreationForm()



def amenity_view(request):
    return render(request, 'amenity.html')

def amenity_view(request):
    selected_course = None
    if request.method == 'POST':
        selected_course = request.POST.get('course')
    return render(request, 'amenity.html', {'selected_course': selected_course})
