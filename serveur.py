import socket
import marshal
UDP_IP = "10.160.108.13"
UDP_PORT = 5050
BateauPlace=0

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))



BN=[['*','A','B','C','D','E',"F","G","H","I"],['1','-','-','-','-','-','-','-','-','-'],['2','-','-','-','-','-','-','-','-','-'],['3','-','-','-','-','-','-','-','-','-'],
    ['4','-','-','-','-','-','-','-','-','-'],['5','-','-','-','-','-','-','-','-','-'],['6','-','-','-','-','-','-','-','-','-'],['7','-','-','-','-','-','-','-','-','-'],
    ['8','-','-','-','-','-','-','-','-','-'],['9','-','-','-','-','-','-','-','-','-'],]     #Creation du tableau de jeu
idx=True

def Afficher():     #Creation de la fonction Afficher()
    tab = ""       #Actualisation du jeu
    for i in range(10):
        tab = "| "
        for j in range (10):        #Mise en forme du jeu
            tab += BN[i][j]
            tab += " | "
        print(tab)     #Affiche le jeu


while (BateauPlace!=2):
	if BateauPlace==0 :
		input("Placez votre bateau: ")
		BateauPlace+=1
	addr = sock.recvfrom(1024)
	sock.sendto("Place ton bateau: ",addr)
	data= sock.recvfrom(1024)
	j2=data.decode()
    

while True:
    data, addr = sock.recvfrom(1024)
    j2=data.decode()
    print ("LUI: ", j2)
    if (j2[0]=="A" or j2[0]=="a"):
        BN[int(j2[1])][1]="X"
    if (j2[0]=="B" or j2[0]=="b"):
        BN[int(j2[1])][2]="X"
    if (j2[0]=="C" or j2[0]=="c"):
        BN[int(j2[1])][3]="X"
    if (j2[0]=="D" or j2[0]=="d"):
        BN[int(j2[1])][4]="X"
    if (j2[0]=="E" or j2[0]=="e"):
        BN[int(j2[1])][5]="X"
    if (j2[0]=="F" or j2[0]=="f"):
        BN[int(j2[1])][6]="X"
    if (j2[0]=="G" or j2[0]=="g"):
        BN[int(j2[1])][7]="X"
    if (j2[0]=="H" or j2[0]=="h"):
        BN[int(j2[1])][8]="X"
    if (j2[0]=="I" or j2[0]=="i"):
        BN[int(j2[1])][9]="X"
    BN_dump = marshal.dumps(BN)
    sock.sendto(BN_dump,addr)
    Afficher()
    j1=input("MOI: ")
    if (j1[0]=="A" or j1[0]=="a"):
        BN[int(j1[1])][1]="X"
    if (j1[0]=="B" or j1[0]=="b"):
        BN[int(j1[1])][2]="X"
    if (j1[0]=="C" or j1[0]=="c"):
        BN[int(j1[1])][3]="X"
    if (j1[0]=="D" or j1[0]=="d"):
        BN[int(j1[1])][4]="X"
    if (j1[0]=="E" or j1[0]=="e"):
        BN[int(j1[1])][5]="X"
    if (j1[0]=="F" or j1[0]=="f"):
        BN[int(j1[1])][6]="X"
    if (j1[0]=="G" or j1[0]=="g"):
        BN[int(j1[1])][7]="X"
    if (j1[0]=="H" or j1[0]=="h"):
        BN[int(j1[1])][8]="X"
    if (j1[0]=="I" or j1[0]=="i"):
        BN[int(j1[1])][9]="X"
    BN_dump = marshal.dumps(BN)
    sock.sendto(BN_dump,addr)
    
    Afficher()