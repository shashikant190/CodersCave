from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def calculator():
    return render_template('index.html', expression="")

@app.route('/calc', methods=['POST'])
def calculate():
    expression = request.form['expression']

    try:
        result = eval(expression)
    except Exception as e:
        result = "Error"

    return render_template('index.html', expression=expression, result=result)

if __name__ == '__main__':
    app.run(debug=True)
