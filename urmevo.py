import sys
sys.set_int_max_str_digits(0)
class URM():
    def __init__(self, registro, codice):
        self.registro = registro +([0]*10) if isinstance(registro,list) else []
        self.codice= codice if isinstance(codice,list) else[]
    def run(self):
        if self.registro:
            ist=0

            Beta=[]
            while ist < len(self.codice):
                for istruzione in self.codice[ist:]:
                    (comando, parametri)= istruzione #mette nella prima variabile comando, nella seconda il parametro
                    print(self.registro[0:5])
                    match comando:
                        case 'Z':
                            Beta.append(4*(parametri))
                            self.registro[parametri]=0
                            ist=ist+1
                        case 'S':
                            Beta.append(4*(parametri)+1)
                            self.registro[parametri]=self.registro[parametri]+1
                            ist=ist+1
                        case 'T':
                            (sorgente, destinazione)= parametri
                            Beta.append((4*((((2**sorgente) *(2*destinazione+1))-1 )))+2)
                            self.registro[destinazione]= self.registro[sorgente]
                            ist=ist+1
                        case 'J':
                            (sorgente, destinazione, salto)=parametri
                            primotermine=(2**sorgente) *(2*destinazione+1)-1
                            Beta.append((2**primotermine)*(2*salto+1)-1)
                            if self.registro[sorgente]==self.registro[destinazione]:
                                ist=self.registro[salto+1]
                                break
                            else:
                                ist=ist+1
            print(Beta)
            betalen=len(Beta)
            ncomputabili=0
            contatorebeta=0
            for x in range(len(Beta)):
                if x == 0:
                    ncomputabili=ncomputabili+(2**Beta[0])
                else:
                    ncomputabili=ncomputabili+(2**(sum(Beta[0:x])+1))

            print("funzioni n computabili ", ncomputabili)





#registro=[9,7]

#pagina 76 valore di ghale
a=URM([9,7],[['Z',(3)],['S', (3)], ['T',(3,0)], ['J',(1,2,1)], ['Z', (5)]])
a.run()
