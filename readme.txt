#Clone the project

#Install all the packages
sudo pip -r packages

#Change the settings
    ##DB Settings
        By default uses the sqlite, change it what you like in settings.py
    ##SMTP settings  
        Change the values in settings.py
    

#Synchronize DB
python manage.py syncdb

#Run    
python manage.py runserver


#Admin login
http://localhost:8080/admin

#For others 
http://localhost:8080/

#Create new client for oauth
http://localhost:8000/o/applications/register/
use the redirect url as http://django-oauth-toolkit.herokuapp.com/consumer/exchange/ for testing

#There is a test service at
http://django-oauth-toolkit.herokuapp.com/consumer/


#Change the look and feel - needs work :)