from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect
from .models import Product, Feature, Section, Image, Page
from .forms import ContactForm
from wmtech import settings


# Create your views here.

def home(request):
    products = Product.objects.all()
    page = Page.objects.get(page='home')
    features = Feature.objects.all()
    feature_section = Section.objects.get(section='features')
    contact_section = Section.objects.get(section='contact')
    project_section = Section.objects.get(section='projects')
    about_section = Section.objects.get(section='about')
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject, from_email, to = 'Kontaktformular Webseite', settings.EMAIL_HOST_USER, settings.EMAIL_HOST_USER
            html_content = render_to_string('email.html', {'prename': cd['prename'], 'name': cd['name'], 'email':cd['email'], 'message':cd['message']})
            text_content = render_to_string('email.txt', {'prename': cd['prename'], 'name': cd['name'], 'email':cd['email'], 'message':cd['message']})
                
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return HttpResponseRedirect('?submitted=True#contact')

    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'home.html', {'products': products, 'features': features, 'form': form, 'feature_section': feature_section, 'contact_section': contact_section, 'project_section': project_section,'about_section': about_section, 'page': page, 'submitted': submitted})

def single_product(request, pk):
    product = Product.objects.get(pk=pk)
    images = product.get_images()
    return render(request, 'single-project.html', {'product': product, 'images': images})


def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/admin/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            auth_login(request, user)
            return HttpResponseRedirect('/admin/')
        else:
            return HttpResponseRedirect('login/')
    return render(request, 'login.html')


def gallery(request):
    images = Image.objects.all()
    return render(request, 'gallery.html', {'images': images})

def impressum(request):
    page = Page.objects.get(page='impressum')
    return render(request, 'legal.html', {'page': page})

def privacy_policy(request):
    page = Page.objects.get(page='legal')
    return render(request, 'legal.html', {'page': page})