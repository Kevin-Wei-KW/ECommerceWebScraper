from flask import Flask, render_template, url_for, redirect
import scrape
# follows directory structure to get html and css files
app = Flask(__name__, template_folder='templates', static_folder='staticFiles')
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    return render_template('test.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/scrape/', methods=['GET', 'POST'])
def activate_scrape():
    scrape.main()
    return redirect("/")


@app.route('/item/<name>', moethods=['POST'])
def show_item(name):
    item = scrape.item_list(scrape.item_index[name])  # gets item from list with stored index in dict
    scrape.create_item_page(item)
    return render_template('item.html')


# def run_app():
#     app.run()


if __name__ == '__main__':
    app.run()



# CMD
# set FLASK_APP=index.py
# $env:FLASK_APP = "index.py"
# flask run
