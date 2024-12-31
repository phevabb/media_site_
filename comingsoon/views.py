from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, EmailMessage
import smtplib


# Create your views here.


def home(request):
    try:
        if request.method == "POST":
            message_name = request.POST["name"].strip()
            message_email = request.POST["email"].strip().lower()
            message_sub = request.POST["subject"]
            message = request.POST["message"]

            email_message = f'Message received from Name :{message_name}, Email: {message_email}\n\n{message}'

            subject = message_sub
            message = email_message
            from_email = message_name + "<bryteredunuakoh@gmail.com>"  # Sender's email address
            recipient_list = ['bright.wiredu@aims.ac.rw']  # List of recipient email addresses

            send_mail(subject, message, from_email, recipient_list)

            subject_user = f'We received your message {message_name}'
            message_user = 'We received your enquiry! Our team will get back to you as soon as possible.'
            from_email_user = "Bright Nuakoh Wiredu <bryteredunuakoh@gmail.com>"  # Sender's email address
            send_mail(subject_user, message_user, from_email_user, [message_email])
            context = {
                'success': [f'Your Message has been sent successfully, {message_name}'],

            }

            return render(request, "index2.html", context)

        else:
            return render(request, "index2.html")

    except smtplib.SMTPRecipientsRefused:
        context = {
            "errors": ['Invalid Email!'],
        }
        return render(request, "index2.html", context)


def index(request):
    return render(request, "index2.html")


def news_let(request):
    try:
        if request.method == "POST":
            context = {
                'success': True
            }
            message_email = request.POST["email"].strip().lower()  # Sender's email address

            name = message_email.strip('@')[0]

            subject = "News Letter"
            recipient_list = ['info@medirevs.com']  # List of recipient email addresses

            send_mail(subject, message_email, recipient_list)

            subject_user = f'Hello {name}! Welcome To our Newsletter'
            message_user = """We’re thrilled to share the latest news, breakthroughs, and updates from our journey to revolutionize the healthcare system. From cutting-edge innovations to inspiring stories of change, we’re dedicated to keeping you informed and inspired.\n\n 

                            Stay tuned for exclusive insights, upcoming events, and opportunities to engage with our transformative products and initiatives. Together, we can make a significant impact on the future of healthcare.

                            Thank you for being a valued part of our community!

                            Warm regards,
                            Bright Wiredu
                            MEDIREV Org."""
            from_email_user = "MEDIREV <info@medirevs.com>"  # Sender's email address
            send_mail(subject_user, message_user, from_email_user, [message_email])

            return render(request, "index2.html", context)

        else:
            context = {
                "errors": ['Invalid Email!'],
            }
            return render(request, "index2.html", context)

    except smtplib.SMTPRecipientsRefused:
        context = {
            "errors": ['Invalid Email!'],
        }
        return render(request, "index2.html", context)
