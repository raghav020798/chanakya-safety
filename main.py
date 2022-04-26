from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message


app = Flask(__name__)
mail = Mail(app) # instantiate the mail class
   
# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route("/")
def index():     


    return render_template("index.html")



@app.route("/final", methods=['POST'])
def form():
    
    name =request.form.get("name")
    designation=request.form.get("designation")
    number=request.form.get("number")
    message=request.form.get("message")
    print(name,designation,number)
    msg = Message(
                'Hello this is an automated mail',
                sender ='',
                recipients = ['']
               )
    msg.body = 'name: {} \ndesignation: {} \nnumber  {} \nmessage {}'.format(name,designation,number,message)
    mail.send(msg)
    return redirect(request.referrer)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)