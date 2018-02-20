#!/usr/bin/python
#-*- coding: utf-8 -*-

#c'est un classe saimple en python 
#class parent 	
class Voiture:

	# definir un constructeur 
	def __init__(self):
		self.nom = "Audi "

	#definir une methode 
	def donne_moi_le_modele(self):
		return "250"

# children class

class Statumoteur(Voiture):

	def etat_du_moteur(self,cle):
		self.cle = cle

		if self.cle==0:
			print("La voiture est eteind")
		elif self.cle == 1:
			print("La voiture est allumer")
		else :
			print("verifier la valeur de la cle : o ou 1 !")


#try the class

if __name__=='__main__':
	#creer une instance 
	ma_voiture = Voiture()
	print("Le nom de la voiture est : ",ma_voiture.nom)
	print("Le modele de la voiture est : ",ma_voiture.donne_moi_le_modele())

	print("=====================")
	#tster le class children 
	test_moteur = Statumoteur()
	cle = 10
	print(test_moteur.etat_du_moteur(cle))
	print("=================")