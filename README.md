# Log_Analysis_Project

OVERVIEW OF THE PROJECT

In this 3rd project for the udacity fullstack nanodegree program, we had to create a reporting tools for the newspaper that'll tell us which articles were the most read and liked. We had to create a complex SQL code to collect data from a large database with over a million row.

HOW TO RUN IT

To run it you need the following:

* [PYTHON](https://www.python.org/downloads/)
* [VAGRANT](https://www.vagrantup.com/)
* [VIRTUALBOX](https://www.virtualbox.org/)

SETTING IT UP

You gone need to download, and install all three of these programs in order to run it. With that you also need to download or clone this repository [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) your vagrant directory is located inside of it. Once you get all that done open up your command terminal for mac it's terminal for windows it is cmd. To get vagrant terminal setup type in the command vagrant up give it few minutes to load and install necessary files, then the following command vagrant ssh will get you logged into the vagrant terminal.

Your vagrant terminal might ask you for authentication, use vagrant for loging and vagrant for the password that should work. Inside your vagrant terminal type in the following command cd /vagrant to go into the directory containing the database you need, and type in this command psql -d news -f newsdata.sql to load the database. To go into the database and look around type in psql -d news, you should see three table:

* Articles
* Authors
* Log

Create a python file with SQL code to answer the following questions: 
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

EXECUTING THE PROGRAM
Now to execute the program from the command line simply type in python3 logs_analysis.py
