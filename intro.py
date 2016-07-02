partecipante1={"nome":"Stefania", "cognome":"Carone", "data_nascita":[30,9,1989]}
#print(partecipante1)
#print(len(partecipante1))
partecipante2={"nome":"Stefania", "cognome":"Carone", "data_nascita":[30,9,1989]}
anno1=partecipante1["data_nascita"][2]
anno2=partecipante2["data_nascita"][2]
mese1=partecipante1["data_nascita"][1]
mese2=partecipante2["data_nascita"][1]
giorno1=partecipante1["data_nascita"][0]
giorno2=partecipante2["data_nascita"][0]
#print(anno2,anno2)
#print(anno1>anno2)
#print(anno1<anno2)
#print(anno1-anno2)
#print(anno2-anno1)
#print(anno1,"-",anno2,"=",anno1-anno2)
if anno1==anno2 and mese1==mese2 and giorno1==giorno2:
    print("partecipante1 e partecipante2 sono nati lo stesso giorno")
elif anno1==anno2:
    print("partecipante1 e partecipante2 hanno la stessa età")
elif anno1<anno2:
    print("partecipante2 è più piccolo di partecipante1")
else:
    print ("partecipante1 è più piccolo di partecipante2")
