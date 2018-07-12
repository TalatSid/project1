# Project 1

Web Programming with Python and JavaScript

Approach: 
I wanted to write the python functionality first, make sure the basic htmls are rendered without errors and then move on to layout and styling
1) Login - I used the post method for this, but when I uised more than one column in the SQL query, it was failing. I meant to come back to this point and point this code to models.py. I could not accomplish that however. The code is the basic SQl extraction python and rendering in html
2) Register - The idea was to direct to invld_user_error.html and provide functionality for "forgot user id?", "forgot password ?" and "Register". I did not get that far
So far, the code worked as I exected.
3) Logout - Yet to add
4) Import - imported the data using "copy to table from file" 
5) Search, Location, DarkSky - Search for now is by zip code only. I meant to add a list for search by city once the simple zip code search worked. I have the complete code in full_application.py. I kind of drew the initial scope and wrote the python and html accordingly. However, when I started adding these functionalities to application.py one by one I was getting "KeyError: 'SQLALCHEMY_TRACK_MODIFICATIONS'" error. I know it has to do with how I am routing. With all the code written at once I guess I messed up the links. I will look at this more closely and fix it. This is as far as I could get. I will continue working on it however, for my learning.

1)From the comments you had sent for the last project, I paid attention to indentation. Python forced me (it was painful) and html as well I tried to keep them inline.
2)I restricted the length of lines 
