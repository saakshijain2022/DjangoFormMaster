from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.

from .forms import *
# done wrt forms2.html  -- import every form you want

def error_404_view(request,exception):
    return render(request,'404.html')

response = HttpResponse('Hello World')
print(response.content)
# output is b'Hello World'

def myfunctioncall(request):
    return HttpResponse("Hello World")


def myfunctionabout(request):
    return HttpResponse("About Response")


def add(request, a, b):
    return HttpResponse(a+b)


def intro(request, name, age):
    mydictionary = {
        "name": name,
        "age": age
    }
    return JsonResponse(mydictionary)


def mypage(request):
    return render(request, 'index.html')


def mysecondpage(request):
    return render(request, 'second.html')


def mythirdpage(request):
    var = "hello World"
    greeting = "hey how are you"
    myfruits = ["apple", "mango", "banana"]
    num1, num2 = 10, 7
    ans = num1 > num2

    mydictionary = {
        "var": var,
        "msg": greeting,
        "myfruits": myfruits,
        "num1": num1,
        "num2": num2,
        "ans": ans
    }
    return render(request, 'third.html', context=mydictionary)


def myimagepage(request):
    return render(request, 'imagepage.html')


def myimagepage2(request):
    return render(request, 'imagepage2.html')


def myimagepage3(request):
    return render(request, 'imagepage3.html')


def myimagepage4(request):
    return render(request, 'imagepage4.html')


def imagepage5(request, imagename):
    myimagename = str(imagename)
    myimagename = myimagename.lower()
    print(myimagename)
    if myimagename == "django":
        var = True
    elif myimagename == "python":
        var = False
    mydictionary = {
        "var": var
    }
    return render(request, 'imagepage5.html', context=mydictionary)


def myform(request):
    return render(request, 'myform.html')


def submitmyform(request):
    mydictionary = {
        "var1": request.POST['mytext'],
        "var2": request.POST['mytextarea'],
        "method": request.method
    }
    return JsonResponse(mydictionary)
 # exta form making from gfg
# def home_view(request):
    # context ={}
    # context['form']= InputForm()
    # return render(request, "home.html", context)


def myform2(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            subject = request.POST['subject']
            email = request.POST['email']
        #     print(title)
            print(subject)
        #     var = str("Form Submitted"+ str(request.method))
        #     return HttpResponse(var)
        # else:
        #     mydictionary =  {
        #     "form" : form
        #     }
        #     return render(request,'myform2.html',context=mydictionary)
        # if form was NOT valid then will just render it

            mydictionary = {
                "form": FeedbackForm()
            }
            errorflag = False
            Errors = []
            if title != title.upper():
                errorflag = True
                # there is error
                errormsg = "Title should be in capital"
                Errors.append(errormsg)
                # mydictionary["error"] = True
                # mydictionary["errormsg"] = "Title should be in capital"
                # return render(request, 'myform2.html', context=mydictionary)

            import re
            # email verification
            regex = '^\w+([\.-]?\w+)@\w+([\.-]?\w+)*(\.\w{2,3})+$'
            if not re.search(regex, email):   #  search is to determine the regex pattern
                errorflag = True
                # error is there
                errormsg = "Not a Valid Email address"
                Errors.append(errormsg)

            if errorflag != True:
                # no error
                mydictionary["success"] = True
                mydictionary["successmsg"] = "Form Submitted"

            # updating the dictionary
            mydictionary["error"] = errorflag
            mydictionary["errors"] = Errors
            print(mydictionary)
            return render(request, 'myform2.html', context=mydictionary)

    elif request.method == "GET":
        form = FeedbackForm()  # this is equivalent to FeedbackForm(None) initiaized the form
        # it will render the form on frontend part
        # for submittion e use POST METHOD
        mydictionary = {
            "form": form
            # "form": FeedbackForm()
        }
        return render(request, 'myform2.html', context=mydictionary)


'''
def myform2(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            subject = request.POST['subject']
            print(title)
            print(subject)
            var = str("Form Submitted"+ str(request.method))
            return HttpResponse(var)
        else:
            mydictionary =  {
            "form" : form
            }
            return render(request,'myform2.html',context=mydictionary)
        
    elif request.method == "GET":
        form = FeedbackForm()  # this is equivalent to FeedbackForm(None) initiaized the form
        # it will render the form on frontend part
        # for submittion e use POST METHOD
        mydictionary = {
            "form": form
        }
        return render(request, 'myform2.html', context=mydictionary)
'''

