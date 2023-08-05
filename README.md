# LaunderKing Web Application 
### August 2nd, 2023 | <small> Ethan Kigotho</small>
#### Video Demo Link:  <URL HERE>
### Project Background:

Hello, CS50! It's been quite a long journey and for my final project I have created a web application of a pickup/delivery laundromat's online business.
I initially put off doing this project because of other school work as well as a lack of ideas, but only recently I have found the motivation to complete it once and for all. 

I struggled in the beginning with coming up with an idea for a final project, but when my dad started to consisder starting a laundromat company, I figured I could try to make a "mock" ecommerce web application. I liked this idea and it has taken me all the way to today.
##
### Tools Used

In this project I utilized Python (Flask), Javascript, CSS, HTML, and SQLAlchemy. 
* Python was used within the Flask framework to create routes, communicate with the database, and manipulate data.
* Javascript was used for form validation (using regular expressions) as well as certain *onclick()* functions.
* HTML and CSS were used for visuals and design.
* SQLAlchemy was the datbase toolkit was used to store account information as well as any services a user may purchase.

>Note: I did not use as much bootstrap as I would have wanted to. I initially wanted to try making pages relatively from scratch (which worked), but when I attempted to use bootstrap later it would mess with all I have done already. Thus, I decided against using bootstrap and would save it for another future project
##
### Web Application Features
#### A Quick Summary of Launderking's Features:
* Index, About, and Account related pages.
* A navbar that reacts to a user being signed in or not.
* Purchase/Login buttons that react to a user being signed in or not.
* Failsafes in place if a user tries to access a "signed-in-only" page.
* Hashed Passwords via sha256_crypt
* Eye-Catching picture designs (courtesy of Pexels) that explain the services.
* Cool, relaxed color scheme.
* Easy to read purchase history table.

## 
### File-By-File Explanation

### layout.html
Layout.html is my file that I "extend" from in every other html file. It includes the consistent header and footer that is seen on every page. It is the blueprint for my website and allowed for faster page creation on my end. This file also makes use of jinja syntax to update the navbar if a user is signed in.


### index.html
Index.html is the front page of my site. It provides the user a brand name and sort of catchphrase: "The King of Cleaning." Once that first section was complete, I was sort of stumped as to what to add to the front page. 

I decided to do some research on  local laundromat companies near my location and they often had three symbols detailing their cleaning process. 
That Idea really stuck with me, so I found free symbols to import online and wrote my own little descriptions for what the deliver/pickup service may provide. I really liked this design because of how effective and simple they are in providing context to the user.

### about.html
about.html is a relatively self explanatory page. It is simply a description about the hypothetical LaunderKing's business, the type of description you would find on any website in this day and age.

While we're on this page though, I want to touch on my frequent usage of picture backgrounds. I'm going to admit that I am not the greatest at color backgrounds so pictures always felt like a safe option. My first plan was going to try to create a parallax effect, but that didn't work out as I expected. The styling just turned out to be a nice way to have an image background for the page so I stuck with it. I think I like how it turned out regardless!

### login.html and register.html
Register and Login are very similar pages as they are based around the same submission form design. Register asks for a username (used for personalization), an email (for the login), a password, and a confirm password. Assuming all information is correctly provided (proper formatting, etc.) an account is entered into the User database. If information is incorrectly provided, the user is told.

Login asks for the email and password of the user. If there is an account that has this email, it compares the inputted password to the hashed password in the database (once again, via sha256_crypt). Once the user is logged in, the session takes note of their username and user_id for future uses.

### order.html
order.html displays the website's available services, their prices, and a brief description. It includes a "buy now" button which will immediately add the purchase to the user's purchase history since there is no actual ecommerce involved. If the user is not signed in, the "buy now" will be replaced with a "sign in." If this business actually existed I would have most likely added a cart system as well as a proper checkout.

### history.html
history.html and order.html go hand in hand. All previous purchases from a user will displayed on their history page. The information includes the order ID, service name, price, and description. This was done using jinja for loops which I learned in the cs50 finance assignment. These orders are all pulled from the database's "orders" table which is linked to the user table with the foreign key "user_id". I chose to do this as it allowed me to look up all of a user's orders with simply their id on hand.

### Static Folder / Other
The Static folder just contains images, css, and the script files. Images I tried to keep within the blue-ish color scheme. The stylesheet is just a massive file of all the styling used in the website. The javascript only has a few functions such as button "onclicks" as well as various alerts to prevent invalid logins/registrations.


##

### Closing Thoughts and Reflections
I thoroughly enjoyed doing this, so much so that I almost regret not doing it sooner 😅. I've been putting off cs50 for about 2 years now (a long time, I know) and I'm glad that I've finally finished it all up. The most difficult thing in this project for me was definitely design ideas. I'm not a very creative/artsy person so brainstorming color schemes or image ideas takes a lot of time from me.

I definitely regret not utilising bootstrap from the very beginning, but hey, it is what it is. This is the first project I've "finished" so I am pretty proud of just making something, even if it is relatively simple to seasoned developers. 

> Thanks For Reading!

<small>Written By: Ethan Kigotho </small>