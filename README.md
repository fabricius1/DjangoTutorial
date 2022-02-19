<h1 style="text-align: center">DJANGO QUICK TUTORIAL COMPANION CODE</h1>

<br />
<p style="float: right;">Author: <a href="https://linktr.ee/fabriciobarbacena">Fabrício Barbacena</a></p>
<br />
<br />

## Project Description
<br />

This repository has the final version of the code I developed in my article/tutorial *[Django First Steps for Total Beginners: A Quick Tutorial](https://medium.com/towards-data-science/django-first-steps-for-the-total-beginners-a-quick-tutorial-5f1e5e7e9a8c)*, published on [Towards Data Science](https://medium.com/towards-data-science). 

The code intermediary versions are not presented here, but one can find them all in the aforementioned article, with detailed descriptions about them.

I'm putting together this present repository so that it can be used as starter code for future projects of mine. Here people will also find the route where I embed a Plotly chart on a Django page, which can be of interest for some folks out there.

<br />

## How to Install the Project
<br />

1. You need to have Python installed in your machine (3.8 or higher is recommended);

2. Create a new folder in your machine, go inside it and clone this repository. 

3. Create a virtual environment with `venv`. I called mine `.myenv`, but you can choose another name you prefer:

<span style="margin-left: 25px;">```python -m venv .myenv```</span> 

4. Activate the virtual environment. Below is the command for most Linux OS:

<span style="margin-left: 25px;">```source .myenv/bin/activate```</span>

<span style="margin-left: 25px;">Check this [Python documentation page](https://docs.python.org/3/library/venv.html) if you have doubts about the command to start your virtual environment.</span>

5. Install the required Python modules (Django, Pandas, and Plotly):

<span style="margin-left: 25px;">```pip install -r requirements.txt```</span>

<br />

## How to Use the Project
<br />

1. Run `python manage.py makemigrations` and `python manage.py migrate` to create the necessary tables in the database;

2. Start the command with `python manage.py runserver`. 8000 is the default port used by Dango;

3. On your browser, access the address http://localhost:8000;

4. Use the Links to navigate by the films pages;

5. Access http://localhost:8000/gapminder/2007 to see the most recent version of the Gapminder interactive Plotly chart.

> You can change the year in the last url to one of the available years in the Gapminder dataset from Plotly Express (1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, and 2007). Choosing a route with any other year will raise an error.

<br />

## Licence
<br />

This project is distributed under the MIT licence (see the LICENCE document).