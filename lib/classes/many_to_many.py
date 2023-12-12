class Game:

    all = {}

    def __init__(self, title):
        self.title = title
        self.plays = {}
        # type(self).all[title] = self

    def results(self):
        results = []
        for result in Result.all:
            if result.game.title == self.title:
                results.append(result)
        return results

    def players(self):
        results = set()
        for result in Result.all:
            if result.game == self:
                results.add(result.player)
        return list(results)

    def average_score(self, player):
        scores = []
        total = 0
        for result in Result.all:
            if result.player == player and result.game == self:
                scores.append(result.score)
        for score in scores:
            total += score
        return total / len(scores)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,name):
        if not hasattr(self,'_title') and isinstance(name,str) and len(name) > 0:
            self._title = name

class Player:

    all = {}

    def __init__(self, username):
        self.username = username
        self.played = {}

    def results(self):
        results = []
        for result in Result.all:
            if result.player == self:
                results.append(result)
        return results

    def games_played(self):
        results = set()
        for result in Result.all:
            if result.player == self:
                results.add(result.game)
        return list(results)

    def played_game(self, game):
        return game in self.games_played()
        pass

    def num_times_played(self, game):
        num = 0
        for result in Result.all:
            if result.player == self and result.game == game:
                num += 1
        return num

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self,name):
        if isinstance(name,str) and 2 < len(name) < 16:
            self._username = name

class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        type(self).all.append(self)
    
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self,object):
        self._player = object
    
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self,object):
        self._game = object
    
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, num):
        if not hasattr(self, 'score'):
            if isinstance(num, int) and 1 <= num <= 5000:
                self._score = num

