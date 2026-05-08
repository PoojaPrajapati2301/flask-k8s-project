from flask import Flask, render_template_string

app = Flask(__name__)

votes = {"Cats": 0, "Dogs": 0}

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Voting App</title>
</head>
<body>

<h1>Version 2</h1>

<form action="/vote/cats">
    <button type="submit">Vote Cats</button>
</form>

<form action="/vote/dogs">
    <button type="submit">Vote Dogs</button>
</form>

<h2>Results</h2>

<p>Cats: {{cats}}</p>
<p>Dogs: {{dogs}}</p>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(
        HTML,
        cats=votes["Cats"],
        dogs=votes["Dogs"]
    )

@app.route('/vote/cats')
def vote_cats():
    votes["Cats"] += 1
    return home()

@app.route('/vote/dogs')
def vote_dogs():
    votes["Dogs"] += 1
    return home()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
