from django.shortcuts import render, redirect
from .models import Artiles
from .forms import ArtilesForm
from django.views.generic import DetailView, UpdateView, DeleteView

# Функции для работы с базой данных
def news_home(request):
    skills = Artiles.objects.all()
    return render(request, "app2/news_home.html", {'skills': skills})

class NewsDetailView(DetailView):
    model = Artiles
    template_name = 'app2/details_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Artiles
    template_name = 'app2/create.html'
    fields = ['skill', 'opisanie', 'full_text']

class NewsDeleteView(DeleteView):
    model = Artiles
    success_url = '/news'
    template_name = 'app2/news_delete.html'

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArtilesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма была неверной'

    form = ArtilesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, "app2/create.html", data)