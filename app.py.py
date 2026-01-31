from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template directly in Python
html = """
<!doctype html>
<html>
    <head>
        <title>Python Calculator</title>
    </head>
    <body>
        <h1>Simple Calculator</h1>
        <form method="POST">
            Number 1: <input type="text" name="num1"><br><br>
            Number 2: <input type="text" name="num2"><br><br>
            Operation:
            <select name="operation">
                <option value="add">Add</option>
                <option value="subtract">Subtract</option>
                <option value="multiply">Multiply</option>
                <option value="divide">Divide</option>
            </select><br><br>
            <input type="submit" value="Calculate">
        </form>
        {% if result is not none %}
            <h2>Result: {{ result }}</h2>
        {% endif %}
    </body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        try:
            num1 = float(request.form.get("num1"))
            num2 = float(request.form.get("num2"))
            operation = request.form.get("operation")
            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                result = num1 / num2
        except Exception as e:
            result = "Error: " + str(e)
    return render_template_string(html, result=result)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
