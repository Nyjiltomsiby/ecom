from .models import Category

def my_link(request):
    links=Category.objects.all()
    return dict(links=links)
