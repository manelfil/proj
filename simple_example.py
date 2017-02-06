import  soccersimulator
from soccersimulator  import Strategy, SoccerAction, Vector2D
from soccersimulator import SoccerTeam, Simulation
from soccersimulator import SimuGUI,show_state,show_simu
from soccersimulator.settings import *
from tools import *
import math
import random
from tools import *







## Creation d'une equipe
team1 = SoccerTeam(name="team1",login="etu1")
team2 = SoccerTeam(name="team2",login="etu2")
team1.add("John",MaStrategyFonceur()) #Strategie qui ne fait rien
team2.add("Paul",MaStrategyCampeur())   #Strategie aleatoire
team1.add("Johns",MaStrategyCampeur()) #Strategie qui ne fait rien
team2.add("Pauls",MaStrategyFonceur())   #Strategie aleatoire
#Creation d'une partie
simu = Simulation(team1,team2)
#Jouer et afficher la partie
show_simu(simu)

