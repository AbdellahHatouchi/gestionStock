from product import Product
import json
from os import path
class Stock :
    def __init__(self,name:str,address:str,tel:str) -> None:
        self.name = name
        self.address = address
        self.tel = tel
        self.products : list[Product] = self.create_in_json_file()

    def get_product_by_ref(self,ref:str) -> Product | None:
        for product in self.products :
            if product.product_id == ref :
                return product
        return None
    
    def get_products_by_name(self,name) -> list[Product]:
        products :list[Product] = []
        for product in self.products :
            if product.name.find(name) != -1 :
                products.append(product)
        return products
    
    def get_products_by_disponiblite(self,is_disponible=True) -> list[Product]:
        products :list[Product] = []
        for product in self.products :
            if product.is_disponible == is_disponible :
                products.append(product)
        return products
    
    def create_product(self,product:Product)->bool:
        if isinstance(product,Product):
            self.products.append(product)
            return True
        return False
    
    def update_product(self,product:Product)->bool:
        if isinstance(product,Product):
            for product_stored in self.products:
                if product_stored.product_id == product.product_id:
                    product_stored.name = product.name
                    product_stored.price = product.price
                    product_stored.pruchase_cost = product.pruchase_cost
                    product_stored.desgnation = product.desgnation
                    product_stored.tva =product.tva
                    product_stored.discount =product.discount
                    product_stored.is_disponible = product.is_disponible
                    return True
            raise f"Product of id : {product.product_id} not Found"
        else :
            return False
        
    def delete_product(self,ref:str)->bool:
        product = self.get_product_by_ref(ref)
        if product != None :
            self.products.remove(product)
            return True
        return False
    
    def read_file_json(self):
        try:
            if path.exists(f"{self.name}.json"):
                with open(f"{self.name}.json","r") as file:
                    data = json.load(file)
                    file.close()
                return data
            raise
        except:
            return []
    
    def create_in_json_file(self):
        data = self.read_file_json()
        products = [Product.create_in_json(product) for product in data]
        return products
    
    def to_json(self):
        data=[product.to_json() for product in self.products]
        return data
    
    def save_to_json(self):
        try :
            with open(f"{self.name}.json","w") as file:
                json.dump(self.to_json(),file)
            return True
        except :
            return False
    
    def __str__(self) -> str:
        store= '\n'
        store += f"Store Name : {self.name}\n"
        store += f"Store tel : {self.tel}\n"
        store += f"Store Address : {self.address}\n"
        return store
