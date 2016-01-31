from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import generic
from datetime import datetime
import random
import os


def get_random_quotes():

    mapper=[
           {'author':'Anjali','topic':'Love','quote':'We go together like copy and paste'},
           {'author':'Marc','topic':'Psycology','quote':'Excellence is not a skill, it is an attitude'},
           {'author':'Vayun','topic':'Love','quote':'We accept the love we think we deserve'},
           {'author':'Nirmal','topic':'Politics','quote':'Those who deny freedom for others deserve it not for themselves'},
           {'author':'Vayun','topic':'Love','quote':'We accept the love we think we deserve'},
           {'author':'Anonymous','topic':'Psycology','quote':'Beauty attracts heart but personality captures the heart'},
           {'author':'Fran Lebowitz','topic':'Psycology','quote':'Humility is no substitute for a good personality'},
           {'author':'Marcus Tull','topic':'Psycology','quote':'The life of the dead is placed in the memory of the living'},

    ]
    selected =random.randint(0,8)
    return mapper[selected];

def index(request):
    context = ''
    count=0
    created=datetime.now()
    session=1#request.session.session_key()
    ip=request.META['REMOTE_ADDR']
    print "REMOTE_ADDR",ip,"created",created,"session",session
    if os.path.isfile('counterfile.txt'):
        try:
            f= open('counterfile.txt','r')
            count=f.read()
            counternew =int(count)+1
            f.close()
        except Exception,e :
            counternew=0
        try:
            if counternew%7 ==0 :
                mapper={'author':'','topic':'','quote':''}
                count=7
                counternew=0
            else:
                count=counternew
                mapper=get_random_quotes();

            f= open('counterfile.txt','w')
            f.write(str(counternew))
            f.close()
        except IOError,e:
             pass
    else:
        with open("counterfile.txt",'w') as f:
            count=0
            f.write('0');
            mapper=get_random_quotes();

    #f.write(count)

    context={
              'template_title':'Quotes',
              'randomquote':mapper,
              'ip':count,
              'count':count,
          }
    return (render(request, 'index.html',context))
