from flask import Flask, request

'''
Ten projekt to aplikacja webowa w Flasku,
 która implementuje grę „Zgadnij liczbę”, 
 gdzie komputer zgaduje liczbę wybraną przez użytkownika z przedziału od 0 do 1000.
Użytkownik informuje komputer, czy jego zgadywana liczba jest „Za duża”, „Za mała” czy „Trafiona”. 
Gra trwa maksymalnie 10 ruchów, a zakres zgadywania zawęża się przy każdej odpowiedzi użytkownika.
'''

HTML = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Guess the number</title>
</head>
<body>
<h1>Imagine number between 0 and 1000</h1>
<form action="" method="POST">
    <input type="hidden" name="min" value="{}">
    <input type="hidden" name="max" value="{}">
    <input type="submit" value="OK">
</form>
</body>
</html>
'''

HTML_GUESS = '''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Guess the number</title>
</head>
<body>
<h1> It is number {guess} </h1>
<form action="" method="POST">
<input type="submit" name="user_input" value="Too big">
<input type="submit" name="user_input" value="Too small">
<input type="submit" name="user_input" value="You won">
<input type="hidden" name="max" value="{max}">
<input type="hidden" name="min" value="{min}">
<input type="hidden" name="guess" value="{guess}">
</form>
</body>
</html>
'''

HTML_WIN = '''
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Guess the number</title>
</head>
<body>
<h1> I guessed! Your number is {guess} </h1>
</body>
</html>
'''


app = Flask("Guess")

@app.route("/", methods=["GET", "POST"])
def guess():
    if request.method == "GET":
        return HTML.format(0, 1000)
    else:
        min_number = int(request.form.get("min"))
        max_number = int(request.form.get("max"))
        user_input = request.form.get("user_input")
        guess_number = int(request.form.get("guess",500))
        if user_input == "Too big":
            max_number = guess_number
        elif user_input == "Too small":
            min_number = guess_number
        elif user_input == "You won":
            return HTML_WIN.format(guess = guess_number)

        guess_number = (max_number - min_number) // 2 + min_number

        return HTML_GUESS.format(guess = guess_number, min = min_number, max = max_number)


if __name__ == '__main__':
    app.run()