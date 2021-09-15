class Team:
    def __init__(self, name, players, coach):
        self.name = name
        self.players = players
        self.coach = coach 
        self.points = 0

    def add_player(self, new_player):
        return self.players.append(new_player)

    def has_player(self, input_name):
        for player in self.players:
            if player == input_name:
                return True
        return False

    def play_game(self, game_won):
        if game_won == False:
            self.points -= 3
        elif game_won == True:
            self.points += 3