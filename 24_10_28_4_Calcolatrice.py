Numero1 = float(input ("Inserisci il primo numero:\n"))
Numero2 = float(input ("Inserisci il primo numero:\n"))
Operazione = input ("""Insere il tipo di operazione da eseguire:
                        se divisione \" / \", se moltiplicazione \" * \" , 
                         altrimenti inserisci \" + \" per la somma e \" - \" per la sottrazione""")
if Operazione == "+":
    print (Numero1+Numero2)
elif Operazione == "-":
    print (Numero1-Numero2)
elif Operazione == "/":
    print (Numero1/Numero2)
elif Operazione == "*":
    print (Numero1*Numero2)
else:
    print ("Input errato")