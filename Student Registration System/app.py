from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/students')
def students():
    students_data = [
        {"roll":101,"name":"Arjun","dept":"IT","year":"3"},
        {"roll":102,"name":"Priya","dept":"CSE","year":"2"},
        {"roll":103,"name":"Rahul","dept":"ECE","year":"4"},
        {"roll":104,"name":"Sneha","dept":"IT","year":"1"},
        {"roll":105,"name":"Kiran","dept":"EEE","year":"2"},
        {"roll":106,"name":"Anjali","dept":"CSE","year":"3"},
        {"roll":107,"name":"Vikram","dept":"MECH","year":"4"},
        {"roll":108,"name":"Deepika","dept":"IT","year":"1"},
        {"roll":109,"name":"Surya","dept":"ECE","year":"2"},
        {"roll":110,"name":"Divya","dept":"CSE","year":"3"}
    ]

    return render_template(
        'students.html',
        students=students_data
    )

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)