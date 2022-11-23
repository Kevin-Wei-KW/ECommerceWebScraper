from flask import Flask, render_template, url_for
import scrape
# follows directory structure to get html and css files
app = Flask(__name__, template_folder='templates', static_folder='staticFiles')


@app.route('/')
def index():
    return render_template('test.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/scrape/', methods=['POST'])
def activate_scrape():
    scrape.main()
    return render_template('test.html')


if __name__ == '__main__':
    app.run()



# CMD
# set FLASK_APP=index.py
# $env:FLASK_APP = "index.py"
# flask run
