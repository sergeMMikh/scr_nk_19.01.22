product_price = ['68,97\xa0', '114,99\xa0', '']

price = ''.join([i.replace(u'\xa0', u"€ ") for i in product_price])

print(f'price: {price}')
