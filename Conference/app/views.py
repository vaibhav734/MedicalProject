from django.shortcuts import render
from django.views.generic import *
from app.models import Session
from django.core.urlresolvers import reverse_lazy
from app.forms import SessionForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def index(request):
    return render(request,'index.html')

class SessionList(ListView):
    model = Session

class SessionDetail(DetailView):
    model = Session

class SessionCreate(LoginRequiredMixin, CreateView):
    model = Session
    form_class = SessionForm

class SessionUpdate(LoginRequiredMixin, UpdateView):
    model = Session
    form_class = SessionForm

class SessionDelete(LoginRequiredMixin, DeleteView):
    model = Session
    success_url = reverse_lazy('sessions_list')