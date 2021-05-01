from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.shortcuts import render

class ProfileView(TemplateView):
    template_name = 'profile.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)