from django.urls import path

from . import views

urlpatterns = [
	path('',views.home,name="home"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('donation',views.donation,name="donation"),
	path('process-payment/', views.process_payment, name='process_payment'),
    path('payment-done/', views.payment_done, name='payment_done'),
    path('payment-cancelled/', views.payment_cancelled, name='payment_cancelled'),
    path('persons-list',views.persons_list,name='persons_list'),

]