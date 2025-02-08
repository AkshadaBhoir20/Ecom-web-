from flask import Flask,jsonify

app = Flask(__name__)

class Product:
    def __init__(self,id,name,price):
        self.id=id
        self.name=name
        self.price=price

class ShoppingCart:
    def __init__(self):
                self.products =[]

    def add_product(self,product):
                self.products.append(product)

    def calculate_total(self):
                        return sum(product.price for product in self.products)
                
#Sample Products

product1 = Product(1, "iPhone" , 1000)
product2 = Product(2,"Haedphones",100)

#Sample Shopping CArt
cart = ShoppingCart()
cart.add_product(product1)
cart.add_product(product2)

@app.route('/cart/total', methods=['GET'])
def get_cart_total():
        total = cart.calculate_total()
        return jsonify({"total_price": total})

if __name__=='__main__':
       app.run(debug=True) 