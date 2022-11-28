from flask import Flask, render_template, url_for, redirect
import scrape
# follows directory structure to get html and css files
app = Flask(__name__, template_folder='templates', static_folder='staticFiles')
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/scrape/', methods=['GET', 'POST'])
def activate_scrape():
    scrape.main()
    return redirect("/")

@app.route('/items/')
def show_item():
    return render_template('item.html')

@app.route('/item/<name>', methods=['POST', 'GET'])
def create_item(name):
    item = scrape.item_list[scrape.item_index[name]]  # gets item from list with stored index in dict
    item_page = scrape.create_item_page(item)
    scrape.insert_item_page(item_page)
    return redirect("/items/")


# def run_app():
#     app.run()


if __name__ == '__main__':
    app.run()



# CMD
# set FLASK_APP=index.py
# $env:FLASK_APP = "index.py"
# flask run
#
# pip install pipreqs
# python -m  pipreqs.pipreqs --encoding utf-8  C:\Users\Kevin\Desktop\Dev\Webscraper
