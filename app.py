from flask import Flask, render_template

app = Flask(__name__)

def getApiUrl():
  cat_url = 'https://cataas.com/cat/says/hello%20world!'
  return cat_url


@app.route('/')
def hello():
  message = "Congratulations on your app!"
  apiUrl = getApiUrl()
  return render_template('index.html',
    message=message,
    apiUrl=apiUrl
  )
