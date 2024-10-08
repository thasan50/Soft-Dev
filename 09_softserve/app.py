# Tanzeem Hasan
# Cheerio (Tanzeem, Leon, Naomi)
# SoftDev
# K09: Putting it Together
# 2024-09-24
# time spent: 1.5 hours

import csv
import random
from flask import Flask

def read_csv(csvfile):
    with open(csvfile, newline='') as csv_file:
        header = next(csv_file)
        percent = 0.0
        content = csv.reader(csv_file)
        dic = {}
        for row in content:
            percent += float(row[1])
            percent = round(percent, 1)
            dic[percent] = row[0]

        dic.popitem()
        #print(dic) key: value --> percentage: occupation
        return dic
    
def choose_random(csvfile):
    data = read_csv(csvfile)
    keys = [key for key in data.keys()]
    random_num = random.random() * 99.8 #random_num is the chance
    for i in range(len(keys)):
        if keys[i] > random_num:
            return data[keys[i-1]] 
            #when percentage is greater than random_num, it is the right occupation

# keep function definitions above @app.route("/")

app = Flask(__name__)
@app.route("/")

def occupation_chooser():
    st = "<h2> Occupation chosen: " + choose_random('occupations.csv') + "</h2>"
    data = read_csv('occupations.csv')
    keys = [key for key in data.keys()]
    output = "<h2>"
    for i in range(len(keys)):
        output += data[keys[i-1]]
        output += "<br>"
    output += "</h2>"
    heading = '''
    # Tanzeem Hasan <br>
# Cheerio (Tanzeem, Leon, Naomi) <br>
# SoftDev <br>
# K09: Putting it Together <br>
# 2024-09-24 <br>
# time spent: 1.5 hours<br><br>'''
    return heading + st + "<br>" + output

# to do-- display list of occupations, display TPNG+roster(???)

if __name__ == "__main__":      
    app.debug = True            
    app.run()