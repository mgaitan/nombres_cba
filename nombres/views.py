import os
from django.shortcuts import render
from nombres.forms import SearchForm, CHOICES
import unicodedata
import matplotlib
matplotlib.rcParams['lines.linewidth'] = 2
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.ioff()
import numpy as np
import pandas as pd
import mpld3

here = os.path.dirname(os.path.realpath(__file__))


def normalizar(cadena):
    try:
        normal = unicodedata.normalize('NFKD', cadena)
    except TypeError:
        cadena = cadena.decode('iso-8859-1')
        normal = unicodedata.normalize('NFKD', cadena)
    only_ascii = normal.encode('ASCII', 'ignore').decode('utf8')
    return only_ascii.upper()


def nombres(request):
    form = SearchForm(data=request.POST if request.method=='POST' else None)
    fig = None
    options = None
    if form.is_valid():
        data = pd.read_pickle(os.path.join(here, 'padron_cba.pickle'))
        fig = plt.figure()
        option = form.cleaned_data['options']

        terms = [normalizar(t.strip()) for t in form.cleaned_data['terms'].split(',')]
        for term in terms:
            if option != 'apellido':
                term = term.title()
            qs = data[(data[option] == term)]
            try:
                qs.groupby('clase')[option].count().plot(label=term.title())
            except TypeError:
                # no data to plot
                plt.plot(0, label=term.title())
        plt.legend(loc='best')
        fig = mpld3.fig_to_html(fig)
        options = (form.cleaned_data['options'], dict(CHOICES)[option])

    return render(request, 'nombres.html', {'form': form, 'fig': fig, 'options': options})

