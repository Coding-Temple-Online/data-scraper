import requests
from bs4 import BeautifulSoup
from .import db
from .models import Player

def populate_database(data):
    # Create a Beautiful Soup object from data
    soup = BeautifulSoup(data, 'html.parser')

    # Selenium functionality goes here

    # Acquire all player data from HTML table
    tbody=[i for i in soup.find_all(class_='row-hover')][1]
    # print(tbody)
    tr_list=[i for i in tbody if i !='\n']

    # compile a list of all players
    player_list =[]
    for idx, value in enumerate(tr_list):
        new_row = [row.text for row in tr_list[idx] if row != '\n'][1:]
        player_list.append(new_row)

    list_to_add = []
    for player in player_list:
        existing_player = Player.query.filter_by(name=player[0]).first()
        if existing_player is None:
            # pool player data into a dictionary
            player_data = {
                'name': player[0],
                'team': player[1],
                'pos': player[2],
                'mpg': player[5],
                'fta': player[9],
                'ftp': player[10],
                'tpa': player[11],
                'tpp': player[12],
                'thpa': player[13],
                'thpp': player[14],
                'ppg': player[17],
                'rpg': player[18],
                'apg': player[20],
                'spg': player[22],
                'bpg': player[23],
                'topg': player[24]
            }

            # instantiate a new player
            p = Player()
            # set the player's (p) attributes
            p.from_dict(player_data)
            list_to_add.append(p)

    db.session.add_all(list_to_add)
    db.session.commit()