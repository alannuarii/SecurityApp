from django import template

register = template.Library()

@register.filter(name='remove_substr')
def remove_substr(string):
    str1 = string.replace("[","")
    str2 = str1.replace("]","")
    str3 = str2.replace("'","")
    return str3