
#! /usr/bin/python3
'''Basic flask web server
-Creates a route on 0.0.0.0/5000
'''
from flask import Flask

app = Flask(__name__)

'''Defining the route'''
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

'''Starting the server'''
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
    