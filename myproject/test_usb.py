import usb.core
import usb.util

# Hitta din oscilloskopenhet (använd Vendor ID och Product ID från lsusb)
dev = usb.core.find(idVendor=0x2a8d, idProduct=0x0386)

if dev is None:
    raise ValueError('Enhet inte hittad')

print("Oscilloskop anslutet")
