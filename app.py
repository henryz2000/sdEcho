from flask import Flask, render_template, request
#import random
    
my_app = Flask(__name__)

@my_app.route('/', methods = ['GET', 'POST'])
def root():
    print "=====headers====="
    print request.headers
    print "=====method====="
    print request.method
    print "=====args====="
    #print request.args["input1"]
    print request.args
    print "=====form====="
    print request.form
    return render_template('root.html')

@my_app.route('/hello/', methods = ['GET', 'POST'])
def hello():
    return render_template('hello.html', method = request.method, username = request.args["username"])

if __name__ == '__main__':
    my_app.debug = True
    my_app.run()
