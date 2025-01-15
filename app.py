from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Process form (e.g., save to database, send email, etc.)
    print(f"Contact form submitted: {name}, {email}, {message}")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
