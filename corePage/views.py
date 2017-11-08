from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class home(TemplateView):
    template_name = 'personal/home.html'
class aboutMe(TemplateView):
    template_name = "personal/_about-me.html"
class mySkills(TemplateView):
    template_name = "personal/_my-skills.html"
class myHobbies(TemplateView):
    template_name = "personal/_my-hobbies.html"
