from django import template
register = template.Library()
def html5type(var):
    if isinstance(var, int):
        return 'number'
    else:
        return 'text'  

register.filter('html5type', html5type)
