from flask import Flask, request, render_template
import random

app = Flask(__name__)

# Generate random number when app starts
secret_number = random.randint(1, 100)
attempts = 0

@app.route('/', methods=['GET', 'POST'])
def game():
    global secret_number, attempts
    message = ""
    status = "playing"  # Added status for better UI control
    
    if request.method == 'POST':
        try:
            guess = int(request.form['guess'])
            attempts += 1
            
            if guess < secret_number:
                message = "Too low! Try a higher number."
                status = "low"
            elif guess > secret_number:
                message = "Too high! Try a lower number."
                status = "high"
            else:
                message = f"Congratulations! You guessed it in {attempts} attempts!"
                status = "won"
                secret_number = random.randint(1, 100)  # Reset game
                attempts = 0
                
        except ValueError:
            message = "Please enter a valid number!"
            status = "error"
            
    return render_template('index.html', message=message, attempts=attempts, status=status)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
