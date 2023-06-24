from django.shortcuts import render

# Create your views here.

rooms = [
    {'id':1,'name':'Lets learn Python'},
    {'id':2,'name':'frontend developers'},
    {'id':3,'name':'design with me'},

]

def home(request):
    context = {'rooms':rooms}
    return render(request,'base/home.html',context)
    # return render(request,'home.html',{'rooms':rooms})


def room(request,pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    
    context = {'room':room}


    return render(request,'base/room.html',context)