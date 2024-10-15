  # Ivan Gontchar
  # Belugas (Ivan, Colyi, Tanzeem)
  # SoftDev
  # K16: Take and Keep
  # 2024-10-09
  # time spent: 3.5 hours

from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)    #create Flask object

# makin' a supa-secret key
app.secret_key = "1234";

# @app.route(("/"), methods=['GET', 'POST'])
# def home():
#     if 'username' in session:
#         return "Welcome back " + session['username']
#     return "Hello Stranger."


@app.route(("/") , methods=['GET', 'POST'])
def login():
    # we though it is a good idea to always clear username from session if someone
    # wanders back to the login page via buttons or with the URL. For example, if they were at
    # the reponse page and tried to go back to the home page, and then GO BACK to the
    # response page, it would now remove their info and send them to the login page via
    # the code in response, since without this line, session would still have their username
    # and it would give them a response, which we thought would be weird
    session.pop('username', None)
    # if there is a submission with post...
    if request.method == 'POST':
        # ...then we put their username into our session
        session['username'] = request.form['username']

        # we tried this print below because we thought that request.cookies.get
        # was equivalent to request.form, based on the notes, however, this prints
        # "None". Perhaps the notes implied that by function it would be the same
        # but there are extra steps to set up the cookies
        # print(request.cookies.get('username'))

        # print(session['username'])

        # since user inputed something, send them to the response page
        return redirect(url_for('response'))

    # otherwise we display the login page
    return render_template( 'login.html' )

@app.route("/response", methods=['GET', 'POST'])
def response():
    # if we have info on the person, aka their username...
    if 'username' in session:
        # if there is a submission with post...
        if request.method == 'POST':
            # ...then the user pressed the button to logout, and we send them to the logout page
            return redirect(url_for('logout'))
        # otherwise we display the response page
        return render_template( 'response.html', username = session['username'])
    # this is something we added in later since we noticed if someone tried to be
    # sneaky and add response to the url from say the home page, it would give an error because there was
    # no username in session, so if they try that without any input, they get sent
    # back to the login screen
    return redirect(url_for('login'))

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    # if we have info on the person, aka their username...
    if 'username' in session:
        # if there is a submission with post...
        if request.method == 'POST':
            # if they pressed the submission named "logout"...
            if request.form.get("logout") is not None:
                # ...then the user is logging out, and we take their info out of the session...
                session.pop('username', None)
                # ... and then we send them back to the login page
                return redirect(url_for('login'))
            # ...otherwise they pressed the submission named "back"...
            else:
                # ...and then we send them back to the response page
                return redirect(url_for('response'))
        # send them back to the login page
        return render_template( 'logout.html', username = session['username'])
    # this is something we added in later since we noticed if someone tried to be
    # sneaky and add logout to the url, it would give an error because there was
    # no username in session, so if they try that without any input, they get sent
    # back to the login screen
    return redirect(url_for('login'))


if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
