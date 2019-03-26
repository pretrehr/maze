from random import *
from turtle import *
from time import *
from copy import copy,deepcopy


def affichator(n):
    l= [[[0 for k in range (4)] for ù in range(n)] for _ in range(n)]
    for i in range(n):
        print(l[i])


def ouverture(l,x,y):
    if x>=0 and y>=0:
        try:
            return l[x][y]==[0,0,0,0]
        except IndexError:
            return False 
    else:
        return False

    #en dehors limite laby=out of range try except
def path(n):
    # nord ouest sud est
    # creation laby
    l=[[[0 for k in range (4)] for ù in range(n)] for _ in range(n)]
    #coordonnées case de départ + liste chemin(sens) 
    x=n//2 #randint(0,n-1)
    y=n//2 #randint(0,n-1)
    i=0
    i2=0
    chemin=[[y,x]]
    #ouverture case
    while len(chemin)<(n*n):
        ls=[0,1,2,3]
        x2=x
        y2=y
        while ls!=[]:
            s=choice(ls)
            if s==0:
                if ouverture(l,y-1,x):
                    l[y][x][s]=1
                    y-=1
                    chemin+=[[y,x]]
                    l[y][x][2]=1
                    ls=[]
                else:
                    ls.remove(0)
            elif s==1:
                if ouverture(l,y,x-1):
                    l[y][x][s]=1
                    x-=1
                    chemin+=[[y,x]]
                    l[y][x][3]=1
                    ls=[]
                else:
                    ls.remove(1)
            elif s==2:
                if ouverture(l,y+1,x):
                    l[y][x][s]=1
                    y+=1
                    chemin+=[[y,x]]
                    l[y][x][0]=1
                    ls=[]
                else:
                    ls.remove(2)
            else:
                if ouverture(l,y,x+1):
                    l[y][x][s]=1
                    x+=1
                    chemin+=[[y,x]]
                    l[y][x][1]=1
                    ls=[]
                else:
                    ls.remove(3)
        if y==y2 and x==x2:
            y=chemin[i2-1][0]
            x=chemin[i2-1][1]
            i2-=1
        else:
            i+=1
            i2=i
    l[0][0][1]=1
    l[n-1][n-1][3]=1
    #for z in range(n):
      #print(l[z])
    return l
        

def dessinator(L,s=15):
    reset()
    a=time()
    up()
    setpos(-680,350)
    down()
    speed("fastest")
    setheading(0)
    for k in range(len(L)):
        for i in range(len(L)):
            for j in range(4):
                if L[k][i][-j]==0:
                    down()
                else:
                    up()
                forward(s)
                right(90)
            up()
            forward(s)
        backward(len(L)*s)
        right(90)
        forward(s)        
        left(90)     
    hideturtle()
    print(time()-a)


def dessinator2(L,s=15):
    reset()
    a=time()
    setheading(0)
    for k in range(len(L)):
        up()
        goto(-680,350-s*k)
        for i in range(len(L)):
            if L[k][i][0]==0:
                down()
            else:
                up()
            forward(s)
    up()
    goto(-680,350-s*len(L))
    for i in range(len(L)):
            if L[len(L)-1][i][2]==0:
                down()
            else:
                up()
            forward(s)
    setheading(-90)
    for i in range(len(L)):
        up()
        goto(-680+s*i,350)
        for k in range(len(L)):
            if L[k][i][1]==0:
                down()
            else:
                up()
            forward(s)
    up()
    goto(-680+s*len(L),350)
    for i in range(len(L)):
            if L[i][len(L)-1][-1]==0:
                down()
            else:
                up()
            forward(s)
    hideturtle()
    print(time()-a)


def dessinator3(L,s=15):
    a=time()
    reset()
    n=len(L)
    up()
    setpos(-680,350)
    for t in range(n//2):
        setheading(0)
        for i in range(n):
            if L[2*t][i][0]==0:
                down()
            else:
                up()
            forward(s)
        right(90)
        up()
        forward(s)
        down()
        setheading(0)
        for i in range(n):
            if L[2*t+1][-i-1][0]==0:
                down()
            else:
                up()
            backward(s)
        right(90)
        up()
        forward(s)
        down()
        setheading(0)
    if n%2!=0:
        for i in range(n):
            if L[n-1][i][0]==0:
                down()
            else:
                up()
            forward(s)
        right(90)
        up()
        forward(s)
        down()
        setheading(0)
        for i in range(n):
            if L[n-1][-i-1][2]==0:
                down()
            else:
                up()
            backward(s)
    else:
        for i in range(n):
            if L[n-1][i][2]==0:
                down()
            else:
                up()
            forward(s)
    up()
    setpos(-680,350)
    for t in range(n//2):
        setheading(-90)
        for i in range(n):
            if L[i][2*t][1]==0:
                down()
            else:
                up()
            forward(s)
        left(90)
        up()
        forward(s)
        down()
        setheading(-90)
        for i in range(n):
            if L[-i-1][2*t+1][1]==0:
                down()
            else:
                up()
            backward(s)
        left(90)
        up()
        forward(s)
        down()
        setheading(-90)
    if n%2!=0:
        for i in range(n):
            if L[i][n-1][1]==0:
                down()
            else:
                up()
            forward(s)
        left(90)
        up()
        forward(s)
        down()
        setheading(-90)
        for i in range(n):
            if L[-i-1][n-1][-1]==0:
                down()
            else:
                up()
            backward(s)
    else:
        for i in range(n):
            if L[i][n-1][-1]==0:
                down()
            else:
                up()
            forward(s)
    hideturtle()
    print(time()-a)


def dessinator2bis(L,s=15):
    reset()
    a=time()
    setheading(0)
    for k in range(len(L)):
        up()
        goto(-100,100-s*k)
        for i in range(len(L)):
            if L[k][i][0]==0:
                down()
            else:
                up()
            forward(s)
    up()
    goto(-100,100-s*len(L))
    for i in range(len(L)):
            if L[len(L)-1][i][2]==0:
                down()
            else:
                up()
            forward(s)
    setheading(-90)
    for i in range(len(L)):
        up()
        goto(-100+s*i,100)
        for k in range(len(L)):
            if L[k][i][1]==0:
                down()
            else:
                up()
            forward(s)
    up()
    goto(-100+s*len(L),100)
    for i in range(len(L)):
            if L[i][len(L)-1][-1]==0:
                down()
            else:
                up()
            forward(s)
    hideturtle()
    print(time()-a)

def dessinator3bis(L,s=15):
    a=time()
    reset()
    n=len(L)
    up()
    setpos(-650,300)
    for t in range(n//2):
        setheading(0)
        for i in range(n):
            if L[2*t][i][0]==0:
                down()
            else:
                up()
            forward(s)
        right(90)
        up()
        forward(s)
        down()
        setheading(0)
        for i in range(n):
            if L[2*t+1][-i-1][0]==0:
                down()
            else:
                up()
            backward(s)
        right(90)
        up()
        forward(s)
        down()
        setheading(0)
    if n%2!=0:
        for i in range(n):
            if L[n-1][i][0]==0:
                down()
            else:
                up()
            forward(s)
        right(90)
        up()
        forward(s)
        down()
        setheading(0)
        for i in range(n):
            if L[n-1][-i-1][2]==0:
                down()
            else:
                up()
            backward(s)
    else:
        for i in range(n):
            if L[n-1][i][2]==0:
                down()
            else:
                up()
            forward(s)
    up()
    setpos(-650,300)
    for t in range(n//2):
        setheading(-90)
        for i in range(n):
            if L[i][2*t][1]==0:
                down()
            else:
                up()
            forward(s)
        left(90)
        up()
        forward(s)
        down()
        setheading(-90)
        for i in range(n):
            if L[-i-1][2*t+1][1]==0:
                down()
            else:
                up()
            backward(s)
        left(90)
        up()
        forward(s)
        down()
        setheading(-90)
    if n%2!=0:
        for i in range(n):
            if L[i][n-1][1]==0:
                down()
            else:
                up()
            forward(s)
        left(90)
        up()
        forward(s)
        down()
        setheading(-90)
        for i in range(n):
            if L[-i-1][n-1][-1]==0:
                down()
            else:
                up()
            backward(s)
    else:
        for i in range(n):
            if L[i][n-1][-1]==0:
                down()
            else:
                up()
            forward(s)
    hideturtle()
    print(time()-a)


def dessinator4bis(L,s=15,murs_épais=False):
    title("Labyrinthe")
    a=time()
    reset()
    up()
    setpos(-650+s,300)
    color(0,1,0)
    if murs_épais:
        width(s/2)
    n=len(L)
    down()
    begin_fill()
    right(90)
    forward(s)
    right(90)
    forward(s)
    right(90)
    forward(s)
    right(90)
    forward(s)
    end_fill()
    up()
    setpos(-650+(n-1)*s,300-n*s)
    setheading(-90)
    down()
    color("red")
    begin_fill()
    left(90)
    forward(s)
    left(90)
    forward(s)
    left(90)
    forward(s)
    left(90)
    forward(s)
    end_fill()
    up()
    setpos(-650,300)
    down()
    color("black")
    for t in range(n//2):
        setheading(0)
        for i in range(n):
            if L[2*t][i][0]==0:
                down()
            else:
                up()
            forward(s)
        up()
        setpos(xcor(),ycor()-s)
        for i in range(n):
            if L[2*t+1][-i-1][0]==0:
                down()
            else:
                up()
            backward(s)
        up()
        setpos(xcor(),ycor()-s)
    if n%2!=0:
        for i in range(n):
            if L[n-1][i][0]==0:
                down()
            else:
                up()
            forward(s)
        up()
        setpos(xcor(),ycor()-s)
        for i in range(n):
            if L[n-1][-i-1][2]==0:
                down()
            else:
                up()
            backward(s)
    else:
        for i in range(n):
            if L[n-1][i][2]==0:
                down()
            else:
                up()
            forward(s)
    up()
    setpos(-650,300)
    for t in range(n//2):
        setheading(-90)
        for i in range(n):
            if L[i][2*t][1]==0:
                down()
            else:
                up()
            forward(s)
        up()
        setpos(xcor()+s,ycor())
        for i in range(n):
            if L[-i-1][2*t+1][1]==0:
                down()
            else:
                up()
            backward(s)
        up()
        setpos(xcor()+s,ycor())
    if n%2!=0:
        for i in range(n):
            if L[i][n-1][1]==0:
                down()
            else:
                up()
            forward(s)
        up()
        setpos(xcor()+s,ycor())
        for i in range(n):
            if L[-i-1][n-1][-1]==0:
                down()
            else:
                up()
            backward(s)
    else:
        for i in range(n):
            if L[i][n-1][-1]==0:
                down()
            else:
                up()
            forward(s)
    hideturtle()
    print(time()-a)


def ouverture2(L,y,x,j): #renvoie True si cul-de-sac sachant qu'on vient de la direction indiquée par j
    l=copie_liste(L)
    l[y][x][j]=0
    if x>=0 and y>=0:
        try:
            return l[y][x]==[0,0,0,0]
        except IndexError:
            return False 
    else:
        return False


def ouv2(L,y,x,j): #une autre variante
    l=[x for x in L]
    ls=[0,1,2,3]
    ls.remove(j)
    if x>=0 and y>=0:
        try:
            cul_de_sac=True
            a=0
            while cul_de_sac and a<3:
                if l[y][x][ls[a]]==0:
                    a+=1
                else:
                    cul_de_sac=False
            return cul_de_sac
        except IndexError:
            return False
    else:
        return False


def copie_liste(L): #pour copier une matrice "proprement"
    l=deepcopy(L) 
    return l


def resolutor(l):
    t=time()
    L=copie_liste(l)
    L[0][0][1]=0
    L[len(l)-1][len(l[0])-1][3]=0
    chemin=[[0,0]]
    visite=[[0,0]]
    valeurs=[3]
    i=0
    j=3
    x=0
    y=0
    while chemin[i]!=[len(L)-1,len(L[0])-1]:
        ls=[0,1,2,3]
        j=(j-2)%4 #direction d'où on vient par rapport à la case actuelle
        #print(j)
        if (not ouverture2(L,y,x,j)):
            ls.remove(j)
            a=0
            non_atteint=True
            while non_atteint:
                if L[y][x][ls[a]]==0:
                    a+=1
                else:
                    non_atteint=False
                    j=ls[a]
            if j==0:
                y-=1
            elif j==1:
                x-=1
            elif j==2:
                y+=1
            else:
                x+=1
            chemin+=[[y,x]]
            visite+=[[y,x]]
            i+=1
            valeurs.append(j)
            #print(j) #direction où on va par rapport à la case actuelle
        else:
            #print("cul-de-sac")
            L[y][x][j]=0
            #print(y,x)
            chemin.remove([y,x])
            del valeurs[i]
            i-=1
            if j==0:
                y-=1
            elif j==1:
                x-=1
            elif j==2:
                y+=1
            else:
                x+=1
            L[y][x][j-2]=0
            j=valeurs[i]
            #print(y,x)
        #print(chemin,visite,valeurs)
        #print("")
    print(time()-t)
    L[0][0][1]=1
    L[len(l)-1][len(l[0])-1][3]=1
    return valeurs


#couleurs:
red=(1,0,0)
green=(0,1,0)
blue=(0,0,1)
magenta=(1,0,1)
cyan=(0,1,1)
yellow=(1,1,0)
orange=(1,.5,0)
light_green=(.5,1,0)
dark_green=(0,.5,0)
grey=(.5,.5,.5)
purple=(.5,0,.5)
pink=(1,.5,1)
gold=(1,215/256,0)
silver=(206/256,206/256,206/256)
bronze=(97/256,78/256,26/256)
dark_blue=(0,0,.5)
brown=(.5,.25,0)
jade=(135/256,233/256,144/256)


def solutionator(l,x,y,couleur,épaisseur=15,murs_épais=False):
    a=time()
    color(couleur)
    up()
    setpos(x+épaisseur/2,y-épaisseur/2)
    setheading(0)
    width(épaisseur-1)
    if murs_épais:
        setpos(x+(épaisseur-1)/2,y-(épaisseur-1)/2)
        width((épaisseur-1)/2)
    down()
    for i in range(1,len(l)):
        setheading((l[i]-3)*90) #0:90° 1:180° 2:270° 3:0°
        forward(épaisseur)
    print(time()-a)

def solutionator2(l,x0,y0,couleur,épaisseur=15,murs_épais=False):
    a=time()
    color(couleur)
    up()
    setpos(x0+épaisseur/2,y0-épaisseur/2)
    x=x0+épaisseur/2
    y=y0-épaisseur/2
    setheading(0)
    width(épaisseur-1)
    if murs_épais:
        setpos(x0+(épaisseur-1)/2,y0-(épaisseur-1)/2)
        width((épaisseur-1)/2)
        x=x0+(épaisseur-1)/2
        y=y0-(épaisseur-1)/2
    down()
    for i in range(1,len(l)):
        if l[i]==0:
            y+=épaisseur
        elif l[i]==1:
            x-=épaisseur
        elif l[i]==2:
            y-=épaisseur
        else:
            x+=épaisseur
        setpos(x,y)
    print(time()-a)

def algorithme_final(n,s,couleur=gold,murs_épais=False):
    l=path(n)
    dessinator4bis(l,s,murs_épais)
    L=resolutor(l)
    input("Appuyez sur ENTRÉE pour continuer ce programme...")
    solutionator2(L,-650,300,couleur,s,murs_épais)

def pathrector(n,m): #O(n²) m hauteur n longueur
    # nord ouest sud est
    # creation laby
    l=[[[0 for k in range (4)] for ù in range(n)] for _ in range(m)]
    #coordonnées case de départ + liste chemin(sens) 
    x=n//2 #randint(0,n-1)
    y=m//2 #randint(0,m-1)
    i=0
    i2=0
    chemin=[[y,x]]
    #ouverture case
    while len(chemin)<(n*m):
        ls=[0,1,2,3]
        x2=x
        y2=y
        while ls!=[]:
            s=choice(ls)
            if s==0:
                if ouverture(l,y-1,x):
                    l[y][x][s]=1
                    y-=1
                    chemin+=[[y,x]]
                    l[y][x][2]=1
                    ls=[]
                else:
                    ls.remove(0)
            elif s==1:
                if ouverture(l,y,x-1):
                    l[y][x][s]=1
                    x-=1
                    chemin+=[[y,x]]
                    l[y][x][3]=1
                    ls=[]
                else:
                    ls.remove(1)
            elif s==2:
                if ouverture(l,y+1,x):
                    l[y][x][s]=1
                    y+=1
                    chemin+=[[y,x]]
                    l[y][x][0]=1
                    ls=[]
                else:
                    ls.remove(2)
            else:
                if ouverture(l,y,x+1):
                    l[y][x][s]=1
                    x+=1
                    chemin+=[[y,x]]
                    l[y][x][1]=1
                    ls=[]
                else:
                    ls.remove(3)
        if y==y2 and x==x2:
            y=chemin[i2-1][0]
            x=chemin[i2-1][1]
            i2-=1
        else:
            i+=1
            i2=i
    l[0][0][1]=1
    l[m-1][n-1][3]=1
    #for z in range(n):
      #print(l[z])
    return l


def dessinator4ter(L,s=15,murs_épais=False):
    title("Labyrinthe")
    a=time()
    reset()
    up()
    setpos(-650+s,300)
    color(0,1,0)
    if murs_épais:
        width(s/2)
    n=len(L)
    m=len(L[0])
    down()
    hideturtle()
    begin_fill()
    right(90)
    forward(s)
    right(90)
    forward(s)
    right(90)
    forward(s)
    right(90)
    forward(s)
    end_fill()
    up()
    setpos(-650+(m-1)*s,300-n*s)
    setheading(-90)
    down()
    color("red")
    begin_fill()
    left(90)
    forward(s)
    left(90)
    forward(s)
    left(90)
    forward(s)
    left(90)
    forward(s)
    end_fill()
    up()
    setpos(-650,300)
    down()
    color("black")
    for t in range(n//2):
        setheading(0)
        for i in range(m):
            if L[2*t][i][0]==0:
                down()
            else:
                up()
            forward(s)
        up()
        setpos(xcor(),ycor()-s)
        for i in range(m):
            if L[2*t+1][-i-1][0]==0:
                down()
            else:
                up()
            backward(s)
        up()
        setpos(xcor(),ycor()-s)
    if n%2!=0:
        for i in range(m):
            if L[n-1][i][0]==0:
                down()
            else:
                up()
            forward(s)
        up()
        setpos(xcor(),ycor()-s)
        for i in range(m):
            if L[n-1][-i-1][2]==0:
                down()
            else:
                up()
            backward(s)
    else:
        for i in range(m):
            if L[n-1][i][2]==0:
                down()
            else:
                up()
            forward(s)
    up()
    setpos(-650,300)
    for t in range(m//2):
        setheading(-90)
        for i in range(n):
            if L[i][2*t][1]==0:
                down()
            else:
                up()
            forward(s)
        up()
        setpos(xcor()+s,ycor())
        for i in range(n):
            if L[-i-1][2*t+1][1]==0:
                down()
            else:
                up()
            backward(s)
        up()
        setpos(xcor()+s,ycor())
    if m%2!=0:
        for i in range(n):
            if L[i][m-1][1]==0:
                down()
            else:
                up()
            forward(s)
        up()
        setpos(xcor()+s,ycor())
        for i in range(n):
            if L[-i-1][m-1][-1]==0:
                down()
            else:
                up()
            backward(s)
    else:
        for i in range(n):
            if L[i][m-1][-1]==0:
                down()
            else:
                up()
            forward(s)
    hideturtle()
    print(time()-a)

def algorithme_final2(l,s,couleur=gold,murs_épais=False):
    dessinator4ter(l,s,murs_épais)
    L=resolutor(l)
    input("Appuyez sur ENTRÉE pour continuer ce programme...")
    solutionator2(L,-650,300,couleur,s,murs_épais)