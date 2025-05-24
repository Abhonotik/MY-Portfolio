from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
import re

def home(request):
    return render(request, 'home.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message_content = request.POST.get('message', '').strip()
        number = request.POST.get('number', '').strip()

        # Simple validation
        errors = False

        if not (1 <= len(name) <= 30):
            messages.error(request, "Please enter a valid name (1-30 characters).")
            errors = True

        email_regex = r"[^@]+@[^@]+\.[^@]+"
        if not re.match(email_regex, email):
            messages.error(request, "Please enter a valid email address.")
            errors = True

        if not (message_content and len(message_content) >= 10):
            messages.error(request, "Message should be at least 10 characters long.")
            errors = True

        if not (number.isdigit() and len(number) == 10):
            messages.error(request, "Please enter a valid 10-digit phone number.")
            errors = True

        if errors:
            return render(request, 'contact.html', {
                'name': name,
                'email': email,
                'message': message_content,
                'number': number,
            })

        # Process the data (e.g., save to database or send email)
        print(f"Contact submission: {name}, {email}, {message_content}, {number}")
        messages.success(request, "Your message has been successfully submitted!")
        return redirect('contact')  # Avoid form resubmission on refresh

    return render(request, 'contact.html')

        