# coding: utf-8
from flask import Flask, request, make_response
from flask_basicauth import BasicAuth

from tools import (
    read_form, init_struct, floydWarshall
)


app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'admin'
app.config['BASIC_AUTH_PASSWORD'] = 'toupie'
basic_auth = BasicAuth(app)


@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World'


@app.route('/floyd-warshall', methods=['POST'])
@basic_auth.required
def solve_floydWarshall():
    if request.method == 'POST':
            data = request.form.get('data', None)
            if data is None:
                return "Please Provide CSV format String"
            else:
                problem = read_form(data)
                adj_mat = init_struct(problem)
                new_adj_mat = floydWarshall(adj_mat)
                return str(new_adj_mat)


#@app.route('/authenticate', methods=['GET', 'POST'])
#def authenticate():
#    error = 'Not logged'
#    if request.method == 'POST':
#        if check_auth(request.form['username'],
#            request.form['password']):
            #return log_the_user_in(request.form['username'])
#            error = 'Success'
#        else:
#            error = 'Invalid username/password'
#    return error


if __name__ == '__main__':
        app.run(debug=True,host='0.0.0.0')
