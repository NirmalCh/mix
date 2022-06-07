
from django.urls import path
from sahakari_app import views
urlpatterns = [
    path('', views.home, name='home' ),
    path('account/', views.account, name='account'),
    path('register/', views.register , name='register'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('general/', views.general_profile, name='general'),
    path('general-edit/', views.general_edit, name='general_edit'),
    path('privacy/', views.privacy, name='privacy'),
    path('personal-account/', views.personal_account, name='personal_account'),
    path('account_info/',views.Account_InfoList.as_view()),
]
