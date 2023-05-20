from uuid import uuid4

class Product :
    def __init__(self,name:str,price:float,pruchase_cost:float,desgnation:str,tva:float,discount :float=0.0,is_disponible:bool=True) -> None:
        self.product_id = "PR"+str(uuid4().int)[:4]
        self.name = name
        self.price = price
        self.pruchase_cost = pruchase_cost
        self.desgnation = desgnation
        self.tva =tva
        self.discount =discount
        self.is_disponible = is_disponible

    def set_is_disponible(self,is_disponible):
        self.is_disponible = is_disponible

    def __str__(self) -> str:
        product = '\n'
        product += f"ID : {self.product_id}\n"
        product += f"Name : {self.name}\n"
        product += f"price : {self.price}\n"
        product += f"Pruchase cost : {self.pruchase_cost}\n"
        product += f"TVA : {self.tva}\n"
        product += f"Discount : {self.discount}\n"
        product += f"the product is disponible : {self.is_disponible}\n"
        product += f"desgnation : {self.desgnation}\n"
        return product
    
    def __eq__(self, __value: object) -> bool:
        return type(__value) == Product and __value.product_id == self.product_id
    
    @classmethod
    def create_in_json(cls,product_json:dict):
        product = cls(
                   product_json.get('name'),
                   product_json.get('price'),
                   product_json.get('pruchase_cost'),
                   product_json.get('desgnation'),
                   product_json.get('tva'),
                   product_json.get('discount'),
                   product_json.get('is_disponible'))
        product.product_id = product_json.get("product_id") or product.product_id
        return product

    def to_json(self) :
        return self.__dict__


