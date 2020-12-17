from flask import current_app as app, render_template

@app.route('/', methods=['GET'])
def index():
    context = {}
    return render_template('index.html', **context)