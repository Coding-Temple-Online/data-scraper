from app import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    team = db.Column(db.String)
    pos = db.Column(db.String)
    mpg = db.Column(db.Float)
    fta = db.Column(db.Float)
    ftp = db.Column(db.Float)
    tpa = db.Column(db.Float)
    tpp = db.Column(db.Float)
    thpa = db.Column(db.Float)
    thpp = db.Column(db.Float)
    ppg = db.Column(db.Float)
    rpg = db.Column(db.Float)
    apg = db.Column(db.Float)
    spg = db.Column(db.Float)
    bpg = db.Column(db.Float)
    topg = db.Column(db.Float)

    def __repr__(self):
        return f"<Player: {self.name} [{self.team.upper()}]>"

    def from_dict(self, data):
        for field in ['name', 'team', 'pos','mpg','fta','ftp','tpa','tpp','thpa','thpp','ppg','rpg','apg','spg','bpg','topg']:
            if field in data:
                setattr(self, field, data[field]) 

    def to_dict(self):
        player_dict = {
            'name': self.name,
            'team': self.team,
            'pos': self.pos,
            'mpg': self.mpg,
            'fta': self.fta,
            'ftp': self.ftp,
            'tpa': self.tpa,
            'tpp': self.tpp,
            'thpa': self.thpa,
            'thpp': self.thpp,
            'ppg': self.ppg,
            'rpg': self.rpg,
            'apg': self.apg,
            'spg': self.spg,
            'bpg': self.bpg,
            'topg': self.topg
        }
        return player_dict