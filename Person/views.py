from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Person, Quote, Blog, Post
from .forms import EmailForm, BlogForm, PersonForm, PostForm
from django.utils import timezone

def index(request):
    response = HttpResponse()

    response.write("<html><body>\n")
    response.write("<h1>People</h1><hr>")
    pList = Person.objects.all()
    for p in pList:
        link = "<a href=\"Info/%d\">" % (p.id)
        response.write("<li>%s%s</a></li>" % (link, p.name))
    response.write("</body></html>")
    return render_to_response('person_index.html', {'pList': pList})
    #return response



def view_index(request):
    colors = ("BLUE","RED","GREEN")
    html = "<HTML><BODY>\n"
    html += "<H1>Colors Index</H1><HR>\n"
    for c in colors:
        html += "<FONT COLOR=%s><LI>%s</LI></FONT>\n" % (c, c)
    html += "</HTML></BODY>"
    return HttpResponse(html)



def view_calendar(request):
    week_days = ('Sunday','Monday','Tuesday',\
                 'Wednesday','Thursday','Friday',\
                 'Saturday')
    weeks = 5

    response = HttpResponse()
    response.write("<HTML><BODY>\n")
    response.write("Calendar<HR>\n")
    response.write("<TABLE BORDER=1><TR>\n")
    for d in week_days:
        response.write("<TD>%s</TD>\n" % d)
    response.write("</TR>\n")
    for w in range(1,weeks):
        response.write("<TR>\n")
        for d in week_days:
            response.write("<TD>&nbsp</TD>\n")
        response.write("</TR>\n")
    response.write("</BODY></HTML>")

    return response


def details(request, pID='0', opts=()):
    p = get_object_or_404(Person, pk=pID)
    rDict = {}
    p = get_object_or_404(Person, pk=pID)
    rDict['p'] = p
    quotes = Quote.objects.all()
    rDict['quotes'] = quotes
    return render_to_response('person_details.html', rDict)
    return response

def contact_view(request):
    eForm = EmailForm()
    return render_to_response('contact_form.html', { 'eForm':eForm })




def person_form(request, pID='0'):


    p = get_object_or_404(Person, pk=pID)
    if request.method == "POST":
        eForm = PersonForm(request.POST, instance=p)
        if eForm.is_valid():
            p = eForm.save(commit=False)
            p.save()
            return redirect('details', pID=pID)

    else:
        eForm = PersonForm(instance=p)

    return render(request, 'person_form.html', { 'pForm':eForm })

def person_detail(request, pk):
    post = get_object_or_404(Person, pk=pk)
    return render(request, 'person_form.html', {'pForm': post})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('details', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})

# Create your views here.
