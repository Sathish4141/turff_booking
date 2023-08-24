from django.urls import path
from .views import *


urlpatterns = [
    path('',run,name='run'),
    path('signup/',signup,name='signup'),
    path('login/',action_login,name='login'),
    path('logout/',action_logout,name='logout'),
    path('turff_list/',turff_list, name='turff_list'),
    path('owner_turff_list/',owner_turff_list, name='owner_turff_list'),
    path('owner_signup/',owner_signup,name='owner_signup'),
    path('add_turff/',turffdetails_form,name='turffdetails'),
    path('turff_in_detail/<int:id>',turff_in_detail,name='turff_in_detail'),
    path('booking/<int:id>', booking, name="booking"),
    path('confirm/<int:id>', confirm, name="confirm"),
    path('about/',about , name="about"),
    path('mybook/',mybook , name="mybook"),
    path('success/',booking_success , name="success"),
    path('tdelete/<int:id>',tdelete , name="tdelete"),
    path('ownerbook/',ownerbook , name="ownerbook"),
    path('turffdelete/<int:id>',turffdelete , name="turffdelete"),
    

]