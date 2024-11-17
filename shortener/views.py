# shortener/views.py
from django.shortcuts import render
from .forms import URLForm
from .models import URL
import random
import string

# Function to generate a shortened URL
def generate_shortened_url(original_url):
    # Generate a random shortened URL (6 characters long)
    short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

    # Save the original URL and its shortened version in the database
    URL.objects.create(original=original_url, shortened=short_url)
    return short_url

# Home view for displaying the form and generating shortened URL
def home(request):
    form = URLForm()
    shortened_url = None  # Initialize shortened_url to None

    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            shortened_url = generate_shortened_url(original_url)  # Generate shortened URL
        else:
            print("Form is not valid: ", form.errors)  # Debugging form errors

    return render(request, 'shortener/home.html', {'form': form, 'shortened_url': shortened_url})


# shortener/views.py
from django.shortcuts import redirect
from .models import URL

def redirect_to_original(request, short_url):
    try:
        url_entry = URL.objects.get(shortened=short_url)
        return redirect(url_entry.original)  # Redirect to the original URL
    except URL.DoesNotExist:
        return redirect('home')  # If the shortened URL does not exist, redirect to the home page
