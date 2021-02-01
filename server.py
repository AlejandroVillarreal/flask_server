from flask import Flask, render_template, request
import csv
app = Flask(__name__)
print(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/<string:page_name>')
def render_page(page_name):
    return render_template(page_name)


@app.route('/<username>/<int:post_id>')
def show_username(username=None,post_id=None):
    return render_template('index.html',name=username,post_id=post_id)

@app.route('/submit_form',methods=['POST','GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        write_to_file(data)
        return render_template('thankyou.html')
    else:
        return 'something went wrong :('

def write_to_file(data):
    with open('database.csv',newline='',mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])