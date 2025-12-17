from flask import Flask, request, jsonify

app = Flask(__name__)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
        #pass
    return a / b

@app.route('/calc', methods=['POST'])
def calculate():
    """
    Endpoint for calculation.
    Expected JSON: {"operation": "add", "a": 10, "b": 5}
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    operation = data.get("operation")
    try:
        a = float(data.get("a"))
        b = float(data.get("b"))
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid numbers"}), 400

    try:
        if operation == "add":
            result = add(a, b)
        elif operation == "subtract":
            result = subtract(a, b)
        elif operation == "multiply":
            result = multiply(a, b)
        elif operation == "divide":
            result = divide(a, b)
        else:
            return jsonify({"error": "Unsupported operation"}), 400
        
        return jsonify({"result": result}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    # Вразливість для Bandit: debug=True не має бути в продакшні
    app.run(host='0.0.0.0', port=5000, debug=True)
