from soccersimulator import SoccerTeam
from .team import joueur1,joueur2,joueur3,joueur4





def get_team(i):
	if i==1:
		return SoccerTeam("DZ", [joueur1])
	if i==2:
		return SoccerTeam("DZZ", [joueur2,joueur1])
	if i==4:
		return SoccerTeam("DZZZ", [joueur5, joueur2, joueur3, joueur4])


