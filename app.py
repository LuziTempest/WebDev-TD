from flask import Flask, render_template, jsonify, request, redirect

app = Flask(__name__)

mahasiswa = [
    {"id": 1, "nama": "Budi Santoso", "nrp": "5025251112", "jurusan": "Informatika"},
    {"id": 2, "nama": "Siti Aminah", "nrp": "5024241243", "jurusan": "Sistem Informasi"}
]

@app.route("/")
def home():
    return render_template()

@app.route("/data")
def data():
    return jsonify()

@app.route("/add", methods=["GET", "POST"])
def add():
    return render_template()

@app.route("/update/<int:id>")
def update(id):
    return render_template()

@app.route("/delete/<int:id>")
def delete(id):
    return redirect()

app.run(debug=True)

