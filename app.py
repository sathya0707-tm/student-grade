from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    result = None

    if request.method == "POST":

        name = request.form.get("name")
        n = int(request.form.get("subjects"))

        marks = []

        for i in range(n):
            mark = int(request.form.get(f"mark{i}"))
            marks.append(mark)

        total = sum(marks)
        average = total / n

        if average >= 90:
            grade = "GRADE A"
        elif average >= 80:
            grade = "GRADE B"
        elif average >= 70:
            grade = "GRADE C"
        elif average >= 60:
            grade = "GRADE D"
        elif average >= 50:
            grade = "GRADE E"
        else:
            grade = "FAILED"

        result = {
            "name": name,
            "marks": marks,
            "total": total,
            "average": average,
            "grade": grade
        }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
