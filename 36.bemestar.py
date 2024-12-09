hr_atv = float(input("Se exercitou quantas horas no mês ?"))
pnt = 0


if hr_atv <= 10 :
    total_pnt = hr_atv * 2
elif hr_atv > 10 and hr_atv <= 20 :
    total_pnt = hr_atv * 5
else:
    total_pnt = hr_atv * 10
    
ganho_total = total_pnt * 0.05

print(f"Pontos feitos: {total_pnt}")
print(f"Ganho: R$ {ganho_total}")
    
