from math import cos, sin, tan, radians

a = float(input(" Informe o valor do angulo : "))

co = cos(radians(a))
se = sin(radians(a))
ta = tan(radians(a))

print(" O angula {:.2f} tem um cosseno de {:.2f}, um seno de {:.2f} e uma tangente de {:.2f} ".format(a,co,se,ta))