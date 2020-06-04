from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.


def conversion(request):
    



    context={}
    return render(request, 'cal/conversion.html', context)



def result(request, *args, **kwargs):
    #paymentMonthly = conversion(payment_monthly)
    #paymentWeekly = conversion(payment_weekly)
    #paymentBiweekly = conversion(payment_biweekly)
    #paymentSemimonthly = conversion(payment_semimonthly)

      
    paymentMonthly = request.GET.get("amount")
    print(paymentMonthly)
    paymentYearly = (float(paymentMonthly)) * 12
    paymentWeekly = float(paymentYearly) / 52
    paymentBiweekly = float(paymentWeekly) * 2
    paymentSemimonthly = float(paymentMonthly) / 2

    context={'paymentMonthly':paymentMonthly, 'paymentWeekly':paymentWeekly, 'paymentBiweekly':paymentBiweekly, 'paymentSemimonthly':paymentSemimonthly, 'paymentYearly':paymentYearly}
   

    return render(request, 'cal/result.html', context)