import http
import pyrebase
from django.shortcuts import render

config={
    'apiKey': "AIzaSyBTvLquqSQsKuweEIzNtE_DyrAN4vIe-A8",
  'authDomain': "atk-check.firebaseapp.com",
  'databaseURL': "https://atk-check-default-rtdb.asia-southeast1.firebasedatabase.app",
  'projectId': "atk-check",
  'storageBucket': "atk-check.appspot.com",
  'messagingSenderId': "582568391327",
  'appId': "1:582568391327:web:1969da6135dfb80f6a68aa",
#   'measurementId': "G-BF5ZZBXFJV"
}
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()

# Create your views here.
def firebase(request):
    channel_age = database.child('Data').child('Age').get().val()
    channel_result = database.child('Data').child('Result').get().val()
    channel_name = database.child('Data').child('Name').get().val()
    return render(request,'firebase.html',{
        "channel_age":channel_age,
        "channel_result":channel_result,
        "channel_name":channel_name
    })
    
def home(request):
    return render(request,'index.html')
    
def daily_report(request):
    return render(request,'daily_report.html')

def weekly_report(request):
    return render(request,'weekly_report.html')

def monthly_report(request):
    return render(request,'monthly_report.html')

def all_report(request):
    return render(request,'all_report.html')

def about(request):
    return render(request,'about.html')

def user(request):
    return render(request,'user.html')

def firebase(request):
    return render(request,'firebase.html')