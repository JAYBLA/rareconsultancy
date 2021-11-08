from django.shortcuts import render, get_object_or_404, redirect, reverse
from.models import Contact
from .forms import ContactForm
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import JsonResponse

def home(request):
    template_name = 'main/home.html'
    context = {
        'title':"We move your business forward with the best solutions!."    
        
    }    
    return render(request, template_name, context)

def contact(request):
    template_name = 'main/contact.html'
    form = ContactForm()
    context = {
        'title':"Contacts",
        'form':form,
    }    
    return render(request, template_name, context)


def process_contact(request):
    if request.is_ajax():
        if request.method == 'POST':
            full_name = request.POST['full_name'],
            email = request.POST['email'],
            phone = request.POST['phone'],            
            message = request.POST['message']
            
            contact = Contact(
                full_name=full_name,
                email=email,
                phone=phone,
                message=message
                
            )
            contact.save()
            subject = 'Jaybla Group Contact Form'
            html_message = render_to_string('main/mail_template.html', {
                'full_name':full_name,
                'email':email,
                'phone':phone,
                'message':message                
            })
            plain_message = strip_tags(html_message)
            recipient_list = ['jayblaenterprises@gmail.com','jayblagroup@gmail.com',]
            from_email = "info@jaybla.com"
            mail.send_mail(subject,plain_message, from_email, recipient_list, html_message=html_message,fail_silently=False,)

            return JsonResponse({'msg': 'success'}, safe=False)
        else:
            return JsonResponse({'msg': 'error'})
