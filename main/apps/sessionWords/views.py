from django.shortcuts import render, redirect
from datetime import datetime

def index(request):
    return render(request,'sessionWords/index.html')

def addWord(request):
    request.session['word'] = request.POST['word']
    request.session['color'] = request.POST['color']
    if 'big' in request.POST:
        request.session['big'] = 'Big'
    else:
        request.session['big'] = 'Small'
    now = datetime.now().strftime('%-I:%M %p %b %-d %Y')
    data = {'c':request.session['color'],'w':request.session['word'],'b':request.session['big'],'t':now}
    if 'text' not in request.session:
        request.session['text'] = [data]
    else:
        request.session['text'].append(data)
    return redirect('/')

def clear(request):
    request.session.clear();
    return redirect('/')
