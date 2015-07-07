from tkinter import *
from random import *
from datetime import *

zablokiraj=0
pravilni=0
napacni=0
prebrano=0

class sestevanje():
    def __init__(self,master):
        global zablokiraj
        global pravilni

        master.minsize(width=550, height=400)

#MENU#...........................................................................................................#MENU#
        menu = Menu(master)
        master.config(menu=menu)

        file_menu = Menu(menu)
        menu.add_cascade(label="Igra", menu=file_menu)

        file_menu.add_command(label="Shrani", command=self.shrani)
        file_menu.add_command(label="Odpri", command=self.odpri)
        file_menu.add_separator() 
        file_menu.add_command(label="Izhod", command=master.destroy)
        file_menu.add_command(label="Ponovi", command=self.restart)

#.....................................................................................................................#
        self.koliko=0
        self.napisi_koliko = StringVar(value=str(self.koliko))
        label_koliko = Label(master, textvariable=self.napisi_koliko)
        label_koliko.grid(row=10, column=15)

        Label(master,text="RAČUNANJE JE IGRA").grid(row = 0,rowspan = 1, column = 4, columnspan = 10,sticky=E+W+N+S)
        Label(master,text="Izberi računsko operacijo ter vpiši rezultat v okence. \n če želiš svoje rezultate shraniti pritisni okvirček 'Igra' in izberi 'shrani'").grid(row = 1,rowspan = 2, column = 0, columnspan = 20,sticky=E+W+N+S)

        Label(master, text="število poskusov:").grid(row=10, column=13)

        Label(master, text='Datum: '+str(date.today())).grid(row=0,column=18)

        self.stevec=0
        self.napis_stevec = StringVar(value=str(self.stevec))
        label_stevec = Label(master, textvariable=self.napis_stevec)
        label_stevec.grid(row=10, column=2)

        Label(master, text="tvoje točke:").grid(row=10, column=0)

        gumb_sestej = Button(master, text="SEŠTEVANJE", command=self.napisi_racun_sestevanje)
        gumb_sestej.grid(row=4, column=0)

        gumb_sestej = Button(master, text="ODŠTEVANJE", command=self.napisi_racun_odstevanje)
        gumb_sestej.grid(row=6, column=0)

        gumb_sestej = Button(master, text="MNOŽENJE", command=self.napisi_racun_mnozenje)
        gumb_sestej.grid(row=8, column=0)

        self.napisano = Listbox(master,selectmode=SINGLE)
        self.napisano.grid(row = 12,rowspan = 2, column = 0, columnspan = 25,sticky=E+W+N+S)

        self.seznam=[]

        self.canvas=Canvas(master, width=550, height=40)
        self.canvas.grid(row = 19,rowspan = 2, column = 0, columnspan = 18,sticky=E+W+N+S)
        for i in range(16):
            krogec=self.canvas.create_oval(10+i*30,10,30+i*30,30)

        self.napacni=Canvas(master, width=550, height=40)
        self.napacni.grid(row = 21,rowspan = 2, column = 0, columnspan = 18,sticky=E+W+N+S)
        for i in range(16):
            krogec=self.napacni.create_oval(10+i*30,10,30+i*30,30)

##        self.stranski=Canvas(master,width=50,height=300)
##        self.stranski.grid(row = 8,rowspan = 2, column = 17, columnspan = 2,sticky=E+W+N+S)

#SESTEVANJE#--------------------------------------------------------------------------------------------#SESTEVANJE#
    def napisi_racun_sestevanje(self):
        global zablokiraj
        zablokiraj=0
        frame=Frame
        frame.pack
        
        self.stevec1=randint(1,10)
        self.napisi_stevec1=StringVar(value=str(self.stevec1))
        label_stevec1 = Label(textvariable=self.napisi_stevec1)
        label_stevec1.grid(row=4, column=3)

        Label(text="+").grid(row=4, column=5)

        self.stevec2=randint(1,10)
        self.napisi_stevec2=StringVar(value=str(self.stevec2))
        label_stevec2 = Label(textvariable=self.napisi_stevec2)
        label_stevec2.grid(row=4, column=7)

        Label(text="=").grid(row=4, column=9)

        self.vpisi=IntVar(value=0)
        polje_vpisi=Entry(textvariable=self.vpisi)
        polje_vpisi.grid(row=4,column=11)

        gumb_preveri = Button(text="PREVERI", command=self.preveri)
        gumb_preveri.grid(row=4, column=13)

        self.prava_resitev=self.stevec1+self.stevec2
        self.napisi='Prava rešitev:  '+str(self.stevec1)+'+'+str(self.stevec2)+'='+str(self.prava_resitev)

        gumb_nov_racun = Button(text="NOV RAČUN", command=self.napisi_racun_sestevanje)
        gumb_nov_racun.grid(row=4, column=15)

#ODSTEVANJE#--------------------------------------------------------------------------------------------#ODSTEVANJE#
    def napisi_racun_odstevanje(self):
        global zablokiraj
        zablokiraj=0
        frame=Frame
        frame.pack
        
        self.stevec1=randint(1,10)
        self.napisi_stevec1=StringVar(value=str(self.stevec1))
        label_stevec1 = Label(textvariable=self.napisi_stevec1)
        label_stevec1.grid(row=6, column=3)

        Label(text="-").grid(row=6, column=5)

        self.stevec2=randint(1,10)
        self.napisi_stevec2=StringVar(value=str(self.stevec2))
        label_stevec2 = Label(textvariable=self.napisi_stevec2)
        label_stevec2.grid(row=6, column=7)

        Label(text="=").grid(row=6, column=9)

        self.vpisi=IntVar(value=0)
        polje_vpisi=Entry(textvariable=self.vpisi)
        polje_vpisi.grid(row=6,column=11)

        gumb_preveri = Button(text="PREVERI", command=self.preveri)
        gumb_preveri.grid(row=6, column=13)

        self.prava_resitev=self.stevec1-self.stevec2
        self.napisi='Prava rešitev:  '+str(self.stevec1)+'-'+str(self.stevec2)+'='+str(self.prava_resitev)

        gumb_nov_racun = Button(text="NOV RAČUN", command=self.napisi_racun_odstevanje)
        gumb_nov_racun.grid(row=6, column=15)

#MNOŽENJE#---------------------------------------------------------------------------------------------#MNOŽENJE#
    def napisi_racun_mnozenje(self):
        global zablokiraj
        zablokiraj=0
        
        frame=Frame
        frame.pack
        
        self.stevec1=randint(1,10)
        self.napisi_stevec1=StringVar(value=str(self.stevec1))
        label_stevec1 = Label(textvariable=self.napisi_stevec1)
        label_stevec1.grid(row=8, column=3)

        Label(text="·").grid(row=8, column=5)

        self.stevec2=randint(1,10)
        self.napisi_stevec2=StringVar(value=str(self.stevec2))
        label_stevec2 = Label(textvariable=self.napisi_stevec2)
        label_stevec2.grid(row=8, column=7)

        Label(text="=").grid(row=8, column=9)

        self.vpisi=IntVar(value=0)
        polje_vpisi=Entry(textvariable=self.vpisi)
        polje_vpisi.grid(row=8,column=11)

        gumb_preveri = Button(text="PREVERI", command=self.preveri)
        gumb_preveri.grid(row=8, column=13)

        self.prava_resitev=self.stevec1*self.stevec2
        self.napisi='Prava rešitev:  '+str(self.stevec1)+'·'+str(self.stevec2)+'='+str(self.prava_resitev)

        gumb_nov_racun = Button(text="NOV RAČUN", command=self.napisi_racun_mnozenje)
        gumb_nov_racun.grid(row=8, column=15)

#PREVERI#-----------------------------------------------------------------------------------------------#PREVERI#
    def preveri(self):
        global zablokiraj
        if zablokiraj!=1:
            self.tvoja_resitev="Tvoja rešitev: "+str(self.vpisi.get())
            self.seznam+=[self.napisi +'    '+ self.tvoja_resitev]
            if self.vpisi.get()==self.prava_resitev:
                self.stevec = self.stevec + 1
                self.napis_stevec.set(str(self.stevec))
                self.napisano.insert(0,str(self.napisi)+'      Tvoja rešitev: '+str(self.vpisi.get())+'   Pravilno :P')
                self.pobarvaj_krogec()
            else:
                self.stevec = self.stevec - 1
                self.napis_stevec.set(str(self.stevec))
                self.napisano.insert(0,str(self.napisi)+'      Tvoja rešitev: '+str(self.vpisi.get())+'   Narobe :(')
                self.pobarvaj_krogec2()
                
            self.koliko+=1
            self.napisi_koliko.set(str(self.koliko))
        else:
            top=Toplevel()
            sporocilo=Message(top, text='To rešitev si že preveril. Pojdi na nov račun')
            sporocilo.pack()
            gumbek=Button(top, text='Zapri', command=top.destroy)
            gumbek.pack()
            
        zablokiraj=1
        
#SHRANI#--------------------------------------------------------------------------------------------------#SHRANI#       
    def shrani(self):
        if prebrano!=1:
            ime=filedialog.asksaveasfilename()
            if ime=="":
                return
            with open(ime, "wt", encoding="utf8") as f:
                for i,j in enumerate(self.seznam):
                    f.write(str(i+1)+'.račun:'+'  '+str(j)+ '\n')
        else:
            top=Toplevel()
            sporocilo=Message(top, text='rešitve, prebrane iz datoteke ne moreš ponovno shraniti')
            sporocilo.pack()
            gumbek=Button(top, text='Zapri', command=top.destroy)
            gumbek.pack()
            

#ODPRI#-----------------------------------------------------------------------------------------------------#ODPRI#
    def odpri(self):
        global prebrano
        prebrano=1
        ime = filedialog.askopenfilename()
        if ime=="":
            return
        with open(ime, encoding='utf8') as f:
            seznam=[]
            for vrstica in f:
                novo=[]
                v=vrstica.strip().split(' ')
                racun=v[5]
                stevilka=racun.split('=')
                resitev=v[11]
                if stevilka[1]==resitev:
                    self.napisano.insert(0,'Prava rešitev:   '+str(racun)+'     Tvoja rešitev: '+str(resitev)+'  Pravilno :P')
                    self.pobarvaj_krogec()
                    self.stevec = self.stevec + 1
                    self.napis_stevec.set(str(self.stevec))
                else:
                    self.napisano.insert(0,'Prava rešitev:   '+str(racun)+'     Tvoja rešitev: '+str(resitev)+'  Narobe :(')
                    self.pobarvaj_krogec2()
                    self.stevec = self.stevec - 1
                    self.napis_stevec.set(str(self.stevec))
                self.koliko+=1
                self.napisi_koliko.set(str(self.koliko))
                

#POBARVAJ#-------------------------------------------------------------------------------------------------#POBARVAJ#
    def pobarvaj_krogec(self):
        global pravilni
        global zablokiraj
        if pravilni==15:
            for i in range(16):
                krogec=self.canvas.create_oval(10+i*30,10,30+i*30,30, fill='green')
            self.napisano.insert(0, '$$$$$$$$$$$$$$$$$ ČESTITAM!!! :D $$$$$$$$$$$$$$$$$$$$$')
            
            top=Toplevel()
            sporocilo=Message(top, text='KONEC')
            sporocilo.pack()
            gumbek=Button(top, text='Zapri', command=top.destroy)
            gumbek.pack()
            
            zablokiraj=1
        elif pravilni<16:
            krogec=self.canvas.create_oval(10+pravilni*30,10,30+pravilni*30,30, fill='BLUE')
        pravilni+=1

        
    def pobarvaj_krogec2(self):
        global napacni
        global zablokiraj
        if napacni==15:
            for i in range(16):
                krogec=self.napacni.create_oval(10+i*30,10,30+i*30,30, fill='red')
            self.napisano.insert(0, '$$$$$$$$$$$$$$$$$ OJOJOJ PONOVI IGRO IN SE KAJ NAUČI $$$$$$$$$$$$$$$$$$$$$')
            
            top=Toplevel()
            sporocilo=Message(top, text='KONEC')
            sporocilo.pack()
            gumbek=Button(top, text='Zapri', command=top.destroy)
            gumbek.pack()
            
            zablokiraj=1
            
        elif napacni<16:
            krogec=self.napacni.create_oval(10+napacni*30,10,30+napacni*30,30, fill='ORANGE')
        napacni+=1

#RESTART#---------------------------------------------------------------------------------------------"RESTART#
    def restart(self):
        global napacni
        global pravilni
        global zablokiraj
        global prebrano

        zablokiraj=0
        pravilni=0
        napacni=0
        prebrano=0

        self.koliko=0
        self.napisi_koliko.set(str(self.koliko))
        self.stevec=0
        self.napis_stevec.set(str(self.stevec))
        
        self.canvas.delete("all")
        self.napacni.delete("all")
        
        self.canvas=Canvas(width=550, height=40)
        self.canvas.grid(row = 19,rowspan = 2, column = 0, columnspan = 18,sticky=E+W+N+S)
        for i in range(16):
            krogec=self.canvas.create_oval(10+i*30,10,30+i*30,30)
            
        self.napacni=Canvas(width=550, height=40)
        self.napacni.grid(row = 21,rowspan = 2, column = 0, columnspan = 18,sticky=E+W+N+S)
        for i in range(16):
            krogec=self.napacni.create_oval(10+i*30,10,30+i*30,30)

        self.napisano = Listbox(selectmode=SINGLE)
        self.napisano.grid(row = 12,rowspan = 2, column = 0, columnspan = 25,sticky=E+W+N+S)

        self.seznam=[]
        
    
root=Tk()
aplikacija=sestevanje(root)
root.mainloop()
