import pyvisa

def lista_resurser():
    rm = pyvisa.ResourceManager('@py')  # Använd pyvisa-py backend
    resources = rm.list_resources()
    
    if resources:
        print("Tillgängliga resurser:")
        for resource in resources:
            print(resource)
    else:
        print("Inga resurser tillgängliga.")

lista_resurser()
