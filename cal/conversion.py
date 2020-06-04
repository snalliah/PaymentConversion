class conversion(object):
    """description of class"""
    payment_monthly = 696

    payment_yearly = (float(payment_monthly) * 12)

    payment_weekly = payment_yearly / 52

    payment_biweekly = payment_weekly * 2

    payment_semimonthly = payment_monthly /2