# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 16:31:09 2021

@author: Matthieu COLLET

Extrait du sujet :
    
"Présentation du problème
On souhaite développer un outil permettant de simuler les combats automatiques proposés 
dans le mode de jeu « champs de bataille » du jeu de stratégie et de cartes à collectionner 
« HearthStone » édité par Blizzard (https://playhearthstone.com/fr-fr/news/23156373).
Ce jeu de stratégie, qui voit s’affronter 8 joueurs, se déroule en deux principales étapes :
    - La première pendant laquelle le joueur définit sa stratégie, recrute et positionne les serviteurs
    qui composent son équipe (limitée à 7 en même temps).
    - La seconde, résolue de façon automatique, qui voit s’affronter les équipes de deux joueurs 
    sélectionnés aléatoirement. 
Ce projet se focalise exclusivement sur cette partie de simulation des affrontements :
on considère donc en entrée de l’outil les équipes de serviteurs déjà organisées et préparées.
Ces deux principales étapes s’enchainent jusqu’il ne reste plus qu’un joueur : le vainqueur de 
la partie !"

Github

"""

import random as rd

################################### Création des classes ###########################################

###Classes avec héritage###

class Classe_RalesdAgonie():   #Classe mère
    """Se déclenche quand le serviteur meurt"""
    def __init__(self, taCible, leServiteurActeur):
        self._cible = taCible   #l'attribut est un élément de la classe "serviteurs"
        self._ServiteurActeur = leServiteurActeur   #l'attribut est un élément de la classe "serviteurs"
        
    def get_cible(self):
        return self._cible
    Cible = property(get_cible)
    
    def get_ServiteurActeur(self):
        return self._ServiteurActeur
    ServiteurActeur = property(get_ServiteurActeur)
    
    def set_cible(self, cible):
        self._cible = cible

class invocation(Classe_RalesdAgonie):
    def __init__(self, tonServiteurInvoque, tonNbOccurrence):
        self._ServiteurInvoque = tonServiteurInvoque   #l'attribut est un élément de la classe "serviteurs"
        self._NbOccurence = int(tonNbOccurrence)
        
    def get_ServiteurInvoque(self):
        return self._ServiteurInvoque
    ServiteurInvoque = property(get_ServiteurInvoque)
    
    def get_NbOccurence(self):
        return self._NbOccurence
    NbOccurence = property(get_NbOccurence)
    
    def start(self):
        for i in range(self.NbOccurrence):
            joueurs.add_Serviteurs(self.serviteurs.Joueur,self.ServiteurInvoque)   #J'ajoute dans les serviteurs du joueur le nombre de fois nécessaire le serviteur invoqué
            
class degats(Classe_RalesdAgonie):   #Peut s'attaquer à un seul serviteur, tout les serviteurs ennemis ou tout les serviteurs
    def __init__(self, tesDegats):
        self._degats = int(tesDegats)
    
    def get_degats(self):
        return self._degats
    Degats = property(get_degats)
    
    def start(self):
        for elt in self.Cible:
            #Pq erreur ??
            add_PV(elt,self.Degats)   #Pour chaque cible, on inflige les dégâts

class AmeliorationStats(Classe_RalesdAgonie):
    """ 3 types d'amélioration :
            - 1 : augmentation de PV
            - 2 : augmentation des points d'attaques
            - 3 : ajout d'un mot clef
        En prendra soin de nomer les améliorations comme ceci : "TypesCaractéristique"
        Par exemple "123" signifie une augmentation de PV de +23"""
    def __init__(self, taNature):
        self._nature = str(taNature)
        
    def get_nature(self):
        return self._nature
    Nature = property(get_nature)
      
    def start_simple(self):
        #Je choisis ma cible.
        joueur_serviteur = self.ServiteurActeur.Joueur
        equipe = joueur_serviteur.Equipe
        joueurs_equipe = equipe.Joueurs
        serviteurs_equipe = []
        for joueur in joueurs_equipe:
            serviteurs_equipe += joueur.ServiteursVivants
        #Pq erreur ???
        set_cible(self, rd.choice(serviteurs_equipe))   #On choisis au hasard un serviteur allié et on le désigne comme cible pour l'amélioration
        
        #J'applique ensuite l'amélioration.
        type_amelioration = self.Nature[0]
        caractéristique_amelioration = self.Nature[1:]
        if type_amelioration == "1":
            add_PV(self.Cible, caractéristique_amelioration)
        elif type_amelioration == "2":
            add_PointsdAttaque(self.Cible, caractéristique_amelioration)
        elif type_amelioration == "3":
            add_MotClef(self.Cible, caractéristique_amelioration)
            
    def start_famille(self):
        #Ici les cibles de l'amélioration sont tout les membres d'une même famille.
        famille_ServiteurActeur = self.ServiteurActeur.Famille   #Voici la famille du serviteur qui déploie son râle d'agonie
        joueur_serviteur = self.ServiteurActeur.Joueur
        equipe = joueur_serviteur.Equipe
        joueurs_equipe = equipe.Joueurs
        serviteurs_cibles = []
        for joueur in joueurs_equipe:
            if joueur.Famille == famille_ServiteurActeur:   #Je prends seulement les serviteurs d'une même famille
                serviteurs_cibles += joueur.ServiteursVivants
        
        #J'applique ensuite l'amélioration à tout les serviteurs cibles.
        for serviteur_cible in serviteurs_cibles:
            type_amelioration = self.Nature[0]
            caractéristique_amelioration = self.Nature[1:]
            if type_amelioration == "1":
                add_PV(serviteur_cible, caractéristique_amelioration)
            elif type_amelioration == "2":
                add_PointsdAttaque(serviteur_cible, caractéristique_amelioration)
            elif type_amelioration == "3":
                add_MotClef(serviteur_cible, caractéristique_amelioration)   
    
class Classe_Bonus():   #Autre classe mère
    pass

class auras(Classe_Bonus):
    pass

class AurasSousConditions(Classe_Bonus):
    
    pass

###Classes sans héritage###

class serviteurs():   #7 par joueur
    def __init__(self, toNnom, tesPV, tesPointsdAttaque, tonNiveau, taFamille, tesMotsClefs, tonRaledAgonie,tonBonus, tonJoueur):
        self._nom = str(toNnom)
        self._PV = int(tesPV)
        self._PointsdAttaque = int(tesPointsdAttaque)
        self._niveau = int(tonNiveau)
        self._famille = taFamille   #l'attribut est un objet de la classe "Classe_Famille"
        self._joueur = tonJoueur   #l'attribut est un objet de la classe "joueurs"
        self._MotsClefs = list(tesMotsClefs)   #l'attribut est une liste d'objets de la classe "Classe_MotsClefs"
        self._RaledAgonie = tonRaledAgonie   #l'attribut est un objet de la classe "Classe_RalesdAgonie"
        self._bonus = tonBonus   #l'attribut est un objet de la classe "Classe_Bonus"
        
        
    def get_nom(self):
        return self._nom
    Nom = property(get_nom)
    
    def get_famille(self):
        return self._famille
    Famille = property(get_famille)
    
    def get_joueur(self):
        return self.get_joueur
    Joueur = property(get_joueur)
    
    def get_MotsClefs(self):
        return self._MotsClefs
    MotsClefs = property(get_MotsClefs)
    
    def add_MotClef(self, nv_MotClef):
        self._MotsClefs.append(nv_MotClef)
    
    def get_RaledAgonie(self):
        return self._RaledAgonie
    RaledAgonie = property(get_RaledAgonie)
    
    def get_bonus(self):
        return self._bonus
    Bonus = property(get_bonus)
    
    def get_PV(self):
        return self._PV
    PV = property(get_PV)
    
    def add_PV(self, dommages):   #Positifs si gains/soins, négatifs si dégâts
        self._PV += dommages
    
    def get_PointsdAttaque(self):
        return self._PointsdAttaque
    PointdAttaque = property(get_PointsdAttaque)
    
    def add_PointsdAttaque(self, up_attaque):
        self._PointsdAttaque += up_attaque
    
    def get_niveau(self):
        return self._niveau
    Niveau = property(get_niveau)
    
    def deces(self):
        self.Joueur.ServiteursVivants.remove(self)
        self.Joueur.ServiteursMorts.append(self)
    
    def __repr__(self):
        return "Serviteur " + self.get_nom()
    
class Classe_Famille():   # ??
    def demon():
        pass
    
    def dragon():
        pass
    
    def elementaire():
        pass
    
    def meca():
        pass

class vengeance():   #Compte simplement les serviteurs tués
    pass

class joueurs():   #8 par equipe
    def __init__(self, tesServiteursVivants, tesServiteursMorts, tesCombats, tonNom, tonEquipe, tesPV):
        self._ServiteurSvivants = list(tesServiteursVivants)
        self._ServiteursMorts = []
        self._combats = list(tesCombats)
        self._nom = str(tonNom)
        self._equipe = tonEquipe
        self._PV = int(tesPV)
        
    def get_ServiteursVivants(self):
        return self._ServiteursVivants
    ServiteursVivants = property(get_ServiteursVivants)
    
    def add_ServiteurVivants(self, serviteur):
        self._ServiteursVivants.append(serviteur)
        
    def get_ServiteursMorts(self):
        return self._ServiteursMorts
    ServiteursMorts = property(get_ServiteursMorts)
    
    def add_ServiteusrMorts(self, serviteur):
        self._ServiteurMorts.append(serviteur)
    
    def get_combats(self):
        return self._combats
    Combats = property(get_combats)
    
    def get_nom(self):
        return self._nom
    Nom = property(get_nom)
    
    def get_equipe(self):
        return self._equipe
    Equipe = property(get_equipe)
    
    def get_PV(self):
        return self._PV
    PV = property(get_PV)
    
    def add_PV(self, dommages):
        self._PV += dommages
    
    def __repr__(self):
        return "Joueurs " + self.get_nom()

class equipe():
    def __init__(self,tesJoueurs, tonNom):
        self._joueurs = list(tesJoueurs)
        self._nom = str(tonNom)
        
    def get_joueurs(self):
        return self._joueurs
    Joueurs = property(get_joueurs)
    
    def get_nom(self):
        return self._nom
    Nom = property(get_nom)
    
    def __repr__(self):
        return "Equipe " + self.get_nom()
    
class Classe_MotsClefs():
    def __init__(self, tonTyp):
        self._type = str(tonTyp)
    
    def get_type(self):
        return self._type
    Type = property(get_type)
    
    def provocation():
        pass
    
    def toxicité():
        pass
    
    def BouclierDivin():
        pass
    
    def reincarnation():
        pass
    
    def FurieDesVents():
        pass
        
################################### Création des fonctions ###########################################
        
def combat():
    pass

