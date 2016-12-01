# Data-Representation-Querying-Project
Michael Geraghty and Damian Curran Dec 2016 Project

    Data Representation and Querying Project 2016
 
This repositry contains the Data Representation and querying Project for Lecturer Ian McLoughlin (1/12/16) Gmit 3rd year. Composed by Students Michael Geraghty and Damian Curran.

    Project Overview
    
We have created a Single-Page Web Application (SPA) It's basis is a for a user who wishes to have something generated for them that they cant decide for themselves or need assistance. This application  lets a user ask a Magic 8 Ball a question and get a response, generates their weeks lotto ticket and rolls Dice for them.

We considered adding a log in function to save a users lotto tickets and 8 ball question and responses  but decided against it because it went against the quick use and fast interaction we were looking for.The idea is we want a user to use the application look for an answer a ticket no. or a die result quickly with no load times or (single page web app helps this) be bogged down with a log in. We had also researched an 8ball app which saves user input and displays it with names and we felt that a user does not want their questions saved if it is sensitive material.Aswell we wished to add a third app (at this point we had only two apps in Application) and with submission loooming.


    Team Members
We decided to attempt this project as a team of two.

*Michael Geraghty
*Damian Curran

All members contributed to all aspects in some way.However Michael lead GitHub branches , master merges ,Overview and documentation and Back end development(python) python. Damian lead in front end development(HTML,css and js) .


    Meetings
Team meetings were held daily on TeamSpeak.At these meetings management,task division and github commits were discussed.

    How to run the application
The application is written using Flask library in python 2.7 Both must be installed to run the project.

The project was developed using cloud 9 and has notes on how to run the application through such medium otherwise it can be run locally:

//python run.py

once the application is runnin g it will notify you of the address it is running on and can be accessed by pointing your browser at "Running on http://127.0.0.1:5000/ "


    Cloud 9
needed if you are running on cloud 9
cmds to run : sudo pip install flask
and install requirements.txt: sudo pip install -r requirements.txt
also in run.py you will need to replace app.run() with the commented version.


    Architecture
The web application runs using Python 2.7 using the flask web micro framework and uses libraries such as jquery and Bootstrap.