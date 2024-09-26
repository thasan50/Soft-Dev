## K11: Some Things Never Change
### Due: 2024-09-26r before class

Your Trio Mission:

1. In a new directory in your workshop, save a copy of the demo for using flask to serve static files.
1. As a team...
  - Familiarize yourself with the app directory structure and the files' content.
  - Note anything notable.
  - Predict expected behaviors.
  - Spin up your website on localhost and reconcile behavior with prediction.
  - Record your notes in `readme` in app's root directory.
1. Once your team has done this, compose and store another html file named `fixie.html` (containing some html to render your team name and roster) so that flask can serve it staticly.

<br>

DELIVERABLES:
* Save to workshop as indicated.
* Each teammate should submit matching sourcecode.

NOTES and PREDICTIONS:
  - When you add the second app route to the url that appears after running app.py, the function h will be called on the website with its corresponding message in terminal. The standard route would give you "no hablo queso", while the second route will give you a random decimal in string form
  - "foo" is only plaintext, and should appear on the website without any additional text decoration or organization
  - foo.html has html tags, though the text is commented out. If the text wasn't commented out, I expect that it would look much the same as "foo" does when the link is clicked, just with a slightly different font.
  <br>
RESULTS:
  - We found the first prediction to be true in class
  <s>- Firefox can’t establish a connection to the server at localhost:5000. I suspect this needs to be done on a lab computer specifically. When I open foo and foo.html without clicking the links, the results line up with my predictions. </s>
  - It turns out that I need to activate app.py with python first before the local host links work. The other predictions lined up with my expectations

```
path/to/myworkshop$ tree 11_flask-static
.
├── app.py
├── readme
└── static
    ├── foo
    ├── foo.html
    └── fixie.html
```

<br>

[related](https://ukulelemagazine.com/lessons/uke-lesson-3-chords-and-the-truth-country-songwriting-legend-harlan-howard)  
[related](https://en.wikipedia.org/wiki/Plain_text)  
