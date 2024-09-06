from django.urls import path
from .import views


urlpatterns = [
    path('show/',views.product_list,name='product'),
    path('bill/',views.bill,name='bill'),
    path('index/',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('menu/',views.menu,name='menu'),
    path('service/',views.service,name='service'),
    path('team/',views.team,name='team'),
    path('testimonial/',views.testimonial,name='testimony'),


    path('',views.home,name='home'),
	path('accounts/login/',views.loginview,name="login"),
	path('logout',views.logout_view),
	path('accounts/sign_up/',views.sign_up,name="signup") ,
	path('reset',views.Resethome,name='reset'), 
	path('passwordreset',views.resetPassword,name="passwordreset")
   
    
]


