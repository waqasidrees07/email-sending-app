from django.shortcuts import HttpResponse, render
from django.core.mail import send_mail
from django.views.generic import View
from .forms import EmailSendForm
from .models import EmailSend
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


# Create your views here.


# def index(request):
#     send_mail(
#         'Subject here',
#         '''Great Its Works Nice''',
#         'waqasidrees15@gmail.com',
#         ['waqas84573@gmail.com'],
#         fail_silently=False,
#     )
#     return HttpResponse('<h1>Email Sended</h1>')


class EmailSendView(View):
    def get(self, request):
        form = EmailSendForm()
        return render(request, 'send/index.html', {'form': form})

    def post(self, request):
        form = EmailSendForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            reg = EmailSend(email=email, subject=subject, message=message)
            reg.save()
            html_message = render_to_string('send/email_template.html')
            plain_message = strip_tags(render_to_string('send/email_template.txt'))
            email = EmailMultiAlternatives(
                f'{subject}',
                f'{plain_message}',
                'waqasidrees15@gmail.com',
                [f'{email}'],
            )
            email.attach_alternative(html_message, "text/html")
            email.send()
            messages.success(request, "Email Send Successfully...")
        else:
            form = EmailSendForm()
            messages.error(request, 'Something went wrong!')
        return render(request, 'send/index.html', {'form': form})



# def send_email():
#     # Render the HTML and plain text templates
#     html_message = render_to_string('send/email_template.html')
#     plain_message = strip_tags(render_to_string('send/email_template.txt'))
#
#     # Create the email message
#     email = EmailMultiAlternatives(
#         'Subject line',
#         plain_message,
#         'waqasidrees15@gmail.com',
#         ['waqas84573@gmail.com'],
#     )
#
#     # Attach the HTML version
#     email.attach_alternative(html_message, "text/html")
#
#     # Send the email
#     email.send()
