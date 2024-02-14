#Sequência 1/2+1/4+...1/2n#
n=int(input("""1 / 2  +  1 / 4  +...1 / 2n
Digite o valor de n:"""))
for i in range(1,n+1):
    d=2*i
    if d==2*n:
        print("1 /",d)
        break
    print("1 /",d,end="  +  ")
    
