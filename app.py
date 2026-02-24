from flask import Flask, request, jsonify, render_template
import uuid

app = Flask(__name__)
expenses = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/expenses', methods=['GET'])
def get_expenses():
    category = request.args.get('category')
    if category:
        filtered = [e for e in expenses if e['category'].lower() == category.lower()]
        return jsonify(filtered)
    return jsonify(expenses)

@app.route('/expenses', methods=['POST'])
def add_expense():
    data = request.json
    expense = {
        'id': str(uuid.uuid4()),
        'title': data['title'],
        'amount': float(data['amount']),
        'category': data['category']
    }
    expenses.append(expense)
    return jsonify(expense), 201

@app.route('/expenses/<id>', methods=['DELETE'])
def delete_expense(id):
    global expenses
    expenses = [e for e in expenses if e['id'] != id]
    return jsonify({'message': 'Deleted'}), 200

@app.route('/expenses/total', methods=['GET'])
def get_total():
    total = sum(e['amount'] for e in expenses)
    return jsonify({'total': total})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)