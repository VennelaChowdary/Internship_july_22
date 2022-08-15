from ast import And
from flask import Flask, render_template, request
import re


app = Flask(__name__,template_folder='template')


@app.route('/')
def index_page():
    return "Welcome to Regular expression clone"


@app.route('/match_us', methods = ['GET', 'POST'])
def home_page():
    
    if request.method == 'POST':
        pat = request.form['in_re']
        str = request.form['in_str']

        pattern = re.compile(pat)
        n = str

        total = len(pattern.findall(n))
        matched = pattern.findall(n)

        return render_template("index.html", a = total, b = matched, c = pat, n = str)
        return render_template("index.html")

def main(argv):
    reloader = '--reloader' in argv
    print('Starting with reloader={}'.format(reloader))
    app.run(host='0.0.0.0', port=8080, debug=True, use_reloader=reloader)

if __name__ == '__main__':
    app.run()