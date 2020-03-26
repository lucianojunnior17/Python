medida = float(input('Digite a Medida em Kilometros \n' ))
cm = medida*100
mm = medida*1000
dc = medida/100
hc = medida/1000
print('A medida de {:.1f}km coresponden a {:.1f}cm , {:.1f}mm, {} Devimetros,{} Hectometros. '.format(medida, cm, mm, dc, hc))
