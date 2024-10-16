from django.shortcuts import render
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect
from .models import Product, Feature, Section
from .forms import ContactForm
from wmtech import settings

# Create your views here.

def home(request):
    products = Product.objects.all()
    features = Feature.objects.all()
    feature_section = Section.objects.get(section='features')
    contact_section = Section.objects.get(section='contact')
    project_section = Section.objects.get(section='projects')
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            subject, from_email, to = 'Kontaktformular Hexacoding', settings.EMAIL_HOST_USER, 'contact@hexacoding.ch'
            html_content = render_to_string('email.html', {'salutation':cd['salutation'], 'prename': cd['prename'], 'name': cd['name'], 'email':cd['email'], 'message':cd['message']})
            text_content = render_to_string('email.txt', {'salutation':cd['salutation'], 'prename': cd['prename'], 'name': cd['name'], 'email':cd['email'], 'message':cd['message']})
                
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return HttpResponseRedirect('?submitted=True#contact')

    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'home.html', {'products': products, 'features': features, 'form': form, 'feature_section': feature_section, 'contact_section': contact_section, 'project_section': project_section,'submitted': submitted})

def single_product(request, pk):
    product = Product.objects.get(pk=pk)
    images = product.get_images()
    return render(request, 'single-project.html', {'product': product, 'images': images})