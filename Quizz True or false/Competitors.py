class Competitor:
    user_id = 0  # Class attribute

    def __init__(self, username, score=0):
        Competitor.user_id += 1
        self.user_id = Competitor.user_id
        self.username = username
        self.score = score
