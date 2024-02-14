from classePrincipal_Seguro import*;

seguradora1=ControleDeSeguros()

caio=Cliente(12345678901,'Caio',40)
fernando=Cliente(10987654321,'Fernando',52)
rosana=Cliente(98197367627,'Rosana',27)
bruna=Cliente(35624625332,'Bruna',66)

seguro1=SeguroVida(12345,caio,'Caio')
seguro2=SeguroAutomóvel(54321,fernando,1232573457,'Gol',2015,25000)
seguro3=SeguroAutomóvel(75137,caio,9824792493,'Bros',2018,10000)
seguro4=SeguroVida(83573,rosana,'Rosana')
seguro5=SeguroAutomóvel(43949,rosana,5397738573,'Onix',2020,47500)
seguro6=SeguroVida(75734,bruna,'Bruna')
seguro7=SeguroVida(32764,fernando,'Fernando')

seguradora1.cadastrarSeguro(seguro1)
seguradora1.cadastrarSeguro(seguro2)
seguradora1.cadastrarSeguro(seguro3)
seguradora1.cadastrarSeguro(seguro4)
seguradora1.cadastrarSeguro(seguro5)
seguradora1.cadastrarSeguro(seguro6)
seguradora1.cadastrarSeguro(seguro7)
seguradora1.relatorio()