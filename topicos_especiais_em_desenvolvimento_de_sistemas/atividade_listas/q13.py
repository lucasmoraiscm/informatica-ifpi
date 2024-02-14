mes = ['1 - Janeiro', '2 - Fevereiro', '3 - Março', '4 - Abril', '5 - Maio', '6 - Junho', 
'7 - Julho', '8 - Agosto', '9 - Setembro', '10 - Outubro', '11 - Novembro', '12 - Dezembro']
temp_media = []
acima_media = []
media_anual = 0

for t in range(12):
    temp = float(input("Digite a temperatura média do mês:"))
    temp_media.append([mes[t], temp])

for m in temp_media:
    media_anual += m[1]
media_anual /= 12

for a in temp_media:
    if a[1] > media_anual:
        acima_media.append(a)
        
print(acima_media)