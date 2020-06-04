from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.


def conversion(request):
    



    context={}
    return render(request, 'cal/conversion.html', context)



def result(request):

    #paymentMonthly = conversion(payment_monthly)
    #paymentWeekly = conversion(payment_weekly)
    #paymentBiweekly = conversion(payment_biweekly)
    #paymentSemimonthly = conversion(payment_semimonthly)

      
    paymentMonthly = 696

    payment_yearly = float(paymentMonthly) * 12
    paymentWeekly = payment_yearly / 52
    paymentBiweekly = paymentWeekly * 2
    paymentSemimonthly = paymentMonthly / 2

    context={'paymentMonthly':paymentMonthly, 'paymentWeekly':paymentWeekly, 'paymentBiweekly':paymentBiweekly, 'paymentSemimonthly':paymentSemimonthly, 'payment_yearly':payment_yearly}
   

    return render(request, 'cal/result.html', context)