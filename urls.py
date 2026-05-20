# hotels/urls.py
from django.urls import path
from . import views
from .views import (
    register,
    login_view,
    logout_view,
    booking_form,
    about,
    home,
    facility,
    amenity,
    loan,
    payment_form,
    paytutorials,
    paytutorial_wh_new,
    admin,
    login,
    logout,
    amenity_view,
    index,
    
)
from .views import happyvally

urlpatterns = [
    path('', home, name='home'),  # Home page
    path('about/', about, name='about'),  # About page
    path('admin/', admin, name='admin'),
    path('register/', register, name='register'),  # Registration page
    path('login/', login_view, name='login'),  # Login page
    path('logout/', logout_view, name='logout'),  # Logout page
    path('booking_form/', booking_form, name='booking_form'),  # Booking form page
    path('facility/', facility, name='facility'),  # Facility page
    path('amenity/', amenity, name='amenity'),  # Amenity page
    path('loan/', loan, name='loan'),  # Loam Item page
    path('payment_form/', payment_form, name='payment_form'),  # Payment form page
    path('api/loan/', loan, name='loan'),  # Loan API endpoint
    path('amenity/path_to_previous_page/', loan, name='path_to_previous_page'),  # Path to previous form page
    path('paytutorials/', paytutorials, name='paytutorials'),  # Payment tutorials page
    path('paytutorial_wh_new/', paytutorial_wh_new, name='paytutorial_wh_new'),  # New payment tutorial page
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('logout/', logout, name='logout'),
    path('happyvally/', views.happyvally, name='happyvally'),
    path('amenity/', amenity_view, name='amenity'),
    path('index/', views.index, name='index'),
]

from django.contrib import admin
admin.autodiscover()


