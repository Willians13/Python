from math import hypot

co = float(input(" Digite o cateto oposto : "))
ca = float(input(" Digite o cateto adjancente :"))

hipo = hypot(co,ca)

print("A hipotenusa é {:.2f}".format(hipo))