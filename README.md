# weather-checker
  Show weather information for user selected city through API and HTML pages

# Prerequisite
  Python 3.7
  
  SQLite installed https://www.sqlite.org/index.html

# Make it work (Locally)
   Create a file inside weather_checker called `local_settings.py` and add `ALLOWED_HOSTS = ['*']` and Your database configurations

  `pip install -r requirements.txt`
  
  `python manage.py migrate`
  
  `python manage.py runserver`
 
 # Live App
 This app is deployed on Heroku
 
 Visit `https://weather-checker-ash.herokuapp.com`
 
 
# API Documentation
  You can find all Endpoints here: `https://weather-checker-ash.herokuapp.com/api/v1/docs`
  
  `api/v1/login`
  
  `api/v1/register`
  
  `api/v1/weather` > *You must login to use this endpoint*

