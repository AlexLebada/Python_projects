These projects are from udemy course: <u>*The complete Python programming course: Beginner to Advanced*</u>, by Joseph Delgadillo & Nick Germaine


* ### basic_calculator/

Builds a simple calculator that does continous basic calculations, like Windows OS calculator. I changed it a bit, from terminal 
interface to a tkinter window object

* ### RPG_battle/  

Is a text based game for RPG type of play. It's a pretty nice game, which I intend in near future to 
make it on a more friendly GUI. 

* ### Web_Scraper/

Uses 2 scripts: main.py to get bing.com results as a HTML content; images.py get results from search engine, as images which are stored in a folder

* ### Blog_platform_app/

 Notes:
 <br/>
  Actually has functionalities more like a networking platform\
Not working all design imported from bootstrap/MBD, as tutorial is using older libraries\
Also HTML/CSS pages is not entirely covered in tutorial lessons and I had to make a visually valid version

 This project involves:
 <br/>
 
  1.API work using web.py, as a MVC architecture:

  Routes for user registration: '/register', '/postregistration'\
  For Login/Logout sessions are the following routes: '/login', '/check-login', '/logout'\
  Track user activity and settings: '/post-activity' - user is posting to his profile, '/settings', '/update-settings', '/profile/(.*)/' - get user info and ordered post by date\, '/upload-image/(.*)' - upload profile images
<br/> 

  2.Storing & verify data in local installed MongoDB using PyMongo:
  
  Users & Posts collection which are defined in RegisterModel, LoginModel, Posts\
<br/>

  3.Responsive pages & dynamically display data :
  
  Used MBD kit with bootstrap 3.3.7\
  Avoid reloading page by using ajax method for triggered events in HTML pages

<br/>

![Screenshot 2024-12-02 203952](https://github.com/user-attachments/assets/687c5f2f-0229-4035-a7c6-fb8088541eec)

<br/>

* ### Blog_2/

Applications using Django framework