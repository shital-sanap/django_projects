from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from cats.models import Breed, Cat

# Create your views here.
class CatList(LoginRequiredMixin, View):
    def get(self,request):
        cl = Cat.objects.all()
        bc = Breed.objects.all().count()
        return render(request, 'cats/cat_list.html', {'cat_list':cl, 'breed_count':bc})

class BreedList(LoginRequiredMixin, View):
    def get(self, request):
        bl = Breed.objects.all()
        return render(request, 'cats/breed_list.html', {'breed_list':bl})

class BreedCreate(LoginRequiredMixin,CreateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

