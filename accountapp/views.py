from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.functional import lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountCreationForm
from accountapp.models import HelloWorld


def introduce(request):
    if request.method == 'POST':

        temp = request.POST.get('introduce_input')

        new_introduce = HelloWorld()
        new_introduce.text = temp
        new_introduce.save()

        return HttpResponseRedirect(reverse('accountapp:introduce'))
    else:
        introduce_list = HelloWorld.objects.all()
        return render(request, 'accountapp/introduce.html',
                      context={'introduce_list': introduce_list})



class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url =reverse_lazy('accountapp:introduce')
    template_name ='accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name ='target_user'
    template_name = 'accountapp/detail.html'

class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:introduce')
    template_name = 'accountapp/update.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.get_object() == request.user:
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.get_object() == request.user:
            return super().post(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:introduce')
    template_name = 'accountapp/delete.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.get_object() == request.user:
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.get_object() == request.user:
            return super().post(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
