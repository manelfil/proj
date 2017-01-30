# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 18:46:00 2017

@author: 3410516
"""
from strategies import MaStrategy

joueur1=Player(name="player 1", Strategy())
joueur3=Player(name="player 3", Strategy())
joueur4=Player(name="player 4", Strategy())

team1=SoccerTeam(name="Team1",[joueur1])
team2=SoccerTeam(name="Team2",[joueur3,joueur4])