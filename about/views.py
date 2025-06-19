from django.shortcuts import render
from django.utils.translation import gettext as _

def about(request):
    context = {
        'mission': _("Advancing non-energy applications of nuclear technology for sustainable development"),
        'team_members': [
            {
                'name': _("Dr. Sarah Chen"),
                'position': _("Nuclear Applications Specialist"),
                'bio': _("15 years experience in medical isotope research"),
                'image': 'team/sarah-chen.jpg'
            },
            {
                'name': _("Dr. Michael Rodriguez"),
                'position': _("Industrial Applications Lead"),
                'bio': _("Pioneer in nuclear gauging technologies"),
                'image': 'team/michael-rodriguez.jpg'
            },
            {
                'name': _("Priya Patel"),
                'position': _("Agricultural Solutions"),
                'bio': _("Developing mutation breeding techniques"),
                'image': 'team/priya-patel.jpg'
            }
        ],
        'milestones': [
            {'year': "2018", 'event': _("Founded with IAEA partnership")},
            {'year': "2020", 'event': _("First industrial applications deployed")},
            {'year': "2022", 'event': _("Expanded to 15 countries")},
            {'year': "2023", 'event': _("Received UN Sustainable Development Award")}
        ]
    }
    return render(request, 'about/about.html', context)