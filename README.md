1. install Pycharm and python

install  virtualenv (in Pycharm termainal )

2.pip install virtualenv

3. virtualenv env
   
4. env/bin/activate
   
5. pip install -r /path/to/requirements.txt
   
6. python manage.py runserver 0.0.0.0:8000


Exposing a Django app with Ngrok

1. download Ngrok : https://ngrok.com/download
   
2. add token : ngrok config add-authtoken <token>

3. running local server >> external server : ngrok http 80
