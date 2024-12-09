alt = float(input("Altura da parede "))
larg = float(input("largura da parede "))

area = float(alt * larg)
tinta =float(area / 2)

print("Uma parede com {}m2 necessita de {}l de tinta para ser pintada.".format(area, tinta))