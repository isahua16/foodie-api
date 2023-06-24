from dbhelpers import run_statement
from dbcreds import production_mode
from apihelpers import check_data
from flask import Flask, request, make_response, jsonify
import uuid

app = Flask(__name__)

@app.get('/api/client')
def get_client():
    error = check_data(request.args, ['client_id'])
    if(error != None):
        return make_response(jsonify(error), 400)
    results = run_statement('call get_client(?)', [request.args.get('client_id')])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response('Something went wrong', 500)

@app.post('/api/client')
def post_client():
    error = check_data(request.json, ['email', 'first_name', 'last_name', 'image_url', 'username', 'password'])
    if(error != None):
        return make_response(jsonify(error), 400)
    token = uuid.uuid4().hex
    results = run_statement('call post_client(?,?,?,?,?,?,?)', [request.json.get('email'), request.json.get('first_name'), request.json.get('last_name'), request.json.get('image_url'), request.json.get('username'), request.json.get('password'), token])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response('Something went wrong', 500)

@app.patch('/api/client')
def patch_client():
    error = check_data(request.headers, ['token'])
    if(request.is_json == False):
        return make_response(jsonify("You must send data"), 415)
    if(error != None):
        return make_response(jsonify(error), 400)
    results = run_statement('call patch_client(?,?,?,?,?,?,?)', [request.json.get('email'), request.json.get('first_name'), request.json.get('last_name'), request.json.get('image_url'), request.json.get('username'), request.json.get('password'), request.headers.get('token')])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response('Something went wrong', 500)
    
@app.delete('/api/client')
def delete_client():
    error_data = check_data(request.json, ['password'])
    error_headers = check_data(request.headers, ['token'])
    if(error_data != None):
        return make_response(jsonify(error_data), 400)
    elif(error_headers != None):
        return make_response(jsonify(error_headers), 400)
    results = run_statement('call delete_client(?,?)', [request.headers.get('token'),request.json.get('password')])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response('Something went wrong', 500)

if(production_mode == True):
    print('Running in production mode')
    import bjoern # type: ignore
    bjoern.run(app, '0.0.0.0', 5000)
else:
    print('Running in development mode')
    from flask_cors import CORS
    CORS(app)
    app.run(debug=True)
    CORS(app)
