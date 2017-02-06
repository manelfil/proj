from PlayerStateDeco import MaStrategyFonceur
from PlayerStateDeco import MaStrategyDefensive
from PlayerStateDeco import MaStrategyCampeur
from PlayerStateDeco import MaStrategyUtilitaire
from PlayerStateDeco import MaStrategyGoal
from PlayerStateDeco import SoccerTeam, Player



joueur1 = Player("Majrez", MaStrategyFonceur())
joueur2 = Player("Mnolhi", MaStrategyDefensive())
joueur3 = Player("Larsen", MaStrategyCampeur())
joueur4 = Player("Selmani", MaStrategyGoal())

team1 = SoccerTeam("DZ", [joueur1])
team2 = SoccerTeam("Tremblez!", [joueur2,joueur1])
team4 = SoccerTeam("Lel", [joueur5, joueur2, joueur3, joueur4])

