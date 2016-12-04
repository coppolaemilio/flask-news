from flask import Flask, render_template, request
app = Flask(__name__)

# Mock DB
users = [
    {"id":0, "username": "coppolaemilio"},
    {"id":1, "username": "pepitopapelito"}
]

comments = [
    {"entry_id": 0, "user":0, "text": "hello world!"},
    {"entry_id": 0, "user":1, "text": "It works!"},
    {"entry_id": 2, "user":1, "text": "It works!"}
]

entries = [
    {"id":0, "title":"Google, a search engine", "url":"http://google.com","points":5, "user": 0},
    {"id":1, "title":"Fuck the other!", "url":"http://duckduckgo.com","points":2,  "user": 1},
    {"id":2, "title":"This website's inspiration", "url":"http://news.ycombinator.com","points":0,  "user": 0}
]


# Routing and controllers
@app.route("/")
def front_page():
    # Get the comment count of each entry
    comment_count = []
    for i in entries:
        comment_count.append(0)

    for entry in entries:
        for comment in comments:
            if entry["id"] == comment["entry_id"]:
                comment_count[entry["id"]] += 1

    return render_template('index.html', entries = entries, users = users, comment_count = comment_count)

# Running the app
if __name__ == "__main__":
    app.run(debug = True)