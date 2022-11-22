from flask import Flask, render_template
import scrape
# follows directory structure to get html and css files
app = Flask(__name__, template_folder='templates', static_folder='staticFiles')


@app.route('/')
def index():
    return render_template('test.html')


@app.route('/scrape/')
def activate_scrape():
    scrape.main()


if __name__ == '__main__':
    app.run()



# CMD
# set FLASK_APP=index.py
# $env:FLASK_APP = "index.py"
# flask run
