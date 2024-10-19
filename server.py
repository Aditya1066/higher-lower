from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def index():
    return f'<h1>Guess a number between 0 and 9</h1>' \
           f'<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


r_num = random.randint(0,9)
print(r_num)

@app.route('/<int:guess>')
def guess(guess):
    if guess == r_num:
        return f'<h1 style="color: green;">Yay! You found me</h1>' \
                f'<img src = "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExaDBmanZkeTJveWIxcGZ4MGdxeXFuZjZzemVocXc1aDFoc3BiMHd5NyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Bu6qM4P4WVmBIDSUh5/giphy.gif">'
    elif guess < r_num:
        return f'<h1 style="color: red;">Too low! Guess Higher</h1>' \
                f'<img src = "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExa3YxNTQ3OHE2eGE5Ymg1OTZ3YXhhdmVjc3Y2aGxheDZ5N2JlZmd2YyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/7SF5scGB2AFrgsXP63/giphy.gif">'
    elif guess > r_num:
        return f'<h1 style="color: blue;">Too High! Guess Lower</h1>' \
               f'<img src = "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExajU0eHg2MWt1azJvdnd6azh4cHR3NHVieDY0dGo5ZjA4bHdrcmJyNSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fBEMsUeGHdpsClFsxM/giphy.gif">'


if __name__ == '__main__':
    app.run(debug=True)
