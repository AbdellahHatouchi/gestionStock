
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
    def replace_content(n:int,frame:ttk.Frame):
        # Delete the current content of the frame
        frame.pack_forget()
        select(n)
    def display_all_product(frame):
        table_cols = ['Product Name','Price','Disponible','TVA','Discount']
        table = ttk.Treeview(frame, columns=[f'col_{i+1}' for i in range(len(table_cols))])
        table.heading('#0', text='ID')
        table.column('#0',width=100)
        for i,col in enumerate(table_cols):
            table.heading(f'col_{i+1}', text=col)
        
        table.column('col_1',width=200)
        table.column('col_2',width=100)
        table.column('col_3',width=100)
        table.column('col_4',width=75)
        table.column('col_5',width=75)
        # Inserting sample data
       
        if len(my_store.products)==0:
            label = ttk.Label(frame,text="List of Products is Empty!!",font=('TkDefaultFont',16),foreground="#1e88e5")
            label.grid(column=0,row=1,sticky=tk.NSEW,pady=60)
            btn = ttk.Button(frame,text="Create New Product",command=lambda: replace_content(5,frame),padding=8)
            btn.grid(column=0,columnspan=2,row=2,sticky=tk.NSEW,pady=8)
        else:
            for id,product in enumerate(my_store.products):
                table.insert(parent='', index='end', iid=id, text=product.product_id, values=(product.name,product.price,product.is_disponible,product.tva,product.discount))

            table.grid(column=0,row=1,sticky=tk.NSEW)
            scrollbar = ttk.Scrollbar(frame,orient=tk.VERTICAL,command=table.yview)
            table.configure(yscrollcommand=scrollbar.set)
            scrollbar.grid(row=1,column=1,sticky='ns')
    def display_store(frame):
        label_values = {
            "Name":my_store.name,
            "Phone Number":my_store.tel,
            "Address":my_store.address
        }
        # Store information
        for n,[label,value] in enumerate(label_values.items()):
            label_var = ttk.Label(frame, text=label+" :",font=("TKDefaultFont",16))
            label_var.grid(row=n+1, column=0,sticky=tk.NSEW, padx=5, pady=5)
            value_var = ttk.Label(frame, text=value,font=("TKDefaultFont",16))
            value_var.grid(row=n+1, column=1,sticky=tk.NSEW, padx=5, pady=5)
        
    def create_table(f,cols):
        table = ttk.Treeview(f,columns=cols)

    def create_product(frame):
        entry_labels = {
            "name":'Product Name',
            "price":"Product Price",
            "pruchase_cost":"Pruchase Cost",
            "tva":"TVA",
            "discount":"Discount",
            "desgnation":"Desgnation"
        }
        def data():
            # Get the data from the entry widgets
            product_data = {}
            for entry_name, entry_widget in entry_widgets.items():
                product_data[entry_name] = entry_widget.get()
            #use destructuring dict  
            product = Product(**product_data)
            my_store.create_product(product)
            messagebox.showinfo('Create Product',f"Product with ID {product.product_id} Created Succefully :)")
            # Reset the form
            for entry_widget in entry_widgets.values():
                entry_widget.delete(0, tk.END)
        
        # Create the form elements using ttk widgets
        entry_widgets:dict[str,ttk.Entry] = {}
        for n,[entry_name, entry_label] in enumerate(entry_labels.items()):
            label = ttk.Label(frame, text=entry_label,font=("TKDefaultFont",14))
            label.grid(row=n+1, column=0,sticky=tk.NSEW, padx=5, pady=5)
            entry_widgets[entry_name] = ttk.Entry(frame,font=("TKDefaultFont",14))
            entry_widgets[entry_name].grid(row=n+1, column=1,sticky=tk.NSEW, padx=5, pady=5)
        
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