from flask_sqlalchemy import SQLAlchemy

from app import db

class Seasons(db.Model):
    '''
        CREATE TABLE seasons (
          id serial PRIMARY KEY,
          season_name VARCHAR(16),
          start_date DATE,
          end_date DATE,
          total_games integer
        );
    '''
    id = db.Column(db.Integer, primary_key=True)
    season_name = db.Column(db.String(16))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    total_games = db.Column(db.Integer)

    def __repr__(self):
        return f'Season [id = {self.id}, season_name = {self.season_name}' + \
                f', start_date = {self.start_date}, end_date = {self.end_date}' + \
                f', total_games = {self.total_games}]'

    def to_json(self):
        return {
            'id': self.id,
            'season_name': self.season_name,
            'start_date': str(self.start_date),
            'end_date': str(self.end_date),
            'total_games': self.total_games
        }
