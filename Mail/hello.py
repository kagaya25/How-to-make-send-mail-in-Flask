from flask import Flask
from flask_mail import Mail, Message
#Step 1 : pip install Flask-Mail
app =Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'put you username here' # Step 2 :out your username here 
app.config['MAIL_PASSWORD'] = 'put your password here'# Step 3: Put your password here  
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
   msg = Message('Hello', sender = 'put your sender here', recipients = ['put your recipients here']) # Step4: sender add your gmail Step 5: put your recipients
   msg.body = "Hello Flask message sent from Flask-Mail" #Step 6: Change your mail 
   mail.send(msg)
   return "Sent"

if __name__ == '__main__':
   app.run(debug = True)

#Step 7: https://myaccount.google.com/lesssecureapps