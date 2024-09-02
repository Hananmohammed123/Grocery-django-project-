from django import template
from gsapp.models import * 
register = template.Library() 
import json 


register = template.Library()

# @register.filter()
# def applydiscount(pid):
#     try:
#         data = Product.objects.get(id=pid)
#         price = float(data.price)
#         discount = float(data.discount)
#         discounted_price = price * (100 - discount) / 100
#         return round(discounted_price, 2)  # rounding to 2 decimal places for better readability
#     except (Product.DoesNotExist, ValueError, TypeError) as e:
#         return "N/A"  # Returning 'N/A' if there is any issue with the product data

# @register.filter()
# def productimage(pid):
#     try:
#         data = Product.objects.get(id=pid)
#         return data.image.url
#     except Product.DoesNotExist:
#         return ''  # Returning an empty string if the product doesn't exist

# @register.filter()
# def productname(pid):
#     try:
#         data = Product.objects.get(id=pid)
#         return data.name
#     except Product.DoesNotExist:
#         return 'Unknown'  # Returning 'Unknown' if the product doesn't exist

# @register.filter()
# def productprice(pid):
#     try:
#         data = Product.objects.get(id=pid)
#         return data.price
#     except Product.DoesNotExist:
#         return 0  # Returning 0 if the product doesn't exist

# @register.simple_tag
# def producttotalprice(data, qty):
#     try:
#         product = Product.objects.get(id=data)
#         price = float(product.price) * (100 - float(product.discount)) / 100
#         return int(qty) * price
#     except (Product.DoesNotExist, ValueError, TypeError) as e:
#         return 0  # Returning 0 if there is any issue with the product data or quantity
@register.filter()
def get_product(productli):
    try:
        productli = productli.replace("'", '"')
        myli = json.loads(str(productli))['objects'][0]
        print(myli)
        pro_li = []
        for i, j in myli.items():
            pro_li.append(int(i))
        product = Product.objects.filter(id__in=pro_li)
        print(product)
        return product
    except:
        return None

@register.simple_tag
def get_qty(pro, bookid):
    try:
        book = Booking.objects.get(id=bookid)
        productli = book.product.replace("'", '"')
        myli = json.loads(str(productli))['objects'][0]
        return myli[str(pro)]
    except:
        return 0
@register.filter()
def productimage(pid):
    data = Product.objects.get(id=pid)
    return data.image.url

@register.filter()
def productname(pid):
    data = Product.objects.get(id=pid)
    return data.name

@register.filter()
def productprice(pid):
    data = Product.objects.get(id=pid)
    return data.price

@register.simple_tag()
def producttotalprice(pid, qty):
    data = Product.objects.get(id=pid)
    return int(qty) * int(data.price)