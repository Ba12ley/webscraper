from django.views.generic import ListView
from .models import DefibLocationNI

class DefibLocationView(ListView):
    model = DefibLocationNI
    template_name = 'pages/defib_loc.html'
    context_object_name = 'defib_locaction'
