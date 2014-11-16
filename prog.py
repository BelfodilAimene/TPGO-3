VILLEA="A"
VILLEB="B"
STATION="Station_"

LSTANDARD=[10,20,5,17,28,30,29,10]
MaxPlein=38

def AfficherStations(Liste=LSTANDARD) :
    if (len(Liste)>0) :
        print VILLEA," -> ",
        print Liste[0]," -> ",
        for i in range(1,len(Liste)) :
            print STATION+str(i)," -> ",
            print Liste[i]," -> ",
        print VILLEB
            

def getMinMaxPlein(Liste=LSTANDARD) :
    return max(Liste)

def getStations(MaxPlein=max(LSTANDARD),Liste=LSTANDARD) :
    if (len(Liste)<1 or MaxPlein<getMinMaxPlein(Liste)) :
        return "Impossible"
    else :
        L = []
        D=MaxPlein
        D-=Liste[0]
        for i in range(1,len(Liste)) :
            if (D<Liste[i]) :
                L.append(STATION+str(i))
                D=MaxPlein
            D-=Liste[i]
        return L
            




AfficherStations(LSTANDARD)
print "Plein : ",MaxPlein
print getStations(MaxPlein,LSTANDARD)
