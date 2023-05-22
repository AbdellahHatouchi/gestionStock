
from main import my_store
import tkinter as tk
from tkinter import ttk,messagebox
from product import Product


root = tk.Tk()
root.title("Gestion de Stock")
window_width = 800
window_height = 550
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
root.resizable(False,False)
root.iconbitmap('./store.jpg') #icon
menu = ["Display Infortmaion of Store",
        "Display All Product in Store",
        "Display All Product Disponible in Store",
        "Display All Product No Disponible in Store",
        "Create new Product",
        "update Product exist in store",
        "update disponiblite of Product exist in store",
        "Delete Product exist in store",
        "Search Product by ID",
        "Search Product by name",
        "Exit"]
try:
    def display_all_product(frame):
        table = ttk.Treeview(frame, columns=('col_1', 'col_2', 'col_3','col_4','col_5'))
        table.heading('#0', text='ID')
        table.heading('col_1', text='Product Name')
        table.heading('col_2', text='Price')
        table.heading('col_3', text='Disponible')
        table.heading('col_4', text='TVA')
        table.heading('col_5', text='Discount')
        
        table.column('#0',width=100)
        table.column('col_1',width=200)
        table.column('col_2',width=100)
        table.column('col_3',width=100)
        table.column('col_4',width=75)
        table.column('col_5',width=75)
        # Inserting sample data
       
        if len(my_store.products)==0:
            pass
        else:
            for id,product in enumerate(my_store.products):
                table.insert(parent='', index='end', iid=id, text=product.product_id, values=(product.name,product.price,product.is_disponible,product.tva,product.discount))

        table.grid(column=0,row=1,sticky=tk.NSEW)
        scrollbar = ttk.Scrollbar(frame,orient=tk.VERTICAL,command=table.yview)
        table.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=1,column=1,sticky='ns')
    def display_store(frame):

        # Store information
        name_label = ttk.Label(frame, text="Name:",font=("TKDefaultFont",16))
        name_label.grid(row=1, column=0, padx=5, pady=5)
        name_value = ttk.Label(frame, text=my_store.name,font=("TKDefaultFont",16))
        name_value.grid(row=1, column=1, padx=5, pady=5)

        phone_label = ttk.Label(frame, text="Phone Number:",font=("TKDefaultFont",16))
        phone_label.grid(row=2, column=0, padx=5, pady=5)
        phone_value = ttk.Label(frame, text=my_store.tel,font=("TKDefaultFont",16))
        phone_value.grid(row=2, column=1, padx=5, pady=5)

        address_label = ttk.Label(frame, text="Address:",font=("TKDefaultFont",16))
        address_label.grid(row=3, column=0, padx=5, pady=5)
        address_value = ttk.Label(frame, text=my_store.address,font=("TKDefaultFont",16))
        address_value.grid(row=3, column=1, padx=5, pady=5)
    def create_table(f,cols):
        table = ttk.Treeview(f,columns=cols)

    def create_product(frame):
        def data():
            name = name_value.get()
            price = float(price_value.get())
            purchase_cost = float(purchase_cost_value.get())
            tva = float(tva_value.get())
            discount = float(discount_value.get())
            desgnation = desgnation_value.get()
            product =  Product(name,price,purchase_cost,desgnation,tva,discount)
            my_store.create_product(product)
            messagebox.showinfo('Create Product',f"Product with ID {product.product_id} Created Succefully :)")
        name_label = ttk.Label(frame, text="Product Name:",font=("TKDefaultFont",14))
        name_label.grid(row=1, column=0,sticky=tk.NSEW, padx=5, pady=5)
        name_value = ttk.Entry(frame,font=("TKDefaultFont",14))
        name_value.grid(row=1, column=1,sticky=tk.NSEW, padx=5, pady=5)

        price_label = ttk.Label(frame, text="Price :",font=("TKDefaultFont",14))
        price_label.grid(row=2, column=0,sticky=tk.NSEW, padx=5, pady=5)
        price_value = ttk.Entry(frame,font=("TKDefaultFont",14))
        price_value.grid(row=2, column=1,sticky=tk.NSEW, padx=5, pady=5)

        purchase_cost_label = ttk.Label(frame, text="Purchase Cost:",font=("TKDefaultFont",14))
        purchase_cost_label.grid(row=3, column=0,sticky=tk.NSEW, padx=5, pady=5)
        purchase_cost_value = ttk.Entry(frame,font=("TKDefaultFont",14))
        purchase_cost_value.grid(row=3, column=1,sticky=tk.NSEW, padx=5, pady=5)
        
        tva_label = ttk.Label(frame, text="TVA:",font=("TKDefaultFont",14))
        tva_label.grid(row=4, column=0,sticky=tk.NSEW, padx=5, pady=5)
        tva_value = ttk.Entry(frame,font=("TKDefaultFont",14))
        tva_value.grid(row=4, column=1,sticky=tk.NSEW, padx=5, pady=5)
        
        discount_label = ttk.Label(frame, text="Discount:",font=("TKDefaultFont",14))
        discount_label.grid(row=5, column=0,sticky=tk.NSEW, padx=5, pady=5)
        discount_value = ttk.Entry(frame,font=("TKDefaultFont",14))
        discount_value.grid(row=5, column=1,sticky=tk.NSEW, padx=5, pady=5)
        
        desgnation_label = ttk.Label(frame, text="Desgnation:",font=("TKDefaultFont",14))
        desgnation_label.grid(row=6, column=0,sticky=tk.NSEW, padx=5, pady=5)
        desgnation_value = ttk.Entry(frame,font=("TKDefaultFont",14))
        desgnation_value.grid(row=6, column=1,sticky=tk.NSEW, padx=5, pady=5)
        btn = ttk.Button(frame,text="Create Product",padding=8,command=data)
        btn.grid(column=0,row=7,columnspan=2,sticky=tk.NSEW,padx=16,pady=8)

    def back(frame_current,frame_toback):
        frame_current.pack_forget()
        frame_toback.pack()
    def select(n):
        print(n)
        frame.pack_forget()
        frame2=ttk.Frame(root,padding=20)
        l = ttk.Label(frame2,text=menu[n-1],font=("TKDefaultFont",22),justify="center")
        l.grid(column=0,row=0,sticky=tk.NSEW,padx=16,pady=8)
        b = ttk.Button(frame2,text="Back",command=lambda: back(frame2,frame))
        b.grid(column=1,row=0,sticky=tk.NSEW,padx=16,pady=8)
        if n==1:
            display_store(frame2)
        elif n==2:
            display_all_product(frame2)
        elif n==5:
            create_product(frame2)
        elif n==11:
            pass
        frame2.pack()

    frame = ttk.Frame(root)
    label = ttk.Label(frame,text="Store Menu",font=("TKDefaultFont",22),justify="center")
    label.grid(column=0,row=0,sticky=tk.NSEW,padx=16,pady=8)
    i=1
    for n,fn in enumerate(menu) :
        j=int(n%2)
        ttk.Button(frame,text=fn,padding=12,width=50,command=lambda n=n+1: select(n)).grid(column=j,row=i,sticky=tk.NW,padx=16,pady=8)
        if n%2 == 1 :
            i+=1
    frame.pack()
finally:
    root.mainloop()