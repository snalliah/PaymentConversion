from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime


# Create your views here.

def home(request):
   

 #   mes = print('test')

    context={}
    return render(request, 'cal/home.html', context)

def navbar(reqeust):
    now = datetime.datetime.now()
    time = now.strftime("%H:%M:%S")




    context={'time':time}
    return render(request, 'cal/navbar.html', context)
    
def conversion(request):
    now = datetime.datetime.now()
    currentTime = now.hour  

    if currentTime < 12 :
         greet = 'Good Morning!'
    if currentTime >= 12 :
         greet = 'Good Afternoon!'
    if currentTime >= 18 :
         greet = 'Good Evening!'
  
    print(greet)



    context={'greet':greet, 'currentTime':currentTime,}

    return render(request, 'cal/conversion.html', context)



def result(request, *args, **kwargs):
    
    if request.method == 'POST':
        user_input = (request.POST.get('input_amount'))
        option = request.POST.get('customRadioInline1')
       
       # try:
        user_payment = float(user_input)
       # except ValueError as error:
       #     print(error)

       
        
        print('checking the option selected from dropdown menu')
        print(option)
        if option == '1':                
            paymentYearly = user_payment * 12
            
        elif option == '2':
            paymentYearly = user_payment * 52
        elif option == '3':
            paymentYearly = user_payment * 26
        elif option == '4':
            paymentYearly = user_payment * 24
        else:
            paymentYearly = user_payment
        
        paymentMonthly = paymentYearly / 12
        paymentWeekly = paymentYearly / 52
        paymentBiweekly = paymentWeekly * 2
        paymentSemimonthly = paymentMonthly / 2

        
        
        context={'paymentYearly':paymentYearly, 'paymentMonthly':paymentMonthly, 'paymentWeekly':paymentWeekly, 'paymentBiweekly':paymentBiweekly, 'paymentSemimonthly':paymentSemimonthly,}
   
   # else:
        return render(request, 'cal/result.html', context)

def about(request):
    

    context={}
    return render(request, 'cal/about.html', context)


def test(request): #Home tap

    now = datetime.datetime.now()

    currentTime = now.hour  

    if currentTime < 12 :
         greet = 'Good Morning!'
    if currentTime >= 12 :
         greet = 'Good Afternoon!'
    if currentTime >= 18 :
         greet = 'Good Evening!'
  
    print(greet)



    context={'greet':greet, 'currentTime':currentTime}
    return render(request, 'cal/test.html', context)