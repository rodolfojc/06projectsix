from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
# Create your views here.

from . models import Article

class ArticleListView(ListView):
    model = Article
    template_name = 'home.html'

class ArticleDetailsView(DetailView):
    model = Article
    template_name = 'detail.html'
    context_object_name = 'batman'

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = '__all__'

    
