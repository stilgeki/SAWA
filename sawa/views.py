from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render
from django.core.management import call_command
from sawa.models import Sentiment, SentimentPercentage, SentimentCount

def upload(request):
    return render(request, 'sawa/upload.html')

def execute(request):
    return render(request, 'sawa/execute.html')


def help(request):
    return render(request, 'sawa/help.html')

def results(request):
    
    #Delete all values in previous sessions
    SentimentPercentage.delete_session_values()
    SentimentCount.delete_session_values()
    
    sentiment = call_command('analysis')
    pt_sentiment = SentimentPercentage.objects.all().distinct()
    ct_sentiment = SentimentCount.objects.all().distinct()
    
    context = {'pt_sentiment': pt_sentiment, 'sentiment': sentiment, 'ct_sentiment': ct_sentiment}
    return render(request, 'sawa/results.html', context)

def loading(request):
    return render(request, 'sawa/loading.html')
