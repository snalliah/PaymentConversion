from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime


# Create your views here.
   
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



    context={'greet':greet, 'currentTime':currentTime}
    return render(request, 'cal/conversion.html', context)



def result(request, *args, **kwargs):
    
    if request.method == 'POST':
        user_payment = request.POST.get('month_amount')
        option = request.POST.get('inputSelect')
        
        print('checking the option selected from dropdown menu')
        print(option)

        if option == '1':                
            paymentYearly = float(user_payment) * 52
            
        else:
            paymentYearly = (float(user_payment)) * 12

        paymentMonthly = float(paymentYearly) / 12
        #paymentYearly = float(paymentMonthly) * 12
        paymentWeekly = float(paymentYearly) / 52
        paymentBiweekly = float(paymentWeekly) * 2
        paymentSemimonthly = float(paymentMonthly) / 2

        context={'paymentMonthly':paymentMonthly, 'paymentWeekly':paymentWeekly, 'paymentBiweekly':paymentBiweekly, 'paymentSemimonthly':paymentSemimonthly, 'paymentYearly':paymentYearly,}
   

    return render(request, 'cal/result.html', context)

def about(request):
    

    context={}
    return render(request, 'cal/about.html', context)
