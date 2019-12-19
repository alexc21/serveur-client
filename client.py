import socket

hote = "localhost"
port = 12800


connexion= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion.connect((hote, port))
print("Connexion établie avec le serveur sur le port {}".format(port))


valeur=input()
signe=input()
valeur2=input()
    
    # Peut planter si vous tapez des caractères spéciaux
valeur= valeur.encode()
signe= signe.encode()
valeur2= valeur2.encode()
    
    # On envoie le message
connexion.send(valeur)
connexion.send(signe)    
connexion.send(valeur2)

msg_recu = print("le resultat est", connexion.recv(1024))


print("Fermeture de la connexion")
connexion.close()




























