from django.contrib import admin
from django.urls import path,include
from app import views
urlpatterns = [
   
    path('',views.ThankYouView.as_view(),name='tq_view'),
    path('list',views.review_list_View.as_view(),name='rev_list'),
    path('single_item/<int:pk>',views.SingleReviewView.as_view(),name='sing_item'),
    path('form/',views.form_view.as_view(),name='form_view'),
    path('form_with_form_view/',views.Form_View.as_view(),name='form_view_with_FormView'),
    path('create_view/',views.create_view.as_view(),name='create_view'),

]
