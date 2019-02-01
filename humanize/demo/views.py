from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    now=datetime.datetime.now()
    context={
        'first':6,
        'second':343245,
        'third':344366,
        'fourth':4512,
        'fifth':12,
        'now': now,
        'other_date':now+datetime.timedelta(days=1),
        'future':now+ datetime.timedelta(days=542),
        'past':now- datetime.timedelta(days=14),
    }
    return render(request,'demo.html',context)