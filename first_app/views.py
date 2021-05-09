from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from first_app.anforms import NewUser
from first_app.models import Webpage, Topic, AccessRecord


# Create your views here.

def index(request):
    # return HttpResponse("Hello World")
    # my_dict = {'insert_me': "Hello I am from views!!!"}
    # return render(request, 'first_app/index.html', context=my_dict)
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, 'first_app/index.html', context=date_dict)
#
#
# def from_name_view(request):
#     form = forms.FormName
#
#     if request.method == 'POST':
#         form = forms.FormName(request.POST)
#
#         if form.is_valid():
#             print("Validation Success!!!")
#             print("Name: " + form.cleaned_data['name'])
#             print("Email: " + form.cleaned_data['email'])
#             print("Message: " + form.cleaned_data['text'])
#
#     return render(request, 'first_app/form_page.html', {'from': form})


def users(request):
    form = NewUser()

    if request.method == 'POST':
        form = NewUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request, 'first_app/index.html')
        else:
            print('Form has error!!!')

    return render(request, 'first_app/form_page.html', {'forms': form})
