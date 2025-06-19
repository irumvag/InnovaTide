from django.shortcuts import render
from django.utils.translation import gettext as _

from django.shortcuts import render
from django.utils.translation import gettext as _

def category_detail(request, category):
    """Handle dynamic category pages"""
    data = {
        'medical': {
            'title': _("Medical Applications"),
            'description': _("Nuclear technologies in healthcare and medicine"),
            'applications': [
                {
                    'title': _("Cancer Therapy"),
                    'image': 'applications/medical-1.jpg',
                    'description': _("Radioisotopes for targeted cancer treatment"),
                    'stats': _("Used in 85% of radiotherapy procedures")
                },
                # Add more medical applications...
            ]
        },
        'agriculture': {
            'title': _("Agricultural Applications"),
            'description': _("Nuclear solutions for food security"),
            'applications': [
                {
                    'title': _("Mutation Breeding"),
                    'image': 'applications/agri-1.jpg',
                    'description': _("Developing improved crop varieties"),
                    'stats': _("Used in 100+ crop species worldwide")
                },
                # Add more agriculture applications...
            ]
        },
        'industrial': {
            'title': _("Industrial Applications"),
            'description': _("Nuclear techniques in manufacturing"),
            'applications': [
                {
                    'title': _("Material Testing"),
                    'image': 'applications/industrial-1.jpg',
                    'description': _("Non-destructive testing of materials"),
                    'stats': _("Used in aerospace and automotive industries")
                },
                # Add more industrial applications...
            ]
        }
    }
    
    if category not in data:
        # Handle unknown categories
        return render(request, 'applications/404.html', status=404)
    
    context = {
        'category': data[category],
        'related_categories': [cat for cat in ['medical', 'agriculture', 'industrial'] if cat != category]
    }
    return render(request, 'applications/category.html', context)

# Individual category views (optional but cleaner URLs)
def medical(request):
    return category_detail(request, 'medical')

def agriculture(request):
    return category_detail(request, 'agriculture')

def industrial(request):
    return category_detail(request, 'industrial')