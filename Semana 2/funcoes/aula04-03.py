""" 
Artigo Python: entendendo o uso de *args e **kwargs em funções e métodos 
https://medium.com/rafaeltardivo/python-entendendo-o-uso-de-args-e-kwargs-em-fun%C3%A7%C3%B5es-e-m%C3%A9todos-c8c2810e9dc8
"""

def world_cup_titles(country, *args):    
    print('Country: ', country)    
    for title in args:
        print('year: ', title)

world_cup_titles('Brasil', '1958', '1962', '1970', '1994', '2002')


world_cup_titles('Espanha', '2010')


def calculate_price(value, **kwargs):
    tax_percentage = kwargs.get('tax_percentage')
    discount = kwargs.get('discount')    
    if tax_percentage:
        value += value * (tax_percentage / 100)
    if discount:
        value -= discount    
    return value

final_price = calculate_price(100.0)
print(final_price)

final_price = calculate_price(100.0, discount=5.0)
print(final_price)


final_price = calculate_price(100.0, tax_percentage=7)
print(final_price)

final_price = calculate_price(100.0, tax_percentage=7, discount=5.0)
print(final_price)

