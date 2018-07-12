import os

from flask import Flask, session, render_template, request
from flask_session import Session
from models import *
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
       return render_template("index.html")

@app.route('/register', methods=['POST'])
def register():
    '''Login Or Register new user.'''


    act = request.form.get('signin')
    if act != 'SIGN IN':
        login_name = request.form.get('login_name')
        password = request.form.get('login_pswd')
        first_name = request.form.get('user_f_name')
        last_name = request.form.get('user_l_name')
        email = request.form.get('user_email')

        if db.execute('SELECT * FROM reg_user '
                          'WHERE login_name = :login_name',{'login_name': login_name}).rowcount >= 1:
            return render_template('recurr_user_error.html', message='User or e-mail already exists.')


        # If the user is not registered
        db.execute('INSERT INTO reg_user (login_name,login_pswd,user_f_name,user_l_name,user_email'
                       ') VALUES (:login_name, :login_pswd, :user_f_name, :user_l_name, :'
                       'user_email)',{'login_name': login_name, 'login_pswd': password,
                           'user_f_name': first_name, 'user_l_name':last_name, 'user_email': email})
        # Registartion complete
        db.commit()
        return render_template('success.html', message='Registration complete')

    else:
        login_name = request.form.get('login_n')

        if db.execute('SELECT * FROM reg_user '
                           'WHERE login_name = :login_name',{'login_name': login_name}).rowcount == 0:
            return render_template('invld_user_error.html', message='invalid user or password.')
        else:
           user = reg_user.query.get(login_name)
           if user is None:
              return render_template('error.html', message='No such user.')
           else:
              u_sess = user_session(sgk_user_id=user.sgk_user_id, session_start_time=datetime.now().time()\
                           ,session_active_flag='Y')
              db.session.add(u_sess)
              db.session.commit()
              return render_template('explore.html')

@app.route('/explore', methods=['POST'])
def explore():
    zip_code = request.form.get('zip')

    loc_det = location.query.get(zip_code)
    if loc_det is None:
        return render_template('error.html', message='My Bad! I do not show small closeknit communities.')
    else:
        return render_template('locinfo.html')

@app.route('/locinfo/<string:zip_code>')
def locweath():
    '''Get weather info from DarkSky'''

    zip_code = request.form.get('zip')

    loc_det = location.query.get(zip_code)
    if loc_det is None:
        return render_template('error.html', message='My Bad! I do not show small closeknit communities.')
    else:
        weather = requests.get("https://api.darksky.net/forecast/25bf028ed7c3417aeed15461721f7d3a/:lat/:long"\
                ,{"lat": loc_det.latitude,"long": loc_det.longitude}).json()
        print(json.dumps(weather["Present Weather Update"], indent = 2))

