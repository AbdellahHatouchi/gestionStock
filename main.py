from stock import Stock
from product import Product

def display_menu():
    print("""
    +------------------- Store Menu -------------------+
    | 1. Display Infortmaion of Store                  |
    | 2. Display All Product in Store                  |
    | 3. Display All Product Disponible in Store       |
    | 4. Display All Product No Disponible in Store    |
    | 5. Create new Product                            |
    | 6. update Product exist in store                 |
    | 7. update disponiblite of Product exist in store |
    | 8. Delete Product exist in store                 |
    | 9. Search Product by ID                          |
    | 10. Search Product by name                       |
    | 11. Exit                                         |
    +--------------------------------------------------+
    """)

my_store = Stock("project Store",'tinghir','486548564')
my_store.create_product(Product('p1',67,55,"fjhfk",5))
choix = None
product_id =""
product_name = ""
price = 0.0
pruchase_cost = 0.0
tva = 0.0
discount = 0.0
is_disponible = True
desgnation = ""
def main():
    while True:
        display_menu()
        try :
            choix = int(input("Please select number of menu : "))
            if choix == 1 :
                print(my_store)
            elif choix == 2:
                if len(my_store.products) == 0:
                    print('\n Product list is Empty!!\n')
                else :
                    for product in my_store.products :
                        print(product)
            elif choix == 3:
                products  = my_store.get_products_by_disponiblite()
                if len(products) != 0:
                    for product in products:
                        print(product)
                else :
                    print('\nList of Product disponible is Empty!\n')
            elif choix == 4:
                products  = my_store.get_products_by_disponiblite(False)
                if len(products) != 0:
                    for product in products:
                        print(product)
                else :
                    print('\nList of Product No disponible is Empty!\n')
            elif choix == 5:
                try :
                    product_name = str(input("Product Name : \n")) 
                    price = float(input("Product Price : \n")) 
                    pruchase_cost = float(input("Product Pruchase Cost : \n")) 
                    tva = float(input("TVA : \n"))
                    discount = float(input("Discount (by default is 0): \n") or 0.0)
                    desgnation = str(input("Desgnation : \n"))
                    
                    product = Product(product_name,price,pruchase_cost,desgnation,tva,discount)
                    if my_store.create_product(product) :
                        print('\nProduct Created successful :) \n')
                    else:
                        raise
                except :
                    product_id =""
                    product_name = ""
                    price = 0.0
                    pruchase_cost = 0.0
                    tva = 0.0
                    discount = 0.0
                    is_disponible = True
                    desgnation = ""
                    print('Opss! something went wrong :( !!!')
            elif choix == 6:
                product_id = str(input('Please write product ID : '))
                product  = my_store.get_product_by_ref(product_id)
                if product != None :
                    print("\nNOTE: if you not update any fiald click Entre\n")
                    product_name = str(input(f"Product Name: ({product.name})\n")) or product.name
                    price = float(input(f"Product Price : ({product.price})\n") or product.price)
                    pruchase_cost = float(input(f"Product Pruchase Cost : ({product.pruchase_cost})\n") or product.pruchase_cost)  
                    tva = float(input(f"TVA : ({product.tva})\n") or product.tva)
                    discount = float(input(f"Discount ({product.discount}): \n") or product.discount)
                    is_disponible = bool(input(f"Disponible ({product.is_disponible}): \n") or product.is_disponible)
                    desgnation = str(input(f"Desgnation : ({product.desgnation})\n")) or product.desgnation
                    try:
                        product = Product(product_name,price,pruchase_cost,desgnation,tva,discount,is_disponible)
                        product.product_id = product_id
                        if my_store.update_product(product):
                            print("\nProduct updated Successful :) \n")
                        else:
                            raise
                    except :
                        print('Opss! something went wrong :( !!!')
                else :
                    print(f'\nProduct with id {product_id} not Fount :( \n')
            elif choix == 7:
                product_id = str(input('Please write product ID : '))
                product = my_store.get_product_by_ref(product_id)
                if product != None:
                    dispo = str(input('The Product is Disponible (y/n): '))
                    if (dispo == "y" or dispo=="yes") :
                        is_disponible = True 
                    else: 
                        is_disponible = False
                    product.set_is_disponible(is_disponible)
                    print(f'\nSuccessful update disponiblite of product ID : {product.product_id}\n')
                else:
                    print(f'\nProduct of ID {product_id} Not Found!!\n')
            elif choix == 8:
                product_id = str(input('Please write product ID : '))
                product  = my_store.get_product_by_ref(product_id)
                if product != None :
                    confirm = str(input('Are you sure you want delete this product ? (y/n)'))
                    if confirm == "y" or confirm=="yes":
                        my_store.delete_product(product)
                        print('\nDeleted producted successful :) \n')
                    else :
                        print('\nOpertion canceled :)\n')
                else:
                    print(f'\nProduct with id {product_id} not Fount :( \n')
            elif choix == 9:
                product_id = str(input('Please write product ID : '))
                product = my_store.get_product_by_ref(product_id)
                if product != None:
                    print(product)
                else:
                    print(f'\nProduct of ID {product_id} Not Found!!\n')
            elif choix == 10:
                product_name = str(input('Please write product name or part of name : '))
                products = my_store.get_products_by_name(product_name)
                if len(products) != 0:
                    for product in products:
                        print(product)
                else:
                    print(f'\nProduct of name {product_name} Not Found!!\n')
            elif choix == 11:
                print("Thank you for use application")
                print("\nsaving data ...\n")
                if my_store.save_to_json():
                    print('\nSuccessful saving data\n')
                    break
                else:
                    print('\nError can not be save data\n')
                    confirm = str(input('close app (y/n):'))
                    if confirm == 'y' or confirm == 'yes':
                        break
                    else:
                        pass
        except:
            print('the value not exist in menu please select correct value!')
if __name__ == "__main__":
    main()