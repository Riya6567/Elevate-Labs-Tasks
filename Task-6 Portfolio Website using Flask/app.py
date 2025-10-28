from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "riya_portfolio_secret"

@app.route('/')
def home():
    return render_template('index.html')

# Contact form route (POST)
@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    flash(f"Thanks {name}! Your message has been received.", "success")
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
