from flask import Flask, render_template


app = Flask(__name__)
app.secret_key = 'secret 1 development key'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/Suzhou')
def suzhou_index():
    return 'Hi Suzhou'



if __name__ == '__main__':
    app.run(debug = False)
