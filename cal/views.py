from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime


# Create your views here.
   
def conversion(request):

    now = datetime.datetime.now()
    time = datetime.datetime.now().strftime('%H:%M:%S')
    currentTime = now.hour  

    if currentTime < 12 :
         greet = 'Good Morning!'
    if currentTime >= 12 :
         greet = 'Good Afternoon!'
    if currentTime >= 18 :
         greet = 'Good Evening!'
  
    print(greet)



    context={'greet':greet, 'currentTime':currentTime, 'time':time}
    return render(request, 'cal/conversion.html', context)



def result(request, *args, **kwargs):
    
    if request.method == 'POST':
        user_payment = float(request.POST.get('month_amount'))
        option = request.POST.get('customRadioInline1')
        
        print('checking the option selected from dropdown menu')
        print(option)
        
       # try:
        #    amount = float(user_payment)
        #    print("Input is a float  number. Number = ", val)
       # except ValueError:
       #     print("No.. input is not a number. It's a string")

       #amount = float(user_payment)

        if option == '1':                
            paymentYearly = user_payment * 12
            
        else:
            paymentYearly = user_payment * 52
        
        paymentMonthly = paymentYearly / 12
        paymentWeekly = paymentYearly / 52
        paymentBiweekly = paymentWeekly * 2
        paymentSemimonthly = paymentMonthly / 2

        
        print('have a nice day')
    context={'paymentMonthly':paymentMonthly, 'paymentWeekly':paymentWeekly, 'paymentBiweekly':paymentBiweekly, 'paymentSemimonthly':paymentSemimonthly, 'paymentYearly':paymentYearly,}
   

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