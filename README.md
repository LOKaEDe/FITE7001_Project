1. install visual studio and python
   
2. pip install -r /path/to/requirements.txt
  
3. python manage.py runserver 


Exposing a Django app with Ngrok

1. download Ngrok : https://ngrok.com/download
   
2. add token : ngrok config add-authtoken <token>

3. running local server >> external server : ngrok http 8000
