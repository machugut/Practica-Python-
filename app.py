from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def grade_checker():
    result = None
    score = None

    if request.method == "POST":
        score = int(request.form["score"])

        # IF / ELIF / ELSE — the core concept being taught
        if score >= 90:
            result = {"grade": "A", "message": "Excellent work!", "emoji": "🏆"}
        elif score >= 75:
            result = {"grade": "B", "message": "Good job!", "emoji": "😊"}
        elif score >= 60:
            result = {"grade": "C", "message": "You passed.", "emoji": "👍"}
        elif score >= 40:
            result = {"grade": "D", "message": "Need more study.", "emoji": "📚"}
        else:
            result = {"grade": "F", "message": "Please retake the exam.", "emoji": "😬"}

    return render_template("index.html", result=result, score=score)

if __name__ == '__main__':
    app.run(debug=True, port=5000)