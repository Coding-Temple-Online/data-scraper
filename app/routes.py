import requests, os, time
from flask import current_app as app, render_template, redirect, url_for, request, json
from .import db
from .models import Player, SelectedPlayer
from .forms import GetPlayerDataForm
from .seed import populate_database
from csv import writer
import csv

@app.route('/', methods=['GET', 'POST'])
def index():
    form = GetPlayerDataForm()
    form.name.choices = [(p.id, p.name) for p in Player.query.order_by('name').all()] or []
    context = {
        'form': form,
        'players': SelectedPlayer.query.order_by('name').all()
    }
    return render_template('index.html', **context)

@app.route('/get_data', methods=['POST'])
def get_data():
    form = GetPlayerDataForm()
    if request.method == 'POST':
        id_ = form.name.data

        # Query original player from database
        p = Player.query.get(id_)
        player_stuff_to_add = Player.query.get(id_)


        if not os.path.isfile("data.json"):
            with open("data.json", "w") as save_file:
                json.dump([], save_file)
                # json.dump([p.to_dict()], save_file)

        if os.path.isfile("data.json"):
            with open("data.json", "r+") as save_file:
                data = json.load(save_file)
                with open("data.json", "w+") as save_file:
                    data.append(p.to_dict())
                    json.dump(data, save_file)

        # create the SelectedPlayer so I can show info in table
        table_player = SelectedPlayer()
        table_player.from_dict(player_stuff_to_add.to_dict())

        db.session.add(table_player)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/seed_data', methods=['GET'])
def seed_data():
    url = 'https://www.nbastuffer.com/2019-2020-nba-player-stats/'
    page = requests.get(url)
    populate_database(page.content)
    return redirect(url_for('index'))

@app.route('/cronjob', methods=['POST'])
def cronjob():
    p = SelectedPlayer.query.get(request.args.get('id'))

    
    csv_columns = p.to_dict().keys()
    pdict = p.to_dict()
    csv_file = "players.csv"

    while True:
        if not os.path.isfile('players.csv'):
            try:
                with open(csv_file, 'w') as f:
                    writer = csv.DictWriter(f, fieldnames=csv_columns)
                    writer.writeheader()
            except IOError:
                print("I/O error")
        with open(csv_file, 'a+', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=csv_columns)
            writer.writerow(pdict)
        time.sleep(5)
        # time.sleep(86407)
    return redirect(url_for('index'))
        