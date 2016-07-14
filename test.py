from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def index(name = 'treehouseeeeee'):
  return 'hello, {}'.format(name)

@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<int:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')

def add(num1,num2):
  return """
<!doctype html>
<html>
<head><title>Adding!</title></head>
<body>
<h1>{} + {} = {}</h1>
</body>
</html>
""".format(num1,num2,num1+num2)

app.run(debug=True, port = 8000, host = '0.0.0.0')