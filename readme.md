#Clone the project

#Install all the packages
sudo pip -r packages

#Change the values in local_settings.py for test runs
    ##DB Settings
        By default uses the sqlite, change it what you like in settings.py
    ##SMTP settings  
        Change the values in settings.py
    ##Secret key 
        SECRET_KEY = '_' to any other value in settings.py
    

#For production 
- Make a copy local_settings.py and call it production_settings.py
- Change the values as per production requirement
- Never commit production_settings.py


#Deploy
./bin/deploy.sh


#Create a superuse - Only once in most cases    
./bin/create_superuser.sh

#Run    
./bin/run.sh

#URLS
##Admin login
http://localhost:8080/admin

##For others 
http://localhost:8080/

##Authorization url
http://localhost:8000/o/authorize

##Create new client for oauth
http://localhost:8000/o/applications/register/

##URL For access token
http://localhost:8000/o/token

##URL to get user profile
http://localhost:8000/api/user

##There is a test service at
- http://django-oauth-toolkit.herokuapp.com/consumer/
- use the redirect url as http://django-oauth-toolkit.herokuapp.com/consumer/exchange/ for testing


#Change the look and feel - needs work :)
