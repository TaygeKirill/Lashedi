from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm




def index(request):
    return render(request, 'blog/index.html')


def about(request):
    return render(request, 'blog/about.html')


def contact(request):
    return render(request, 'blog/contact.html')


def jobs(request):
    return render(request, 'blog/jobs.html')


def calendar(request):
    form = BlogForm()
    context = {'form': form}
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('calendar')
    return render(request, 'blog/calendar.html', context)


def price(request):
    return render(request, 'blog/price.html')

