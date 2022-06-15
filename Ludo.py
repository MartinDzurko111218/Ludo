import random


def prazdne_pole(n,medzera): #v jednom poli vytvara n prazdnych poli
    pp=[]
    for i in range(n):
        pp.append(n*[medzera])
    return pp


plocha=[] #urcenie si prazdneho pola do ktoreho priradime vzhlad plochy
def hracia_plocha(n):
    plocha=prazdne_pole(n, " ")
    for i in range(int((n/2)-1),int((n/2)+2)): #horne 3 hviezdicky
        plocha[0][i]="*"
    for i in range(1,int((n/2)-1)): #vertikalne horne domceky
        plocha[i][int((n/2)-1)]="*"
        plocha[i][int(n/2)]="D"
        plocha[i][int((n/2)+1)]="*"
    for i in range(int((n/2))): #horna horizontalna cast
        plocha[int((n/2)-1)][i]="*"
    plocha[int((n/2)-1)][int(n/2)]="D"
    for i in range(int((n/2)+1),n):
        plocha[int((n/2)-1)][i]="*" #koniec HHC
    plocha[int(n/2)][0]="*" #stred horizontalnej casti
    for i in range(1,int((n/2))):
        plocha[int(n/2)][i]="D"
    plocha[int(n/2)][int(n/2)]="X"
    for i in range(int(n/2)+1,n-1):
        plocha[int(n/2)][i]="D"
    plocha[int(n/2)][n-1]="*" # koniec SHC
    for i in range(int(n/2)): #dolna horizontalna cast
        plocha[int((n/2)+1)][i]="*"
    plocha[int((n/2)+1)][int(n/2)]="D"
    for i in range(int((n/2)+1),n):
        plocha[int((n/2)+1)][i]="*" #koniec DHC
    for i in range(int((n/2)+2),n-1): #vertikalne spodne domceky
        plocha[i][int((n/2)-1)]="*"
        plocha[i][int(n/2)]="D"
        plocha[i][int((n/2)+1)]="*"
    for i in range(int((n/2)-1),int((n/2)+2)): #spodne 3 hviezdicky
        plocha[n-1][i]="*"
    return plocha


def vypis_plochy(pole): #funkcia printuje vytvorenu plochu
    for riadok in range(len(pole)):
        for stlpec in range(len(pole[riadok])):
            print(pole[riadok][stlpec], end=" ")
        print()


def p_pole_pohybu(n): #definuje prazdne pole pohybu podla rozmeru n
    ppp=[]
    for i in range (int(((4*n)-4)+((n-3)/2))):
        ppp.append(2*[" "])
    return ppp


cestaA=[]  #urcenie prazdneho pola suradnic pohybu A 
def pohybA(n): #zapisovanie suradnic pohybu panacika A
    cestaA=p_pole_pohybu(n)
    for i in range(int((n/2))):
        cestaA[i][0]=i
        cestaA[i][1]=int((n/2)+1)
    s=int((n/2)+2)
    for i in range(int(n/2),int((2*n-3)/2)):  
        cestaA[i][0]=int((n/2)-1) 
        cestaA[i][1]=s
        s=s+1
    cestaA[int((2*n-3)/2)][0]=int(n/2)
    cestaA[int((2*n-3)/2)][1]=n-1
    s=n-1
    for i in range(int(((2*n-3)/2)+1),int((3*n-3)/2)): 
        cestaA[i][0]=int((n/2)+1)
        cestaA[i][1]=s      
        s=s-1
    r=int((n/2)+1)+1
    for i in range(int((3*n-3)/2),int(2*n-3)): 
        cestaA[i][0]=r 
        cestaA[i][1]=int((n/2+1))
        r=r+1    
    cestaA[int(2*n-3)][0]=n-1
    cestaA[int(2*n-3)][1]=int(n/2)
    r=n-1
    for i in range(int((2*n-3)+1),int((5*n-4)/2)):
        cestaA[i][0]=r
        cestaA[i][1]=int((n/2)-1)
        r=r-1
    s=int((n/2)-1)-1
    for i in range(int((5*n-4)/2),int((6*n-7)/2)):
        cestaA[i][0]=int((n/2)+1)
        cestaA[i][1]=s
        s=s-1
    cestaA[int((6*n-7)/2)][0]=int(n/2)
    cestaA[int((6*n-7)/2)][1]=0
    s=0
    for i in range(int((6*n-7)/2)+1,int(((7*n-7)/2))):
        cestaA[i][0]=int((n/2)-1)
        cestaA[i][1]=s
        s=s+1
    r=int((n/2)-1)-1
    for i in range(int(((7*n-7)/2)),int(4*n-5)):
        cestaA[i][0]=r
        cestaA[i][1]=int((n/2)-1)
        r=r-1
    cestaA[int(4*n-5)][0]=0
    cestaA[int(4*n-5)][1]=int(n/2)
    r=1
    for i in range(int(4*n-5)+1,len(cestaA)):
        cestaA[i][0]=r
        cestaA[i][1]=int(n/2)
        r=r+1
    return cestaA


cestaB=[]  #urcenie prazdneho pola suradnic pohybu B 
def pohybB(n): #zapisovanie suradnic pohybu panacika B
    cestaB=p_pole_pohybu(n)
    r=n-1
    for i in range(int(n/2)):
        cestaB[i][0]=r
        cestaB[i][1]=int((n/2)-1)
        r=r-1
    s=int((n/2)-2)
    for i in range(int(n/2),int((2*n-3)/2)):
        cestaB[i][0]=int((n/2)+1)
        cestaB[i][1]=s
        s=s-1 
    cestaB[int((2*n-3)/2)][0]=int(n/2) 
    cestaB[int((2*n-3)/2)][1]=0
    s=0
    for i in range(int(((2*n-3)/2)+1),int((3*n-3)/2)):   
        cestaB[i][0]=int((n/2)-1)
        cestaB[i][1]=s
        s=s+1
    r=int((n/2)-1)
    for i in range(int((3*n-3)/2-1),int(2*n-3)):   
        cestaB[i][0]=r
        cestaB[i][1]=int((n/2)-1)
        r=r-1
    cestaB[int(2*n-3)][0]=0
    cestaB[int(2*n-3)][1]=int(n/2)
    r=0    
    for i in range(int((2*n-3)+1),int((5*n-4)/2)):   
        cestaB[i][0]=r
        cestaB[i][1]=int((n/2)+1)
        r=r+1
    s=int((n/2)+2)
    for i in range(int((5*n-4)/2),int((6*n-7)/2)):
        cestaB[i][0]=int((n/2)-1)
        cestaB[i][1]=s
        s=s+1
    cestaB[int((6*n-7)/2)][0]=int(n/2)
    cestaB[int((6*n-7)/2)][1]=n-1
    s=n-1
    for i in range(int((6*n-7)/2)+1,int(((7*n-7)/2))):
        cestaB[i][0]=int((n/2)+1)
        cestaB[i][1]=s
        s=s-1
    r=int((n/2)+2)
    for i in range(int(((7*n-7)/2)),int(4*n-5)):
        cestaB[i][0]=r
        cestaB[i][1]=int((n/2)+1)
        r=r+1
    cestaB[int(4*n-5)][0]=n-1
    cestaB[int(4*n-5)][1]=int(n/2)
    r=n-2
    for i in range(int(4*n-5)+1,len(cestaB)):
        cestaB[i][0]=r
        cestaB[i][1]=int(n/2)
        r=r-1
    return cestaB


def hod_kockou(): #generuje random cislo od 1 do 6
    hod=random.randint(1,6)
    return hod


# V tejto casti priamo zacina simulacia dvoch panacikov
n=int(input("Zadaj nepárne číslo: "))
while n%2!=1 or n<5:
    n=int(input("Nesprávne. Zadaj nepárne číslo väčšie/rovné ako 5: "))
vypis_plochy(hracia_plocha(n))
plocha=hracia_plocha(n)
pohybA=pohybA(n)
pohybB=pohybB(n)
pA=0
pB=0
hodA=hod_kockou()
hodB=hod_kockou()

while hodA!=6:
    print("Hrac A hodil cislo ",hodA,", hadze znova")
    hodA=hod_kockou()
print("Hrac A hodil cislo 6  a stavia sa na startovnu poziciu")
plocha[pohybA[0][0]][pohybA[0][1]]="A"
vypis_plochy(plocha)
while hodB!=6:
    print( "Hrac B hodil cislo",hodB,", hadze znova")
    hodB=hod_kockou()
print("Hrac B hodil cislo 6 a stavia sa na startovnu poziciu")
plocha[pohybB[0][0]][pohybB[0][1]]="B"
vypis_plochy(plocha)

while pA not in range((len(pohybA)-int((n-3)/2)),len(pohybA)) or pB not in range((len(pohybB)-int((n-3)/2)),len(pohybB)):
    plocha=hracia_plocha(n)
    hodA=hod_kockou()
    hodB=hod_kockou()
    if pA in range((len(pohybA)-int((n-3)/2)),len(pohybA)):
        break
    elif pB in range(len(pohybB)-int((n-3)/2),len(pohybB)):
        break
    else:
        if hodA!=6:
            pA=pA+hodA
            if pA>len(pohybA)-1:
                print("Hrac A hodil prilis velke cislo, ",hodA,", a nemoze sa dostat do domceka")
                pA=pA-hodA
                plocha[pohybA[pA][0]][pohybA[pA][1]]="A"
            else: 
                print("Hrac A hodil ",hodA)
                plocha[pohybA[pA][0]][pohybA[pA][1]]="A"
        else:
            hodA1=hodA
            hodA2=hod_kockou()
            pA=pA+hodA1+hodA2
            print("Hrac A hodil ",hodA1," a ",hodA2)
            if pA>len(pohybA)-1:
                print("Hrac A hodil prilis velke cislo a nemoze sa dostat do domceka")
                pA=pA-hodA1-hodA2
                plocha[pohybA[pA][0]][pohybA[pA][1]]="A"
            else: 
                plocha[pohybA[pA][0]][pohybA[pA][1]]="A"
        if pA in range((len(pohybA)-int((n-3)/2)),len(pohybA)):
            plocha[pohybB[pB][0]][pohybB[pB][1]]="B"
            vypis_plochy(plocha)
            break
        if hodB!=6:
            pB=pB+hodB
            if pB>len(pohybB)-1:
                print("Hrac B hodil prilis velke cislo,",hodB,", a nemoze sa dostat do domceka")
                pB=pB-hodB
                plocha[pohybB[pB][0]][pohybB[pB][1]]="B"
            else:
                print("Hrac B hodil ",hodB)
                plocha[pohybB[pB][0]][pohybB[pB][1]]="B"
        else:
            hodB1=hodB
            hodB2=hod_kockou()
            pB=pB+hodB1+hodB2
            print("Hrac B hodil ",hodB1," a ",hodB2)
            if pB>len(pohybB)-1:
                print("Hrac B hodil prilis velke cislo a nemoze sa dostat do domceka")
                pB=pB-hodB1-hodB2
                plocha[pohybB[pB][0]][pohybB[pB][1]]="B"
            else:
                plocha[pohybB[pB][0]][pohybB[pB][1]]="B"
    vypis_plochy(plocha)
if pA in range(len(pohybA)-int((n-3)/2),len(pohybA)):
    print("Hrac A vyhral!")
else: print("Hrac B vyhral!")

