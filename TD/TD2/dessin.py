import tkinter as tk

HEIGHT = 800
WIDTH = 800

racine = tk.Tk() # Création de la fenêtre racine

bouton1 = tk.Button(racine, text="Choisir une couleur", command=lambda : affichage("Choisir une couleur"),
                     font = ("helvetica", "30")
                   ) 
bouton1.grid(column=1, row=0) 

bouton1 = tk.Button(racine, text="Cercle", command=lambda : affichage("ils sont fous ces romains"),
                     font = ("helvetica", "30")
                   ) 
bouton1.grid(column=0, row=1) 

bouton1 = tk.Button(racine, text="Carré", command=lambda : affichage("ils sont fous ces romains"),
                     font = ("helvetica", "30"))
bouton1.grid(column=0, row=2) 

bouton1 = tk.Button(racine, text="Croix", command=lambda : affichage("ils sont fous ces romains"),
                     font = ("helvetica", "30")
                   ) 
bouton1.grid(column=0, row=3) 


canvas = tk.Canvas(racine, bg= "black" ,  height=HEIGHT, width=WIDTH)
canvas.grid(column=1, row=1)

racine.mainloop() # Lancement de la boucle principale