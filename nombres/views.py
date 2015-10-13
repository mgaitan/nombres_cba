from django.shortcuts import render
from nombres.forms import SearchForm, CHOICES
from nombres.models import Padron
from django.views.decorators.csrf import csrf_exempt
import unicodedata
import matplotlib
matplotlib.rcParams['lines.linewidth'] = 2
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.ioff()
import pandas as pd
import mpld3


@csrf_exempt
def normalizar(cadena):
    try:
        normal = unicodedata.normalize('NFKD', cadena)
    except TypeError:
        cadena = cadena.decode('iso-8859-1')
        normal = unicodedata.normalize('NFKD', cadena)
    only_ascii = normal.encode('ASCII', 'ignore').decode('utf8')
    return only_ascii.title()


def nombres(request):
    form = SearchForm(data=request.GET if request.GET else None)
    fig = None
    options = None
    tipo = 'count'
    if form.is_valid():

        fig = plt.figure()
        option = form.cleaned_data['options']
        tipo = form.cleaned_data['tipo']
        terms = [normalizar(t.strip()) for t in form.cleaned_data['terms'].split(',')]
        for term in terms:
            data = Padron.objects.filter(**{option: term}).values('clase', 'apellido', 'primer_nombre', 'segundo_nombre')
            qs = pd.DataFrame.from_records(data)
            try:
                count = qs.groupby('clase')[option].count()
                if tipo == 'cumsum':
                    count = count.cumsum()
                count.plot(label=term)
            except (TypeError, KeyError):
                # no data to plot
                plt.plot(0, label=term)
        plt.legend(loc='best')
        fig = mpld3.fig_to_html(fig)
        options = (form.cleaned_data['options'], dict(CHOICES)[option])

    return render(request, 'nombres.html', {'form': form, 'fig': fig,
                                            'options': options, 'tipo': tipo})

