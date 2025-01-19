from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/visi_misi')
def visi_misi():
    return render_template('visi_misi.html')

@app.route('/sejarah')
def sejarah():
    return render_template('sejarah.html')

@app.route('/media')
def media():
    return render_template('media.html')

if __name__ == '__main__':
    app.run(debug=True)
