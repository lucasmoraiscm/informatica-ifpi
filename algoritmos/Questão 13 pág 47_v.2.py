#conversor binário p/ decimal (© 2020, N.R.)#
while True:
    binario=input("Digite um número binário:")
    dec=0
    exp=0
    for i in range(len(binario)-1,-1,-1):
        dec=dec+int(binario[i])*(2**exp)
        exp+=1
    print("o número decimal é",dec)
