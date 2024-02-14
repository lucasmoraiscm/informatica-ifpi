from classes_atv14 import*;

p1=Pessoa(12345678901,"Cléber","12/05/1950","Diabetes","Paciente diagnosticado com diabetes mellitus")
p2=Pessoa(10987654321,"Joana","22/02/1995","Imunossuprimido","Paciente em tratamento de câncer")
p3=Pessoa(38622366462,"Antônio","22/11/1988","Síndrome de Down","Paciente diagnosticado com síndrome de Down")
p4=Pessoa(76254624364,"Fabiana","04/08/2002","Doença neurológica crônica","Paciente diagnosticado com distrofia muscular")
p5=Pessoa(83374384723,"Carlos","23/12/1974","Pneumopatia","Paciente diagnosticado com doença pulmonar obstrutiva crônica")

p2.novaComorbidade("Hipertensão","Paciente diagnosticado com hipertensão estágio III")
p5.novaComorbidade("Transplantado","Paciente recebeu um transplante de rim")

v1=VacinaCovid(12345,"Piauí","Coronavac","10/06/2021",p1)
v2=VacinaCovid(54321,"Maranhão","Pfizer","04/05/2021",p2)
v3=VacinaCovid(72383,"Rio de Janeiro","Astrazeneca","25/10/2021",p3)
v4=VacinaCovid(26389,"Santa Catarina","Pfizer","15/05/2021",p4)
v5=VacinaCovid(86585,"Rio Grande do Norte","Coronavac","22/06/2021",p5)

cv1=ControleVacina()
cv2=ControleVacina()
cv3=ControleVacina()
cv4=ControleVacina()
cv5=ControleVacina()

cv1.incluirVacina(v1)
cv1.incluir2doseVacina(12345,"10/08/2021")
print(v1)
print(p1)

cv2.incluirVacina(v2)
cv2.incluir2doseVacina(54321,"04/07/2021")
print(v2)
print(p2)

cv3.incluirVacina(v3)
print(v3)
print(p3)

cv4.incluirVacina(v4)
cv4.incluir2doseVacina(26389,"15/06/2021")
print(v4)
print(p4)

cv5.incluirVacina(v5)
cv5.incluir2doseVacina(7346484375483,"22/08/2021")
print(v5)
print(p5)

RelatorioVacinação.relatorioComorbidade40(RelatorioVacinação)