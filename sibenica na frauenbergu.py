#vlozenie modulov
import random

#zadeklarovanie premennych a zoznamov
spravne = 0
nespravne = 0
slova = []
zakryte_slovo = []
spravne_pismena = []

#otvorenie suboru
subor = open("obesenec.txt","r")

def slovotvorba(): #funkcia na vytvorenie hadaneho slova
    #zadeklarovanie globalnej premennej
    global vybrane_slovo
    
    for riadok in subor: #cyklus na prechadzanie riadkov v subore
        riadocek = riadok.strip()

        slova.append(riadocek)

    #nahodny vyber zo zoznamu
    vybrane_slovo = random.choice(slova)

    for pismeno in vybrane_slovo: #cyklus na vytvorenie zakryteho slova
        zakryte_slovo.append(".")

def hadaj(): #funkcia na hadanie pismen
    #zadeklarovanie globalnych premennych
    global odpoved, vybrane_slovo, spravne, nespravne

    #vypytanie odpovede
    odpoved = str(input("".join(zakryte_slovo)+"\n"+"Hádaj písmeno:"))

    #vycistenie zoznamu
    zakryte_slovo.clear()

    #podmienka na spravne/nespravne odpovede
    if odpoved in vybrane_slovo:
        spravne_pismena.append(odpoved)
        spravne += 1
    else:
        nespravne += 1

    for pismeno in vybrane_slovo: #cyklus na prechadzanie pismen v slove
        #podmienka na odhalenie pismena
        if pismeno in spravne_pismena:
            zakryte_slovo.append(pismeno) 
        else:
            zakryte_slovo.append(".")

    #podmienka na dalsie pokracovanie
    if nespravne < 10:
        if spravne < len(vybrane_slovo):
            #znovuspustenie funkcie
            hadaj()
        else:
            #vypisanie pozadovanych hodnot
            print("".join(zakryte_slovo))
            print("Gratulujem, zachránil/a si sa a nemáš obvinenie z čarodejníctva.")
    else:
        #vypisanie pozadovanych hodnot
        print("Zlyhal/a si a obesili Ťa ako Barboru Roesslovú na Frauenbergu...")

#spustenie funkcii
slovotvorba()
hadaj()

#zatvorenie suboru
subor.close()
