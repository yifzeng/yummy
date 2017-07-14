from django.http import Http404, HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from yummy.forms import Personform
from person.models import Person
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
import datetime,time

def pseron_list(request):
    persons = []
    
    if request.GET:
        form = Personform(request.GET)        
        ctx = request.GET
        personslist = Person.objects.filter(Q(city__icontains=ctx['city']) & Q(gender=ctx['gender']))
        print(personslist.count())            
        paginator = Paginator(personslist, 10) # Show 25 contacts per page
        page = request.GET.get('page')
        try:
            persons = paginator.page(page)
        except PageNotAnInteger:
                # If page is not an integer, deliver first page.
            persons = paginator.page(1)
        except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
            persons = paginator.page(paginator.num_pages)
        
        return render(request, 'person_list.html', {'persons': persons,'form':form})
       
    else:
         print(" NOT request.GET")
         form = Personform(initial={'gender': '女'})
         return render(request, 'person_list.html', {'persons': persons,'form':form})




def current_datetime(request):
    now = datetime.datetime.now()
 
    html = render_to_string('current_datetime.html',{'current_date': now})
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
        
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = render_to_string('hours_ahead.html',{'hour_offset': offset,'next_time':dt})
    return HttpResponse(html)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(initial={'subject': '王晨我爱你!'})
    return render_to_response('contact_form.html', {'form': form})

def thanks(request):
    now = datetime.datetime.now()
    html = render_to_string('current_datetime.html',{'current_date': now})
    return HttpResponse(html)