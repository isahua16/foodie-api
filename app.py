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

@app.post('/api/client-login')
def post_client_login():
    error = check_data(request.json, ['email', 'password'])
    if(error != None):
        return make_response(jsonify(error), 400)
    token = uuid.uuid4().hex
    results = run_statement('call post_client_login(?,?,?)', [request.json.get('email'), request.json.get('password'), token])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response('Something went wrong', 500)

@app.delete('/api/client-login')
def delete_client_login():
    error = check_data(request.headers, ['token'])
    if(error != None):
        return make_response(jsonify(error), 400)
    results = run_statement('call delete_client_login(?)', [request.headers.get('token')])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response('Something went wrong', 500)    

@app.get('/api/restaurant')
def get_restaurant():
    error = check_data(request.args, ['restaurant_id'])
    if(error != None):
        return make_response(jsonify(error), 400)
    results = run_statement('call get_restaurant(?)', [request.args.get('restaurant_id')])
    if(type(results) == list and results != []):
        return make_response(jsonify(results), 200)
    elif(type(results) == list and results == []):
        return make_response('Restaurant does not exist', 400)
    else:
        return make_response('Something went wrong', 500)

@app.post('/api/restaurant')
def post_restaurant():
    error = check_data(request.json, ['email', 'name', 'address', 'phone', 'city', 'profile_url', 'banner_url', 'password', 'bio'])
    if(error != None):
        return make_response(jsonify(error), 400)
    token = uuid.uuid4().hex
    results = run_statement('call post_restaurant(?,?,?,?,?,?,?,?,?,?)', [request.json.get('email'), request.json.get('name'), request.json.get('address'), request.json.get('phone'), request.json.get('city'), request.json.get('profile_url'), request.json.get('banner_url'), request.json.get('password'), token, request.json.get('bio')])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response('Something went wrong', 500)

@app.patch('/api/restaurant')
def patch_restaurant():
    error = check_data(request.headers, ['token'])
    if(request.is_json == False):
        return make_response(jsonify("You must send data"), 415)
    if(error != None):
        return make_response(jsonify(error), 400)
    results = run_statement('call patch_restaurant(?,?,?,?,?,?,?,?,?,?)', [request.json.get('email'), request.json.get('name'), request.json.get('address'), request.json.get('phone'), request.json.get('city'), request.json.get('profile_url'), request.json.get('banner_url'), request.json.get('password'), request.headers.get('token'), request.json.get('bio')])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response('Something went wrong', 500)
    
@app.delete('/api/restaurant')
def delete_restaurant():
    error_data = check_data(request.json, ['password'])
    error_headers = check_data(request.headers, ['token'])
    if(error_data != None):
        return make_response(jsonify(error_data), 400)
    elif(error_headers != None):
        return make_response(jsonify(error_headers), 400)
    results = run_statement('call delete_restaurant(?,?)', [request.json.get('password'), request.headers.get('token')])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response('Something went wrong', 500)

@app.get('/api/restaurants')
def get_restaurants():
    results = run_statement('call get_restaurants()')
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response('Something went wrong', 500)

@app.post('/api/restaurant-login')
def post_restaurant_login():
    error = check_data(request.json, ['email', 'password'])
    if(error != None):
        return make_response(jsonify(error), 400)
    token = uuid.uuid4().hex
    results = run_statement('call post_restaurant_login(?,?,?)', [request.json.get('email'), request.json.get('password'), token])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response('Something went wrong', 500)

@app.delete('/api/restaurant-login')
def delete_restaurant_login():
    error = check_data(request.headers, ['token'])
    if(error != None):
        return make_response(jsonify(error), 400)
    results = run_statement('call delete_restaurant_login(?)', [request.headers.get('token')])
    if(type(results) == list and results[0]['deleted_rows'] == 1):
        return make_response(jsonify(results), 200)
    elif(type(results) == list and results[0]['deleted_rows'] == 0):
        return make_response('The token is invalid', 400)
    else:
        return make_response('Something went wrong', 500)

@app.get('/api/menu')
def get_menu():
    error = check_data(request.args, ['restaurant_id'])
    if(error != None):
        return make_response(jsonify(error), 400)
    results = run_statement('call get_menu(?)', [request.args.get('restaurant_id')])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response('Something went wrong', 500)

@app.post('/api/menu')
def post_menu():
    error_data = check_data(request.json, ['description', 'image_url', 'name', 'price'])
    error_headers = check_data(request.headers, ['token'])
    if(error_data != None):
        return make_response(jsonify(error_data), 400)
    elif(error_headers != None):
        return make_response(jsonify(error_headers), 400)
    results = run_statement('call post_menu(?,?,?,?,?)', [request.headers.get('token'), request.json.get('description'), request.json.get('image_url'), request.json.get('name'), request.json.get('price')])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response('Something went wrong', 500)

@app.patch('/api/menu')
def patch_menu():
    error_data = check_data(request.json, ['menu_id'])
    error_headers = check_data(request.headers, ['token'])
    if(error_data != None):
        return make_response(jsonify(error_data), 400)
    elif(error_headers != None):
        return make_response(jsonify(error_headers), 400)
    results = run_statement('call patch_menu(?,?,?,?,?,?)', [request.headers.get('token'), request.json.get('description'), request.json.get('image_url'), request.json.get('name'), request.json.get('price'), request.json.get('menu_id')])
    if(type(results) == list and results[0]['updated_rows'] == 1):
        return make_response(jsonify(results), 200)
    elif(type(results) == list and results[0]['updated_rows'] == 0):
        return make_response('Menu item does not exist', 500)
    else:
        return make_response('Something went wrong', 500)

@app.delete('/api/menu')
def delete_menu():
    error_data = check_data(request.json, ['menu_id'])
    error_headers = check_data(request.headers, ['token'])
    if(error_data != None):
        return make_response(jsonify(error_data), 400)
    elif(error_headers != None):
        return make_response(jsonify(error_headers), 400)
    results = run_statement('call delete_menu(?,?)', [request.headers.get('token'), request.json.get('menu_id')])
    if(type(results) == list and results[0]['deleted_rows'] == 1):
        return make_response(jsonify(results), 200)
    elif(type(results) == list and results[0]['deleted_rows'] == 0):
        return make_response('Menu item does not exist', 500)
    else:
        return make_response('Something went wrong', 500)

@app.post('/api/client-order')
def post_client_order():
    error_data = check_data(request.json, ['menu_items', 'restaurant_id'])
    error_headers = check_data(request.headers, ['token'])
    if(error_data != None):
        return make_response(jsonify(error_data), 400)
    elif(error_headers != None):
        return make_response(jsonify(error_headers), 400)
    results = run_statement('call post_client_order(?,?,?)', [request.headers.get('token'), str(request.json.get('menu_items')), request.json.get('restaurant_id')])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response('Something went wrong', 500)
    
@app.get('/api/client-order')
def get_client_order():
    error = check_data(request.headers, ['token'])
    if(error != None):
        return make_response(jsonify(error), 400)
    results = run_statement('call get_client_order(?,?,?)', [request.headers.get('token'), request.args.get('is_confirmed'), request.args.get('is_complete')])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response('Something went wrong', 500)

@app.get('/api/restaurant-order')
def get_restaurant_order():
    error = check_data(request.headers, ['token'])
    if(error != None):
        return make_response(jsonify(error), 400)
    results = run_statement('call get_restaurant_orders(?,?,?)', [request.headers.get('token'), request.args.get('is_confirmed'), request.args.get('is_complete')])
    if(type(results) == list):
        return make_response(jsonify(results), 200)
    else:
        return make_response('Something went wrong', 500)

@app.patch('/api/restaurant-order')
def patch_restaurant_order():
    error_data = check_data(request.json, ['order_id'])
    error_headers = check_data(request.headers, ['token'])
    if(error_data != None):
        return make_response(jsonify(error_data), 400)
    elif(error_headers != None):
        return make_response(jsonify(error_headers), 400)
    results = run_statement('call patch_restaurant_order(?,?,?,?)', [request.headers.get('token'), request.json.get('order_id'), request.json.get('is_confirmed'), request.json.get('is_complete')])
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
