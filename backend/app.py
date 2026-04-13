from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Backend Running Successfully"

# ---------------- CALCULATOR ---------------- #

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.json

        print("CALCULATE DATA:", data)

        if not data:
            return jsonify({'error': 'No data received'})

        num1 = float(data.get('num1', 0))
        num2 = float(data.get('num2', 0))
        operation = data.get('operation', '')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return jsonify({'error': 'Division by zero'})
            result = num1 / num2
        else:
            return jsonify({'error': 'Invalid operation'})

        return jsonify({'result': result})

    except Exception as e:
        print("CALC ERROR:", str(e))
        return jsonify({'error': str(e)})


# ---------------- LINKED LIST ---------------- #

class Node:
    def __init__(self, data):
        self.data = int(data)
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def delete(self, data):
        data = int(data)
        temp = self.head

        if temp and temp.data == data:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != data:
            prev = temp
            temp = temp.next

        if temp:
            prev.next = temp.next

    def search(self, data):
        data = int(data)
        temp = self.head
        while temp:
            if temp.data == data:
                return True
            temp = temp.next
        return False

    def display(self):
        result = []
        temp = self.head
        while temp:
            result.append(temp.data)
            temp = temp.next
        return result


ll = LinkedList()

@app.route('/linkedlist', methods=['POST'])
def linked_list():
    try:
        data = request.json

        print("LL DATA:", data)

        if not data:
            return jsonify({'error': 'No data received'})

        operation = data.get('operation')
        value = data.get('value')

        if operation == 'insert':
            ll.insert(value)
            return jsonify({'list': ll.display()})

        elif operation == 'delete':
            ll.delete(value)
            return jsonify({'list': ll.display()})

        elif operation == 'search':
            found = ll.search(value)
            return jsonify({'found': found})

        else:
            return jsonify({'error': 'Invalid operation'})

    except Exception as e:
        print("LL ERROR:", str(e))
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)