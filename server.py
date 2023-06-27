from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', width=8, row=8)

@app.route('/<height>')
def checkers_height(height):
  return render_template("index.html", width=8, row=int(height))

@app.route('/<width>/<height>/')
def checkers_width_height(width, height):
  return render_template("index.html", width=int(width), row=int(height))

@app.route('/<width>/<height>/<color1>/<color2>')
def checkers_with_colors(width, height,color1, color2):
  return render_template("index.html", width=int(width), row=int(height), color1=color1, color2=color2)

if __name__ == "__main__":
  app.run(debug=True, port=5001)
