from classesRadio import*;

estações=Estações_FM()

estação1=Estação_FM('88,9','Rádio Teresina','A Vida','Pop')
estação2=Estação_FM('101,7','Rádio Piauí','O dia','MPB')
estação3=Estação_FM('97,1','Rádio Fortaleza','A Noite','Rock')

radio1=Radio('AM-16456','Sony',50,estações)
radio2=Radio('Super455','Philco',76,estações)
radio3=Radio('7455-HKS','Mondial',42,estações)

estação1.entrar_no_Ar()
estações.cadastrar_FM(estação1)
estações.consultar_FM('88,9')
radio1.ligar_Desligar()
radio1.sintonizar_Freq('88,9')
print(radio1)

estação2.entrar_no_Ar()
estações.cadastrar_FM(estação2)
radio2.ligar_Desligar()
radio2.sintonizar_Estilo('MPB')
radio2.ajustar_Volume(33)
print(radio2)
radio2.ligar_Desligar()

estação3.entrar_no_Ar()
estações.cadastrar_FM(estação3)
estação3.atualiza_Musica('A Alegria','Forró')
radio3.ligar_Desligar()
radio3.sintonizar_Freq()
print(radio3)

estação3.sair_do_Ar()
estações.excluir_FM(estação3)