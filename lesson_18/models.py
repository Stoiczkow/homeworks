class Category:
    pass

class Product:
    pass
    category = Category()

products = db.querry(Products).all()


for product in products:
    print(product.category_id)