# Clyde 'Thluffy' Sinclair
# SoftDev
# September 2024

from flask import Flask
app = Flask(__name__)          # ... initializing a flask app

@app.route("/")                # ... routing app to directory
def hello_world():
    print(__name__)            # ...  print name of module, which is "__main__", in terminal
    return "No hablo queso!"   # ... prints the string into website

app.run()                      # ... runs app
                
