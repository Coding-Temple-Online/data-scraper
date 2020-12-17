import requests
from flask import current_app as app, render_template, redirect, url_for
from bs4 import BeautifulSoup
from .import db
from .models import Player
from .forms import GetPlayerDataForm

@app.route('/', methods=['GET', 'POST'])
def index():
    form = GetPlayerDataForm()
    form.names.choices = [(p.id, p.name) for p in Player.query.order_by('name').all()]
    if form.validate_on_submit():
        print(Player.query.get(form.names.data).name)
        return redirect(url_for('index'))
    
    context = {
        'form': form
    }
    
    return render_template('index.html', **context)

@app.route('/get_data', methods=['POST'])
def get_data():
    url = 'https://www.nbastuffer.com/2019-2020-nba-player-stats/'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    # tbody=[i for i in soup.find('class_="row-hover"')]
    # tr_list=[i for i in tbody if i !='\n']
    # player_list =[]
    # for idx, value in enumerate(tr_list):
    # new_row= [row.text for row in tr_list[idx] if row != '\n'][1:]
    # player_list.append(new_row)
    
    tbody=[i for i in soup.find('class_="row-hover"')]
    tr_list=[i for i in tbody if i !='\n']


    # print(tbody)
    return redirect(url_for('index'))

# @app.route('/seed_data', methods=['GET'])
# def seed_data():
#     url = 'https://www.nbastuffer.com/2019-2020-nba-player-stats/'
#     page = requests.get(url)
#     soup = BeautifulSoup(page.content, 'html.parser')

#     tbody=[i for i in soup.find(class_='row-hover')]
#     tr_list=[i for i in tbody if i !='\n']
#     player_list =[]
#     for idx, value in enumerate(tr_list):
#         new_row = [row.text for row in tr_list[idx] if row != '\n'][1]
#         player_list.append(new_row)

#     list_to_add = []
#     for name in player_list:
#         existing_player = Player.query.filter_by(name=name).first()
#         if existing_player is None:
#             player = Player(name=name)
#             list_to_add.append(player)

#     db.session.add_all(list_to_add)
#     db.session.commit()
#     return redirect(url_for('index'))
        