from flask import Flask
from flask import request, jsonify

app = Flask(__name__)

# def validate_post_data(data: dict) -> bool



# GET
@app.route('/', methods=['GET'] )
def hello():
    return 'Hello World!'

@app.route('/add', methods=['GET'] )
def add():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
    except (TypeError, ValueError):
        return 'a or b are not numbers'
    return str(a + b)

@app.route('/dec', methods=['GET'] )
def dec():
    try:
        a = float(request.args.get('a'))
        b = float(request.args.get('b'))
    except (TypeError, ValueError):
        return 'a or b are not numbers'
    return str(a - b)    

@app.route('/api', methods=['GET','POST'])
def api():
    if request.method == 'GET':
        return jsonify({'status' : 'test'})
    elif request.method == 'POST' :

        return jsonify({'status' : 'OK!'})



def main():
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    main()