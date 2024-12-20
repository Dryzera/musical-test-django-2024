from django.template import Library

register = Library()

@register.filter
def add_zero_left(number):
    number = str(number)
    n = number.split(':', 1)
    if len(n[0]) == 1:
        new_text = f'0{n[0]}:{n[1]}'
        return new_text
    return number