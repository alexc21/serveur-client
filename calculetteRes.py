import socket

hote = 'localhost'
port = 12800

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print("Le serveur écoute à présent sur le port {}".format(port))

connexion_avec_client, infos_connexion = connexion_principale.accept()


msg1 = int(connexion_avec_client.recv(1024).decode())
 
msg2 = connexion_avec_client.recv(1024).decode()
 
msg3 = int(connexion_avec_client.recv(1024).decode())
    
resultat =""

if msg2 == "*":
    resultat=  msg1 * msg3
    print(resultat)
    resultat = str(resultat).encode()
    connexion_avec_client.send(resultat)
elif msg2 == "/":
    resultat=  msg1 / msg3
    print(resultat)
    resultat = str(resultat).encode()
    connexion_avec_client.send(resultat)
elif msg2 == "+":
    resultat= msg1 + msg3
    print(resultat)
    resultat = str(resultat).encode()
    connexion_avec_client.send(resultat)
else:
    resultat=  msg1 - msg3
    print(resultat)
    resultat = str(resultat).encode()
    connexion_avec_client.send(resultat)
    
    # L'instruction ci-dessous peut lever une exception si le message
   
#print("Fermeture de la connexion")
#connexion_avec_client.close()
#connexion_principale.close()"""
























