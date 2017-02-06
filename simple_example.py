import  soccersimulator
from soccersimulator  import Strategy, SoccerAction, Vector2D
from soccersimulator import SoccerTeam, Simulation
from soccersimulator import SimuGUI,show_state,show_simu
from soccersimulator.settings import *
from tools import *
import math
import random



class PlayerStateDeco:
	def __init__(self,state, id_team, id_player):
		self.state=state
		self.id_team=id_team
		self.id_player=id_player
	@property
	def ball_pos(self):
		return self.state.ball.position
	
	def pos(self):
		return self.state.player_state(self.id_team,self.id_player).position
	
	def petit_pas(self):
		x=self.cible
		x.norm=1.2
		if(self.dist_ball()<(PLAYER_RADIUS + BALL_RADIUS)):
			if(self.distance_adv_proche()<20):
				if(self.ball_pos.y > GAME_HEIGHT - 46):
					x.y+=0.60
				else:
					x.y-=0.60
				return SoccerAction(0,x)
			else:
				return SoccerAction(0,x)
		else:
			return SoccerAction()
             
 

	def campeur(self):
		if(self.id_team==1):
			camping=Vector2D(115,self.pos().y)
		else:
			camping=Vector2D(GAME_WIDTH-115,self.pos().y)
		return SoccerAction(camping-self.pos(),Vector2D(0,0))
 
	def pos_player(self,idteam,idplayer):
		return self.state.player_state(idteam,idplayer).position
	@property
	def cible(self):
            	return self.his_goal-self.pos()
            	
	@property
	def my_goal(self):
		if (self.id_team==1): return Vector2D(0,90/2.)
		return Vector2D(150,90/2.)
	@property
	def his_goal(self):
		if (self.id_team==2): return Vector2D(0,90/2.)
		return Vector2D(150,90/2.)
		

	def dist_ball(self):
		return self.ball_pos.distance(self.pos())
	
	def suivre_balle(self):
    		return SoccerAction(self.ball_pos-self.pos(), Vector2D(0,0))
		
	def shoot_def(self):
		if(self.dist_ball()<(1. + 0.65)):
			
			cible_def=self.cible
		
			#cible_def.angle = 35
			return SoccerAction(0,cible_def)
		else:
			return SoccerAction()


	def shoot(self):
		if(self.dist_ball()<(1. + 0.65)):
			return SoccerAction(0,self.cible)
		else:
			return SoccerAction()
    			

	def shoot_nice(self):
		a=self.cible
		if(self.dist_ball()<(1. + 0.65)):
			if(self.ball_pos.y <= 90 - 46):
				a.y-=2.5
				return SoccerAction(0, a)
			elif(self.ball_pos.y > 90 - 46):
				a.y+=2.3
				return SoccerAction(0, a)
		else:
				return SoccerAction()		
            		
            		
	def get_adv_proche(self):
		return sorted([ (self.pos().distance(self.pos_player(id_team,id_player)),id_team,id_player) for (id_team, id_player) in self.state.players if id_team !=self.id_team])
        
	def get_copain_proche(self):
		return sorted([ (self.pos().distance(self.pos_player(id_team,id_player)),id_team,id_player) for (id_team, id_player) in self.state.players if id_team ==self.id_team])
        	
	def distance_adv_proche(self):
        	
		liste_adv=self.get_adv_proche()
        	
		(dist,idteam,idplayer)=liste_adv[0]
		return dist
	def distance_copain_proche(self):
        	
		liste_copain=self.get_copain_proche()
        	
		(dist,idteam,idplayer)=liste_copain[1]
		return dist
        	
	def passe(self):
		liste_copain=self.get_copain_proche()
		(a,it,ip)=liste_copain[1]
		if(self.dist_ball()<(1. + 0.65)):
			passe=self.state.player_state(it,ip).position-self.pos()
			passe.norm=1
			return SoccerAction(0, passe)
		else:
			return SoccerAction()

	def defense(self):
		if(self.id_team==1):
			back=Vector2D(18, 90/2.)-self.pos()
			if(((self.ball_pos.x < 150/2) and (self.distance_adv_proche()>12))or((self.ball_pos.x < 150/2) and (self.dist_ball()<12))):
				return self.suivre_balle()+ self.shoot_def()
			else:
				return SoccerAction(back, Vector2D())
		
		else:
			back=Vector2D(150-18, 90/2.)-self.pos()
			
			if(((self.ball_pos.x > 150/2) and (self.distance_adv_proche()>12))or((self.ball_pos.x > 150/2) and (self.dist_ball()<12))):
				return self.suivre_balle()+ self.shoot_def()
			else:
				return SoccerAction(back, Vector2D())

	def goal(self):
		if(self.id_team==1):
			back=Vector2D(3, 90/2.)-self.pos()
			if((self.ball_pos.x < 150/10)and(self.dist_ball()<12)):
				return self.suivre_balle()+ self.shoot_def()
			else:
				if(self.ball_pos.y <= 90 - 46):
					back.y-=2.5
				elif(self.ball_pos.y > 90 - 46):
					back.y+=2.3
					return SoccerAction(back, Vector2D())
		
		else:
			back=Vector2D(150-3, 90/2.)-self.pos()
			
			if((self.ball_pos.x > 9*150/10)and(self.dist_ball()<12)):
				return self.suivre_balle()+ self.shoot_def()
			else:
				if(self.ball_pos.y <= 90 - 46):
					back.y-=2.5
				elif(self.ball_pos.y > 90 - 46):
					back.y+=2.3
					return SoccerAction(back, Vector2D())
		
	def utilitaire(self):
      
		if((self.dist_ball())<15 and (self.distance_adv_proche())<10 and (self.distance_copain_proche())<15):
			return self.defense()
        	
		return self.suivre_balle()+self.passe()
        			
	
	
					
	def fonceur(self):
		if(math.fabs(self.pos().x-self.his_goal.x)<25):
			return self.suivre_balle()+self.shoot_nice()
		return self.suivre_balle()+self.petit_pas()
        	
	def jeupasse(self):
		liste_copain=self.get_copain_proche()
		(a,it,ip)=liste_copain[1]
		if(self.dist_ball()<(1. + 0.65)):
			passe=self.state.player_state(it,ip).position-self.pos()
			
			return SoccerAction(Vector2D(), passe)
		else:
	    		
			return self.demarque()
	
	def demarque(self):
		liste_copain=self.get_copain_proche()
		(a,it,ip)=liste_copain[1]
		if(self.dist_ball()>self.state.player(it,ip).position.distance(self.state.ball.position)):
			"""demarque=Vector2D(randint(40,110),randint(20,70))
			if(demarque.distance(ball_pos)>40):
				return SoccerAction(demarque-self.pos(),Vector2D(0,0))
			else:"""
			
			#demarque=self.ball_pos+self.pos()
			
			demarque=Vector2D((self.state.ball.position.x+20)%150,(self.state.ball.position.y+20)%90)
			return SoccerAction(demarque-self.pos(),Vector2D(0,0))
		else:
			
			return self.suivre_balle()
   
   
	def campe(self):
		if(self.id_team==1):
			if(self.ball_pos.x > 3*150/4 or self.dist_ball()<(1. + 0.65)*10 ):
				return self.suivre_balle()+self.shoot_nice()
			else:
				return self.campeur()+self.shoot_nice()
		else:
			if(self.ball_pos.x < 150/4 or self.dist_ball()<(1. + 0.65)*10 ):
				return self.suivre_balle()+self.shoot_nice()
			else:
				return self.campeur()+self.shoot_nice()

          
	def courirVersBalle(self):
		return SoccerAction(self.position_balle - self.position_joueur, Vector2D(0,0))

	
class MaStrategyFonceur(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Fonceur")
	def compute_strategy(self, state, id_team, id_player):
		Mystate=PlayerStateDeco(state, id_team, id_player)
        
class MaStrategyCampeur(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Campeur")
	def compute_strategy(self, state, id_team, id_player):
		Mystate=PlayerStateDeco(state, id_team, id_player)
		return  Mystate.campe()
        
class MaStrategyDefensive(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Defensive")
	def compute_strategy(self,state,id_team,id_player):
		Mystate=PlayerStateDeco(state,id_team,id_player)
		return Mystate.defense()


class MaStrategyGoal(Strategy):
	def __init__(self):
		Strategy.__init__(self,"Goal")
	def compute_strategy(self,state,id_team,id_player):
		Mystate=PlayerStateDeco(state,id_team,id_player)
		return Mystate.goal()


class RandomStrategy(Strategy):
    def __init__(self):
        Strategy.__init__(self,"Random")
    def compute_strategy(self,state,id_team,id_player):
        mystate=PlayerStateDeco(state,id_team,id_player)
        return SoccerAction()

## Creation d'une equipe
team1 = SoccerTeam(name="team1",login="etu1")
team2 = SoccerTeam(name="team2",login="etu2")
team1.add("John",MaStrategyFonceur()) #Strategie qui ne fait rien
team2.add("Paul",MaStrategyGoal())   #Strategie aleatoire
team1.add("Johns",MaStrategyGoal()) #Strategie qui ne fait rien
team2.add("Pauls",MaStrategyFonceur())   #Strategie aleatoire
#Creation d'une partie
simu = Simulation(team1,team2)
#Jouer et afficher la partie
show_simu(simu)

