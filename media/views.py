from django.shortcuts import render
from django.utils.translation import gettext as _

def media_list(request):
    articles = [
        {
            'title': _("InnovaTide Wins Innovation Award"),
            'date': "2023-05-15",
            'source': _("Nuclear News Journal"),
            'excerpt': _("Recognized for breakthrough in agricultural applications...")
        },
        # Add more articles...
    ]
    return render(request, 'media/list.html', {'articles': articles})