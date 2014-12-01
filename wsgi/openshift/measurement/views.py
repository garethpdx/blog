from django.shortcuts import render_to_response
from django.template import RequestContext

from measurement.models import MeasurementForm, User, Measurement, Category

def measure(request, username):
    if request.method == 'POST':
        f = MeasurementForm(request.POST)
        if f.is_valid():
            new_measurement = f.save(commit=False)
            user = User.objects.filter(username=username)[0]
            new_measurement.user = user
            new_measurement.save()
    form = MeasurementForm()
    user = User.objects.filter(username=username)[0]
    default_category = get_default_category(user)
    return render_to_response('home/measurement/measure.html',
                              {'form': form.as_p(),
                               'measure_user': user,
                               'default_category': default_category},
                              context_instance=RequestContext(request))


def retrieve_last_measurement_for_user(user):
    return Measurement.objects.filter(user=user)[0]


def retrieve_any_global_category():
    return Category.objects.all()[0]


def get_default_category(user):
    category = None
    try:
        category = retrieve_last_measurement_for_user(user).type
    except IndexError:
        pass
    if not category:
        category = retrieve_any_global_category()
    return category
