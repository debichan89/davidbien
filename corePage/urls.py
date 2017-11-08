from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.home.as_view(),name='home'),
    url(r'^aboutme$',views.aboutMe.as_view(),name='aboutme'),
    url(r'^myskills$',views.mySkills.as_view(),name='myskills'),
    url(r'^myhobbies$',views.myHobbies.as_view(),name='myhobbies'),
]
