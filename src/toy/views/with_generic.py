
from typing import List
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from toy.models import *
from django.http import HttpResponseRedirect,  HttpResponseNotFound
from django.urls import reverse
 
 
class Salvar_Pessoa(CreateView):
    model = Person
    template_name = "list_person.html"
    fields = ['name', 'birth_date']
    template_name = "salvar_tesouro.html"
    success_url = reverse_lazy('listar_pessoas')
     
class Listar_pessoas(ListView):
    model = Person
    template_name = "list_person.html"
    def get_context_data(self):
        context = {'lista_pessoas':Person.objects.all()}
        return context
        
class Pag_principal(Listar_pessoas, Salvar_Pessoa):
    pass
  

class Atualizar_Pessoa(Salvar_Pessoa, UpdateView):
    pass
class Atualizar_Olho(UpdateView):
    model = Person
    fields = ['eye_color']
    template_name = "person_eye_update.html"
    success_url = reverse_lazy('listar_pessoas')
