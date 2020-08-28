from django.http import JsonResponse
from django.views.generic import ListView
from django.views.generic.base import View

from core.models import Passenger


class PassengerListView(ListView):
    """ Passenger view logic
    """
    model = Passenger

    def get_queryset(self):
        qs = Passenger.objects.filter(age__gte=18, survived=True).order_by('age')[:10]
        return qs


class PassengerView(View):
    """ Returns passenger model json
    """
    def get(self, request):
        result = []
        passengers = Passenger.objects.all()
        for passenger in passengers:
            result.append({
                'id': passenger.id,
                'survived': passenger.survived,
                'pclass': passenger.pclass,
                'name': passenger.name,
                'sex': passenger.sex,
                'age': passenger.age,
                'sib_sp': passenger.sib_sp,
                'parch': passenger.parch,
                'ticket': passenger.ticket,
                'fare': passenger.fare,
                'cabin': passenger.cabin,
                'embarked': passenger.embarked
            })
        return JsonResponse(result, safe=False)
