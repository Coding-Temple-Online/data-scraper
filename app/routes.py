import requests, os
from flask import current_app as app, render_template, redirect, url_for, request, json
from .import db
from .models import Player
from .forms import GetPlayerDataForm
from .seed import populate_database

@app.route('/', methods=['GET', 'POST'])
def index():
    form = GetPlayerDataForm()
    form.name.choices = [(p.id, p.name) for p in Player.query.order_by('name').all()] or []
    context = {
        'form': form
    }
    
    return render_template('index.html', **context)

@app.route('/get_data', methods=['POST'])
def get_data():
    form = GetPlayerDataForm()
    if request.method == 'POST':
        
        p = Player.query.get(form.name.data)

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
                    
        # row_data = []
        # with open('data.json', 'r') as f:
        #     for i in f.readlines():
        #         new_data.append(i)
        # with open("data.json", "a+") as save_file:
        #     for i in save_file.readlines():
        #         print(i)
            # print(type(save_file))
            # data = json.load(save_file)
            # print("works")
            # data.append(p.to_dict)
            # json.dump(p.to_dict(), save_file) 
        # with open("data.json", "a") as save_file:
            # print(save_file)
            # if len(save_file) == 0:
            #     save_file = 
            # x = json.dumps(p.to_dict())
            # print(type(x))
            # y = json.loads(x)
            # print(type(y))
            # y.update(p.to_dict())
            # data = json.loads(save_file)
            # print(data)
            # data.append(p.to_dict())
            # json.dumps(data)
            # print(type(json.dumps(p.to_dict(), save_file)))
            # json.dump([p.to_dict()], save_file)
    return redirect(url_for('index'))

@app.route('/seed_data', methods=['GET'])
def seed_data():
    url = 'https://www.nbastuffer.com/2019-2020-nba-player-stats/'
    page = requests.get(url)
    populate_database(page.content)
    return redirect(url_for('index'))
        