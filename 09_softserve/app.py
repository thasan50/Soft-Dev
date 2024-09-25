# Tanzeem Hasan
# Cheerio (Tanzeem, Leon, Naomi)
# SoftDev
# K09 -- Putting it Together
# 9/24/2024
# time spent: 1.5 hours

from flask import Flask
import numbercruncher

app = Flask(__name__)           #create instance of class Flask

@app.route("/")                 #assign fxn to route
def hello_world():
    return '''Tanzeem Hasan <br>
Cheerio (Tanzeem, Leon, Naomi) <br>
SoftDev <br>
K09 -- Putting it Together <br>
9/24/2024 <br>
time spent: 1.5 hours<br>''' + numbercruncher.func()

if __name__ == "__main__":      # true if this file NOT imported
    app.debug = True            # enable auto-reload upon code change
    app.run()