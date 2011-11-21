from tkinter import *
import tkinter


import Ausgabe
import pickle
#from fileinput import close

#Fenster
root=Tk()

#Labels
l_BelegNr = Label(root, text="Beleg Nr. :")
l_Verkaeufer = Label(root, text="Verkäufer :")
l_Betrag = Label(root, text="Betrag :")
l_BuchungsDatum = Label(root, text="Buchungs Datum :")


#Entrys
e_BelegNr = Entry(root, width=25)
e_Verkaeufer = Entry(root, width=25)
e_Betrag = Entry(root, width=25)
e_BuchungsDatum = Entry(root, width=25)

#RadioButtons
bezahlungsart= StringVar()
rb_EC = Radiobutton(root, text="EC", variable=bezahlungsart, value="EC")
rb_VISA = Radiobutton(root, text="VISA", variable=bezahlungsart, value="VISA")
rb_Bar = Radiobutton(root, text="Bar", variable=bezahlungsart, value="Bar")

#Buttons
b_Abbrechen= Button(root)
b_OK = Button(root)

def ok():
    ausgabe=Ausgabe.Ausgabe()
    print (dir(tkinter))
    try:
        ausgabe.betrag=float(e_Betrag.get())
    except:
        messagebox.showerror("Eingabefehler","Der Eingagebene Betrag ist nicht korrekt")
        return
    try:
        ausgabe.belegNr = int(e_BelegNr.get())
    except:
        messagebox.showerror("Eingabefehler","Die Belegnummer ist keine Nummer")
        return
    
    ausgabe.verkaeufer = e_Verkaeufer.get()
    if ausgabe.verkaeufer == "":
        messagebox.showerror("Eingabefehler","Sie müssen einen Verkaeufer Eingeben")
        return
    
    ausgabe.buchungsDatum = e_BuchungsDatum.get()
    if ausgabe.buchungsDatum == "":
        messagebox.showerror("Eingabefehler","Sie müssen eine Buchungsdatum Eingeben")
        return

    if bezahlungsart.get()=="EC":
        ausgabe.ec=True
    elif bezahlungsart.get()=="VISA":
        ausgabe.visa=True
    elif bezahlungsart.get()=="Bar":
        ausgabe.bar=True
    else:
        messagebox.showerror("Eingabefehler","Sie müssen eine Bezahlungsart auswählen"+bezahlungsart.get())
        return
        
    #Jetzt kann ausgabe gespeichert werden


    """
    f = open('Datei.txt', 'w')
    
    data = list(ausgabe)
    pickle.dump(data, f)
    data.append('a')
    pickle.dump(data, f)
    data.append('b')
    pickle.dump(data, f)
    f.close()
    
    liste = []
    data = liste(ausgabe)
    liste.append(data, f)
    """
    
    #Objekte aus Datei lesen und an Liste uebergeben
    fileRead = open("Datei.txt", "rb")
    liste = []
    liste = pickle.load(fileRead)
    fileRead.close()
    
    #neues Objekt an Liste anhaengen und in Datei schreiben 
    fileSave = open("Datei.txt", "wb")
    liste.append(ausgabe)
    pickle.dump(liste, fileSave)
    fileSave.close()
    
    ##pickle.dump(ausgabe, f)
    #Datei schliessen
    ##f.close()
    
    
def abbrechen():
    #zum testen Objekte aus Datei auslesen und auf der Console anzeigen
    f = open("Datei.txt")
    """
    x = pickle.load(f)
    print(x)
    """
    
    #Datei schliessen
    f.close()
    root.destroy()    


#Button Commands setzen
b_Abbrechen.configure(text="Abbrechen", command=abbrechen)
b_OK.configure(text="OK", command=ok)

#Widgets Ins Grid legen
l_BelegNr.grid(row=1, column=1)
e_BelegNr.grid(row=1, column=2)
l_Verkaeufer.grid(row=2, column=1)
e_Verkaeufer.grid(row=2, column=2)
l_Betrag.grid(row=3, column=1)
e_Betrag.grid(row=3, column=2)
l_BuchungsDatum.grid(row=4, column=1)
e_BuchungsDatum.grid(row=4, column=2)
rb_EC.grid(row=5, column=2)
rb_VISA.grid(row=6, column=2)
rb_Bar.grid(row=7, column=2)
b_Abbrechen.grid(row=8, column=1)
b_OK.grid(row=8, column=2)

#Mainloop starten
root.mainloop()



