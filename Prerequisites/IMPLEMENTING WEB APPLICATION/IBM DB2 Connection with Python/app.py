from flask import Flask, url_for, render_template, request, redirect, session, flash
import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=815fa4db-dc03-4c70-869a-a9cc13f33084.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=30367;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=pfd63832;PWD=eTBT9FvOEaVoSk1V", '', '')

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        email = request.form['email']
        passw = request.form['password']
        sql = "SELECT * FROM users WHERE email=? and password=?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt, 1, email)
        ibm_db.bind_param(stmt, 2, passw)
        ibm_db.execute(stmt)
        data = ibm_db.fetch_assoc(stmt)
        if data:
            session['logged_in'] = True
            session['name'] = data["NAME"]
            session['id']=data["ID"]
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid Credentials!')
            return render_template('login.html',error=True)


@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    if request.method == "GET":
        return render_template('signup.html')
    else:
        name=request.form['name']
        email = request.form['email']
        passw = request.form['password']
        sql = "SELECT * FROM users WHERE email=?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt, 1, email)
        ibm_db.execute(stmt)
        data = ibm_db.fetch_assoc(stmt)
        if not data:
            if len(passw)>7:
                if (request.form['password'] == request.form['confirm-password']):
                    insert_sql = "INSERT INTO users(EMAIL,NAME,PASSWORD) VALUES (?,?,?)"
                    prep_stmt = ibm_db.prepare(conn, insert_sql)
                    ibm_db.bind_param(prep_stmt, 1,email)
                    ibm_db.bind_param(prep_stmt, 2,name)
                    ibm_db.bind_param(prep_stmt, 3,passw)
                    ibm_db.execute(prep_stmt)
                    flash('Registered Successfully!')
                    return  redirect(url_for('login'))
                else:
                    flash("Password must be same")
                    return redirect(url_for('signup'))
            else:
                flash("Length should be greater than 8")
                return redirect(url_for('signup'))
        else:
            flash("Email is already exist")
            return redirect(url_for('signup'))





@
