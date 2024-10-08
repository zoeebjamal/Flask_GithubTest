from flask import Flask, render_template, request
app = Flask(__name__)

# route 1 (page 1) #landing page
@app.route('/')
def home():
    return render_template('index.html')

#route 2 (page 2) #user
@app.route('/user/<name>')
def user(name):
    name = request.args.get('username')
    return render_template('user.html', username=name)

#route 3 (page 3) #user
@app.route('/stocks')
def stocks():
    stocks = ['Apple', 'Microsoft']
    return render_template('stocks.html', stocks=stocks)

@app.route('/stocks')
def team3m2():
    print("Zoeeb J")



if __name__ == "__main__": app.run(debug=True)






# from flask import Flask
# app = Flask(__name__)
# @app.route("/") 
# def hello_world(): 
#     return "Hello, World!"
# if __name__ == "__main__": app.run(debug=True)



# @app.route('/user/<name>')
# def user(name):
#     username = request.args.get('username')
#     return render_template('user.html', username=username)

# @app.route('/stocks')
# def stocks():
#     stocks = ['Apple', 'Microsoft']
#     return render_template('stocks.html', stocks=stocks)