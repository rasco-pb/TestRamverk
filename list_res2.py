import pyvisa

def lista_resurser():
    # Specifika pyvisa-py backend
    rm = pyvisa.ResourceManager('@py')
    resources = rm.list_resources()
    
    if resources:
        print("Tillgängliga resurser:")
        for resource in resources:
            print(resource)
    else:
        print("Inga resurser tillgängliga.")

lista_resurser()
