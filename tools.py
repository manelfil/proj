#import soccersimulator
import math
import random
from soccersimulator import settings
from soccersimulator import SoccerAction 
from soccersimulator import Vector2D

class Mystate(object):
    def __init__(self,state,idteam,idplayer):
        self.state = state
        self.key = (idteam,idplayer)
        self.id_team=idteam
        self.id_player=idplayer
    @property
    def rienFaire(self):
        return SoccerAction()
    @property
    def position_balle(self):
		#Retourne la position de la balle
        return self.state.ball.position

    @property
    def vitesse_balle(self):
	 	#Retourne la vitesse de la balle
        return self.state.ball.vitesse

    @property
    def position_joueur(self):
		#Retourne la position du joueur
        return self.state.player_state(self.id_team, self.id_player).position

    @property
    def position_defense(self):
        return self.state.player_state(self.id_team, self.id_player == 0).position
    

	
    @property
    def peutShooter(self):
        return (self.position_balle.distance(self.position_joueur)) < (settings.PLAYER_RADIUS + settings.BALL_RADIUS) 

    @property
    def Shoot(self):
        return SoccerAction(self.position_balle - self.position_joueur, Vector2D(settings.GAME_WIDTH, settings.GAME_HEIGHT / 2) - self.position_joueur)
	
	
    @property
    def courirVersBalle(self):
        return SoccerAction(self.position_balle - self.position_joueur, Vector2D(0,0))

    @property
    def peutShooterDefensegauche(self):
        return self.position_balle.x < 35

    @property
    def peutShooterDefensedroit(self):
        return self.position_balle.x < 50

    @property
    def peutShooterAttaque(self):
        return self.position_balle.x > 110

    @property
    def peutShooterDefense(self):
        return self.position_balle.x < 35

    @property
    def peutShooterMilieu(self):
        return (self.position_balle.x > 35) 

    @property
    def peutShooterMilieuDefensif(self):
        return (self.position_balle.x < settings.GAME_WIDTH/2+10) 


    @property
    def shootDefense(self):
        if (self.peutShooter):
            return SoccerAction(self.position_balle - self.position_joueur, Vector2D(settings.GAME_WIDTH, settings.GAME_HEIGHT / 2) - self.position_joueur)
        else: 
            return SoccerAction(self.position_balle - self.position_joueur, Vector2D(0,0))

    @property
    def replacementDefense(self):
        return SoccerAction(Vector2D(10, settings.GAME_HEIGHT / 2) - self.position_joueur, Vector2D(0,0))
		 #le defenseur se replace en defense si la balle sort de sa zone defensive

    @property
    def replacementDefenseurGauche(self):
        return SoccerAction(Vector2D(10, settings.GAME_HEIGHT/2 + 5) - self.position_joueur, Vector2D(0,0))
		#le defenseur gauche se replace a sa position

    @property
    def replacementDefenseurDroit(self):
        return SoccerAction(Vector2D(10, settings.GAME_HEIGHT/2 - 5) - self.position_joueur, Vector2D(0,0))
	 	#le defenseur droit se replace a sa position

    @property
    def replacementMilieu(self):
        return SoccerAction(Vector2D(50, settings.GAME_HEIGHT/2) - self.position_joueur, Vector2D(0,0))

    @property
    def replacementMilieuDefensif(self):
		#Le milieu se place en position de contre attaque
        return SoccerAction(Vector2D(settings.GAME_WIDTH/2+10, self.position_balle.y) - self.position_joueur, Vector2D(0,0))

    @property
    def replacementAttaque(self):
		#L'attaquant se place devant les cages
        return SoccerAction(Vector2D(settings.GAME_WIDTH-30, self.position_balle.y) - self.position_joueur, Vector2D(0,0))
	



def attaquant_fonceur(Mystate):
    if(Mystate.peutShooter):
        return Mystate.Shoot	
    else:
        return Mystate.courirVersBalle

def attaquant_pointe(Mystate):
    if(Mystate.peutShooterAttaque):
        if(Mystate.peutShooter):
            return Mystate.Shoot
        else:
            return Mystate.courirVersBalle
    
    return Mystate.replacementAttaque

def defenseur_central(Mystate):
    if(Mystate.peutShooterDefense):
        if(Mystate.peutShooter):
            return Mystate.shootDefense
        else:
            return Mystate.courirVersBalle
    return Mystate.replacementDefense

def defenseur_gauche(Mystate):
    if(Mystate.peutShooterDefense):
        if(Mystate.peutShooter):
            return Mystate.shootDefense
        else:
            return Mystate.courirVersBalle
    return Mystate.replacementDefenseurGauche

def defenseur_droit(Mystate):
    if(Mystate.peutShooterDefense):
        if(Mystate.peutShooter):
            return Mystate.shootDefense
        else:
            return Mystate.courirVersBallestate,
    return Mystate.replacementDefenseurDroit

def milieu(Mystate):
    if(Mystate.peutShooterMilieu):
        if(Mystate.peutShooter):
            return Mystate.Shoot
        else:
            return Mystate.courirVersBalle
    return Mystate.replacementMilieu

def milieu_defensif(Mystate):
    if(Mystate.peutShooterMilieuDefensif):
        if(Mystate.peutShooter):
            return Mystate.Shoot
        else:
            return Mystate.courirVersBalle
    return Mystate.replacementMilieuDefensif