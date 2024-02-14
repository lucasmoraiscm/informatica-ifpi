#Sequência de Fibonacci até o 15º termo#
ant=0
atual=1
a=3
print(ant)
print(atual)
while a<16:
    n=ant+atual
    ant=atual
    atual=n
    a+=1
    print(n)
