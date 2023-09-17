from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length, include_numbers, include_lowercase, include_uppercase, include_symbols):
    characters = ""
    if include_numbers:
        characters += string.digits
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_symbols:
        characters += '~!@#$%^&*()_;.,/{}[]()*-+'

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        password_length = int(request.form['password_length'])
        include_numbers = 'include_numbers' in request.form
        include_lowercase = 'include_lowercase' in request.form
        include_uppercase = 'include_uppercase' in request.form
        include_symbols = 'include_symbols' in request.form
        quantity = int(request.form['quantity'])

        passwords = []
        for _ in range(quantity):
            password = generate_password(password_length, include_numbers, include_lowercase, include_uppercase, include_symbols)
            passwords.append(password)

        return render_template('index.html', passwords=passwords)

    return render_template('index.html', passwords=[])

if __name__ == '__main__':
    app.run(debug=True)

