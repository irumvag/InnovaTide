from django.shortcuts import render
from django.contrib import messages
from django.utils.translation import gettext as _

def home(request):
    context = {
        'featured_projects': [],  # Add actual projects here
        'did_you_know_facts': [
            _("Nuclear technology is used in medicine for diagnostics and treatment."),
            _("Agriculture benefits from nuclear techniques in pest control and food preservation."),
            _("Industrial applications include material testing and sterilization."),
        ]
    }
    return render(request, 'home/home.html', context)

from django.core.paginator import Paginator

def search(request):
    query = request.GET.get('q', '')
    results = perform_search(query)  # Your search logic
    
    paginator = Paginator(results, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'home/search.html', {
        'results': page_obj,
        'query': query,
        'is_paginated': page_obj.has_other_pages(),
        'page_obj': page_obj
    })
def contact(request):
    if request.method == 'POST':
        # Handle form submission
        messages.success(request, _("Thank you for your message!"))
        return redirect('contact')
    
    return render(request, 'home/contact.html')
def privacy(request):
    return render(request, 'home/privacy.html', {
        'privacy_policy': _("Your privacy is important to us. We do not share your data with third parties without consent.")
    })
