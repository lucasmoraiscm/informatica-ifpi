from classes_atv11 import*;

v1=Vacina_covid19(12345,"Piauí",1)
v2=Vacina_covid19(54321,"Ceará",3)
v3=Vacina_covid19(62328,"Maranhão",2)

Maria=Pessoa(12345678,"Maria",10,5,1950)
João=Pessoa(87654321,"João",7,11,1974)
Antônio=Pessoa(17236594,"Antônio",22,8,1998,True,"Asma aguda")
Tais=Pessoa(59473756,"Tais",17,4,1958)

Maria.vacinar1aDose(v1)
Maria.vacinar2aDose(v1,2,7,2021)
print(Maria)

João.vacinar1aDose(v2)
João.vacinar2aDose(v2,2,11,2021)
print(João)

Antônio.vacinar1aDose(v3)
Antônio.vacinar2aDose(v3,2,9,2021)
print(Antônio)

Tais.vacinar1aDose(v1)
Tais.vacinar1aDose(v2)
print(Tais)