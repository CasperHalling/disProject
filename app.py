from flask import Flask, render_template, redirect, url_for, session, abort, request, flash
import requests
from bs4 import BeautifulSoup
import psycopg2
from psycopg2 import sql
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import pandas as pd

app = Flask(__name__ , static_url_path='/static')
app.secret_key = "1234" 

# set your own database name, username and password
db = "dbname='CoursesTest' user='postgres' host='localhost' password='1234'" #potentially wrong password
conn = psycopg2.connect(db)
cursor = conn.cursor()

@app.route('/')

def display_courses():
    course_filter = request.args.get('course_filter', '')
    schedule_filter = request.args.get('schedule_filter', '')
    termin_filter = request.args.get('termin_filter', '')
    average_filter = request.args.get('average_filter', '')
    exam_filter = request.args.get('exam_filter', '')
    ects_filter = request.args.get('ects_filter', '')

    try:

        # Execute SELECT query to fetch course data
        query = "SELECT courseName, schedule, termin, average, exam, ects FROM Course WHERE LOWER(courseName) LIKE %s AND LOWER(schedule) LIKE %s AND termin::text LIKE %s AND average::text LIKE %s AND LOWER(exam) LIKE %s AND ects::text LIKE %s"

        cursor.execute(query, (
            f"%{course_filter.lower()}%",
            f"%{schedule_filter.lower()}%",
            f"%{termin_filter.lower()}%",
            f"%{average_filter.lower()}%",
            f"%{exam_filter.lower()}%",
            f"%{ects_filter.lower()}%"
        ))


        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Process the fetched data and apply filters
        filtered_courses = []
        for row in rows:
            course = list(row)
            if (
                course_filter.lower() in course[0].lower() and
                schedule_filter.lower() in course[1].lower() and
                str(termin_filter) in str(course[2]) and
                str(average_filter) in str(course[3]) and
                exam_filter.lower() in course[4].lower() and
                str(ects_filter) in str(course[5])
            ):
                filtered_courses.append(course)


        return render_template('index.html', courses=filtered_courses)

    except (psycopg2.Error, Exception) as error:
        # Rollback the transaction
        conn.rollback()

        # Handle the error, log or display an appropriate message
        print("Error fetching courses:", error)

        # Return an empty list or an error message to the template
        return render_template('index.html', courses=[])



def get_courses_from_database():
    cursor.execute("SELECT * FROM Course;")
    courses = cursor.fetchall()
    return courses


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get the form data
        username = request.form['username']
        password = request.form['password']

        try:
            # Start a new transaction
            conn = psycopg2.connect(db)
            cursor = conn.cursor()

            # Query the database to check if the user exists
            # Query the database to check if the user exists
            query = sql.SQL('SELECT * FROM "User" WHERE username = {};').format(sql.Literal(username))

            cursor.execute(query)
            user = cursor.fetchone()

            if user:
                # User found, verify the password
                hashed_password = user[2]  # Assuming password is stored in the third column
                bcrypt = Bcrypt(app)

                if bcrypt.check_password_hash(hashed_password, password):
                    # Password is correct, set the user session and redirect to the desired page
                    session['username'] = username
                    return redirect(url_for('display_courses'))
                else:
                    # Password is incorrect, show an error message
                    flash('Invalid username or password.')
            else:
                # User not found, show an error message
                flash('Invalid username or password.')

            # Commit the transaction
            conn.commit()

        except psycopg2.Error as e:
            # Roll back the transaction in case of an error
            conn.rollback()
            flash('Error logging in. Please try again.')
            print(e)

        finally:
            # Close the cursor and connection
            cursor.close()
            conn.close()

    return render_template('login.html')


@app.route('/createaccount', methods=['GET', 'POST'])
def create_account():
    if request.method == 'POST':
        # Get the form data
        username = request.form['username']
        password = request.form['password']
        
        # Hash the password using Bcrypt
        bcrypt = Bcrypt(app)
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        
        # Insert the user into the database
        # Insert the user into the database
        query = sql.SQL('INSERT INTO "User" (username, password) VALUES ({}, {});').format(
            sql.Literal(username), sql.Literal(hashed_password)
        )

        
        try:
            cursor.execute(query)
            conn.commit()
            flash('User created successfully. Please log in.')
            return redirect(url_for('login'))
        except psycopg2.Error as e:
            flash('Error creating user. Please try again.')
            print(e)

        # Redirect to a success page or login page
        flash('User created successfully. Please log in.')
        return redirect(url_for('login'))
    else:
        return render_template('createaccount.html')



@app.route("/logout")
def logout():
    session['logged_in'] = False
    return display_courses()

@app.route("/profile")
def profile():
    cur = conn.cursor()
    if not session.get('logged_in'):
        return render_template('login.html')
    
    username = session['username']

    sql1 = f'''select id, type, gender, skin_tone, count, accessories from favorites natural join attributes where username = '{username}' '''
    cur.execute(sql1)
    favs = cur.fetchall()
    length = len(favs)
    return render_template("profile.html", content=favs, length=length, username = username)


def shutdown_server():
    # Close the cursor and connection
    cursor.close()
    conn.close()
    print('Server shutting down...')

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

if __name__ == '__main__':
    try:
        app.run(debug=True)
    finally:
        shutdown_server()
