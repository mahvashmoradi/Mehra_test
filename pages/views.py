from django.http import JsonResponse
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

# Create your views here.
from django.views import View

from pages.models import Post, Product
from .forms import ContactForm


class HomeView(View):
    def get(self, request):
        post = Post.objects.all()
        product = Product.objects.all()
        return render(request, 'pages/home.html', {'post': post, 'product': product})


class ContactView(View):
    def get(self, request, *args, **kwargs):
        form = ContactForm()  # MODEL FORM
        return render(request, 'pages/contact_us.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Your message is send")
            return redirect(reverse('contact'))
        else:
            return JsonResponse(form.errors)
