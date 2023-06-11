This program is created with inspiration from the example project "nft-crpyto-punk". Certain design
elements and functionality is shared, but the goals of the projects are completely different.


To run the program:

1. navigate the terminal to the correct folder and use command "pip install -r requirements.txt"

2. Initialize the database, by running the SQL files (Creating the necessary tables)

3. Go to app.py and find the variable called "db". Change the parameters to match your own SQL database.

4. Run the app with "python3 app.py". You can now go to the localhost port specified in your terminal.


---------------------------------------------------------------------------------------------------------

Functionality and how to use the application:

When going to the webapp, you will be presented with a table of Bachelor courses for the 5th semester
that can be taken by students at DIKU.

You can use the filters to specify which courses to display. The filters can be combined. For an example,
if you type 'B' in schedule and '1' in Termin, you will get all courses available in schedule B for the
first block of the semester. 

The possible filters are on, Coursename, Schedule, Termin (block), Average grade, Exam (is it oral,
written assignment ect.) and ECTS points. 

The idea is to give a better overview of the possible courses to take, since some of the information
currently is split between two different platforms at KU. This gives a better overview of the "stats"
a given platform has.

By pressing "profile", you will be redirected to a login page. Here you can also create a user.
You can also log out by pressing "logout". In the current implementation, being logged in our out
does nothing for the functionality of the program, but the created logins will be stored in the database
with hased passwords.
