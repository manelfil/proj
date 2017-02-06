from .tools import PlayerStateDeco , MaStrategyFonceur, MaStrategyDefensive, MaStrategyCampeur,  MaStrategyGoal
from soccersimulator import SoccerTeam, Player



joueur1 = Player("Majrez", MaStrategyFonceur())
joueur2 = Player("Mnolhi", MaStrategyGoal())
joueur3 = Player("Larsen", MaStrategyCampeur())
joueur4 = Player("Selmani", MaStrategyGoal())

team1 = SoccerTeam("DZ", [joueur1])
team2 = SoccerTeam("DZZ", [joueur2,joueur1])
team4 = SoccerTeam("DZZZ", [joueur1, joueur2, joueur3, joueur4])

