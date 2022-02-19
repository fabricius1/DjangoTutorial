from audioop import reverse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Film
import plotly.express as px


def get_data():
    df = px.data.gapminder()
    return df


def create_plot(df, year):
    fig = px.scatter(
        data_frame = df.query(f'year=={year}'),
        x = 'gdpPercap',
        y = 'lifeExp',
        color = 'continent',
        size = 'pop',
        height = 500,
        log_x=True,
        size_max=60,
        hover_name="country")
    fig =  fig.to_html()
    return fig


def home(request):
    return render(request, 'home.html')


def main(request):
    title = 'Main Page'
    films_list = Film.objects.all()
    context = {'title': title,
               'films_list': films_list}
    return render(request, 'films/main.html', context)


def user_info(request):
    if request.method == 'GET':    
        print('\n\nrequest.GET ==>>',
              request.GET,
              '\n\n')
    
        if request.session.get('username', False):
            userinfo = {
                'username': request.session['username'],
                'country': request.session['country'],
            }
        else:
            userinfo = False
            
        context = {'userinfo': userinfo,
                   'title': 'User Info Page'}
        template = 'films/user_info.html'
        return render(request,
                      template,
                      context)
    

def user_form(request):
    if request.method == 'GET':
        context = {'title': 'User Form Page'}
        template = 'films/user_form.html'

        return render(request,
                      template,
                      context)
        
    elif request.method == 'POST':
        username = request.POST.get('username')
        country = request.POST.get('country')
        request.session['username'] = username
        request.session['country'] = country

        return redirect(reverse('films:user_info'))


def details(request, id):
    film = Film.objects.get(id=id)
    # other query option:
    # film = Film.objects.filter(id=id)[0]
    context = {'film': film}
    return render(request, 'films/details.html', context)


def gapminder(request, year):
    df = get_data()
    fig = create_plot(df, year)
    context = {"plot": fig, "year": year}
    template = 'gapminder.html'
    return render(request, template, context)
