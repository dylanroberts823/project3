# Project 3

Web Programming with Python and JavaScript

Orders folder contains all to do with ordering, adding items to cart, navigating the ordering process. In that folder, you will find:
- models.py, which includes the models for items, categories, item_toppings, cat_toppings, item_prices, tickets, and orders
- urls.py, which has all the urls for navigating the ordering process
-views.py, which containss the code for managing what information what goes into the page
-templates foler, inside of which:
-- base.html, which provides the headers for all the pages
--menu.html, the main menu page
--select_size.html, the first page users see after selecting an item, to select size and number of toppings
--select_toppings.html: the page where users select toppings
Users folder contains all to do with users, logging in, logging out
-admin.py contains all the uploads necessary for the admin site to work
-forms.py contains the log in form 
-urls.py includes the url patterns for logging in
-views.py includes the views patterns for logging in
Inside of templates:
-- base.html is the basic formatting for the login page (e.g. bootstrap)
-- login.html is the login page
-- register.html is the registration page


