import socket
import marshal
UDP_IP = "10.160.108.93"
UDP_PORT = 5050
BateauPlace=0
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
Message=("Connexion")



BN=[['*','A','B','C','D','E',"F","G","H","I","J"],['0','-','-','-','-','-','-','-','-','-','-'],['1','-','-','-','-','-','-','-','-','-','-'],['2','-','-','-','-','-','-','-','-','-','-'],
    ['3','-','-','-','-','-','-','-','-','-','-'],['4','-','-','-','-','-','-','-','-','-','-'],['5','-','-','-','-','-','-','-','-','-','-'],['6','-','-','-','-','-','-','-','-','-','-'],
    ['7','-','-','-','-','-','-','-','-','-','-'],['8','-','-','-','-','-','-','-','-','-','-'],['9','-','-','-','-','-','-','-','-','-','-']]     #Creation du tableau de jeu
idx=True

def Afficher():     #Creation de la fonction Afficher()
    tab = ""       #Actualisation du jeu
    for i in range(11):
        tab = "| "
        for j in range (11):        #Mise en forme du jeu
            tab += BN[i][j]
            tab += " | "
        print(tab)     #Affiche le jeu

print("En attente de connexion d'un autre joueur \n")
data, addr = sock.recvfrom(1024)
sock.sendto(Message.encode(),addr)
if (addr!=""):
    print("--  Joueur 2 en ligne -- \n")
    
    print("***  Lancement de la partie *** \n")

    
    while (BateauPlace==0):
        j1=input("Entre le sens et la position du bateau (ex:vA1):  ")
        
        if (j1[1]=="A" or j1[1]=="a"):
            BN[int(j1[2])+1][1]="O"
            if (j1[0]=="V" or j1[0]=="v"):
                if ((int(j1[2])+1)<7):
                    BN[int(j1[2])+2][1]="O"
                    BN[int(j1[2])+3][1]="O"
                    BateauPlace=1
            elif (j1[0]=="H" or j1[0]=="h"):
                BN[int(j1[2])+1][2]="O"
                BN[int(j1[2])+1][3]="O"
                BateauPlace=1
        if (j1[1]=="B" or j1[1]=="b"):
            BN[int(j1[2])+1][2]="O"
            if (j1[0]=="V" or j1[0]=="v"):
                if ((int(j1[2])+1)<7):
                    BN[int(j1[2])+2][2]="O"
                    BN[int(j1[2])+3][2]="O"
                    BateauPlace=1
            elif (j1[0]=="H" or j1[0]=="h"):
                BN[int(j1[2])+1][3]="O"
                BN[int(j1[2])+1][4]="O"
                BateauPlace=1
        if (j1[1]=="C" or j1[1]=="c"):
            BN[int(j1[2])+1][3]="O"
            if (j1[0]=="V" or j1[0]=="v"):
                if ((int(j1[2])+1)<7):
                    BN[int(j1[2])+2][3]="O"
                    BN[int(j1[2])+3][3]="O"
                    BateauPlace=1
            elif (j1[0]=="H" or j1[0]=="h"):
                BN[int(j1[2])+1][4]="O"
                BN[int(j1[2])+1][5]="O"
                BateauPlace=1
        if (j1[1]=="D" or j1[1]=="d"):
            BN[int(j1[2])+1][4]="O"
            if (j1[0]=="V" or j1[0]=="v"):
                if ((int(j1[2])+1)<7):
                    BN[int(j1[2])+2][4]="O"
                    BN[int(j1[2])+3][4]="O"
                    BateauPlace=1
            elif (j1[0]=="H" or j1[0]=="h"):
                BN[int(j1[2])+1][5]="O"
                BN[int(j1[2])+1][6]="O"
                BateauPlace=1
        if (j1[1]=="E" or j1[1]=="e"):
            BN[int(j1[2])+1][5]="O"
            if (j1[0]=="V" or j1[0]=="v"):
                if ((int(j1[2])+1)<7):
                    BN[int(j1[2])+2][5]="O"
                    BN[int(j1[2])+3][5]="O"
                    BateauPlace=1
            elif (j1[0]=="H" or j1[0]=="h"):
                BN[int(j1[2])+1][6]="O"
                BN[int(j1[2])+1][7]="O"
                BateauPlace=1
        if (j1[1]=="F" or j1[1]=="f"):
            BN[int(j1[2])+1][6]="O"
            if (j1[0]=="V" or j1[0]=="v"):
                if ((int(j1[2])+1)<7):
                    BN[int(j1[2])+2][6]="O"
                    BN[int(j1[2])+3][6]="O"
                    BateauPlace=1
            elif (j1[0]=="H" or j1[0]=="h"):
                BN[int(j1[2])+1][7]="O"
                BN[int(j1[2])+1][8]="O"
                BateauPlace=1
        if (j1[1]=="G" or j1[1]=="g"):
            BN[int(j1[2])+1][7]="O"
            if (j1[0]=="V" or j1[0]=="v"):
                if ((int(j1[2])+1)<7):
                    BN[int(j1[2])+2][7]="O"
                    BN[int(j1[2])+3][7]="O"
                    BateauPlace=1
            elif (j1[0]=="H" or j1[0]=="h"):
                BN[int(j1[2])+1][8]="O"
                BN[int(j1[2])+1][9]="O"
                BateauPlace=1
        if (j1[1]=="H" or j1[1]=="h"):
            BN[int(j1[2])+1][8]="O"
            if (j1[0]=="V" or j1[0]=="v"):
                if ((int(j1[2])+1)<7):
                    BN[int(j1[2])+2][8]="O"
                    BN[int(j1[2])+3][8]="O"
                    BateauPlace=1
            elif (j1[0]=="H" or j1[0]=="h"):
                BN[int(j1[2])+1][9]="O"
                BN[int(j1[2])+1][10]="O"
                BateauPlace=1
        Afficher()

    
        

    while True:
        data, addr = sock.recvfrom(1024)
        j2=data.decode()
        print ("LUI: ", j2)
        if (j2[0]=="A" or j2[0]=="a"):
            BN[int(j2[1])+1][1]="X"
        if (j2[0]=="B" or j2[0]=="b"):
            BN[int(j2[1])+1][2]="X"
        if (j2[0]=="C" or j2[0]=="c"):
            BN[int(j2[1])+1][3]="X"
        if (j2[0]=="D" or j2[0]=="d"):
            BN[int(j2[1])+1][4]="X"
        if (j2[0]=="E" or j2[0]=="e"):
            BN[int(j2[1])+1][5]="X"
        if (j2[0]=="F" or j2[0]=="f"):
            BN[int(j2[1])+1][6]="X"
        if (j2[0]=="G" or j2[0]=="g"):
            BN[int(j2[1])+1][7]="X"
        if (j2[0]=="H" or j2[0]=="h"):
            BN[int(j2[1])+1][8]="X"
        if (j2[0]=="I" or j2[0]=="i"):
            BN[int(j2[1])+1][9]="X"
        if (j2[0]=="J" or j2[0]=="j"):
            BN[int(j2[1])+1][9]="X"
        BN_dump = marshal.dumps(BN)
        sock.sendto(BN_dump,addr)
        Afficher()
        j1=input("MOI: ")
        if (j1[0]=="A" or j1[0]=="a"):
            BN[int(j1[1])+1][1]="X"
        if (j1[0]=="B" or j1[0]=="b"):
            BN[int(j1[1])+1][2]="X"
        if (j1[0]=="C" or j1[0]=="c"):
            BN[int(j1[1])+1][3]="X"
        if (j1[0]=="D" or j1[0]=="d"):
            BN[int(j1[1])+1][4]="X"
        if (j1[0]=="E" or j1[0]=="e"):
            BN[int(j1[1])+1][5]="X"
        if (j1[0]=="F" or j1[0]=="f"):
            BN[int(j1[1])+1][6]="X"
        if (j1[0]=="G" or j1[0]=="g"):
            BN[int(j1[1])+1][7]="X"
        if (j1[0]=="H" or j1[0]=="h"):
            BN[int(j1[1])+1][8]="X"
        if (j1[0]=="I" or j1[0]=="i"):
            BN[int(j1[1])+1][9]="X"
        if (j1[0]=="J" or j1[0]=="j"):
            BN[int(j1[1])+1][9]="X"
        BN_dump = marshal.dumps(BN)
        sock.sendto(BN_dump,addr)
        
        Afficher()
