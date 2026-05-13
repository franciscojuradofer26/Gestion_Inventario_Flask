import database

def verificar_producto(nombre,cantidad):
    if nombre=="":
        print("Debes introducir un nombre válido para el producto")

        return False
    
    if cantidad<=0:
        print("Debes introducir una cantidad válida para el producto")

        return False
    
    return True
    
def verificar_ID(id_producto):
    ids=[i[0] for i in database.productos()]
    return id_producto in ids