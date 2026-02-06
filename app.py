from flask import Flask, render_template, jsonify, request, redirect

app = Flask(__name__)

mahasiswa = [
    {"id": 1, "nama": "Budi Santoso", "nrp": "5025251112", "jurusan": "Informatika"},
    {"id": 2, "nama": "Siti Aminah", "nrp": "5024241243", "jurusan": "Sistem Informasi"}
]

@app.route("/")
def home():
    # Tambahkan dan return fungsi disini
    return render_template()

@app.route("/data")
def data():
    # Tambahkan dan return fungsi disini
    return jsonify()

@app.route("/add", methods=["GET", "POST"])
def add():
    # Tambahkan dan return fungsi disini
    return render_template()

@app.route("/update/<int:id>")
def update(id):
    # Tambahkan dan return fungsi disini
    return render_template()

@app.route("/delete/<int:id>")
def delete(id):
    # Tambahkan dan return fungsi disini
    return redirect()

app.run(debug=True)

