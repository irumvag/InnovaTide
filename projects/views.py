from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext as _

def project_list(request):
    projects = [
        {
            'id': 1,
            'title': _("Radioisotope Production Facility"),
            'image': 'projects/isotope-facility.jpg',
            'summary': _("Designing sustainable radioisotope production for medical use"),
            'sector': _("Medical"),
            'year': 2022
        },
        # Add more projects...
    ]
    return render(request, 'projects/list.html', {'projects': projects})

def project_detail(request, project_id):
    project = get_object_or_404({
        1: {
            'title': _("Radioisotope Production Facility"),
            'image': 'projects/isotope-facility-detail.jpg',
            'content': _("Detailed case study about isotope production..."),
            'partners': [_("IAEA"), _("WHO")],
            'results': [_("30% cost reduction"), _("Increased production capacity")]
        }
        # Add more projects...
    }, key=project_id)
    
    return render(request, 'projects/detail.html', {'project': project})