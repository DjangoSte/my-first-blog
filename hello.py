def ciao (nome):
    print("Ciao "+nome+"!")
    print("come stai?")


#ciao("Stefania")
#ciao("Chiara")
ragazze=["Viviana","Dana","Stefania","Chiara","Francesca"]
ragazze.append("Enza")
ragazze.reverse()
for nome in ragazze:
    ciao(nome)

for i in range(1, 10000):
    print(i)
#print range(2,10)
