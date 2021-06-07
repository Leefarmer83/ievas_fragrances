![Ieva's Fragrances Logo ](/media/ievalogo.png)
# Milestone Project 4 - Ieva's Fragrances

This app was built using [GitHub](https://pages.github.com/) and deployed to [Heroku](https://www.heroku.com/).

[View Site](https://ievas-fragrances.herokuapp.com/)

# Table of Contents

- [UX](#ux)
    - [Project Goals](#project-goals)
    - [User Stories](#user-stories)
    - [Project Wireframe and Design Process](#Project-Wireframe-and-Design-Process)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
    - [Content](#content)
    - [Acknowledgements](#acknowledgements)

# UX

My inspiration for this project came from a combination of my enjoyment of online shopping and technology, and my desire to help my fiance launch her own business. I decided to build a website where she could display, and market her range of hand picked wax melts, and wax melt warmers. These wax melts are smaller than candles, but they also make great gifts, so value packs are also on offer. 

The site features a clean design with an intuitive interface for users using both a desktop, tablet or a mobile device to purchase. A website is an effective channel to reach a wide base of customers. The market, and demographic for wax melts is broad, from business owners to individuals. Many users are still more familiar with purchasing via a website over purchasing through an app on their table or phone. Ensuring that the site is mobile responsive gives users coming from a tablet or mobile device the best user experience. It also saves outlay for a sole trader or small business owner as they don’t need to invest in iOS, Windows or Android native apps, but can still capture sales from users of those devices. 


# Project Goals

This site aims to give users an opportunity to transform their environment through the medium of scent. Users will be able to select from a range of wax melts, curated into different fragrance families, to bring a unique scent and mood to their home. In addition, wax melt holders in a range of styles are also available. Wax melts and wax melt holders can be purchased individually, or as value pack bundles. 


# User Stories

### First time user
1. As a user I want to know what the website is about.
2. As a user, I want to be able to navigate through the website and easily access all of its features.
3. As a user, I want to see images with easy descriptions of each product.
4. As a user, I want to see details about the product/s.
5. As a user, I want to be able to see and navigate to the product/s I want to buy.
6. As a user, I want to be able to sort products by price and category.
7. As a user, I want a text bar to search for products using keywords.
8. As a user, I want to see the quantity of each product/s I have selected.
9. As a user, I want to see reviews on products to give me confidence in the product/s.
10. As a user, I want to be able to contact the company if I have a question.
11. As a user, I want to be able to create an account.
12. As a user, I want to be able to log in and out of an account.
13. As a user, I want to be able to authenticate with my Google account.
14. As a user, I want to be able to purchase something without having to create an account.
15. As a user I want to be able to purchase from all devices.
16. As a user, I want to see a detailed shopping basket.
17. As a user, I want to be able to see a summary of my order before I place it.
18. As a user I want the ability to edit my shopping basket.
19. As a user, I want to securely add my payment information.
20. As a user, I want to be able to log out when I am done.
21. As a user, I want to be kept up to date with the latest offers. 
### Returning user
22. As a user, I want to be able to edit my personal details.
23. As a user, I would like to leave and edit my own review of the product
24. As a user, I want to be able to see my order history.
### Admin of the store
25. As the Admin of the store, I want to be able to edit, add, and delete products in the website’s UI.
26. As the Admin of the store, I want to be able to easily access, maintain and edit all the data associated with the website.
27. As the Admin of the store, I want to be able to send order confirmations.
28. As the Admin of the store, I want to be able to send offers to existing and potential customers. 

# Project Wireframe and Design Process
- [Wireframe design](https://github.com/Leefarmer83/ievas_fragrances/tree/master/assets/readme_images/Wireframes)
    - [Home](https://github.com/Leefarmer83/ievas_fragrances/blob/master/assets/readme_images/Wireframes/Home.png)
    - [Product Page](https://github.com/Leefarmer83/ievas_fragrances/blob/master/assets/readme_images/Wireframes/Products_Page.png)
    - [Product Detail](https://github.com/Leefarmer83/ievas_fragrances/blob/master/assets/readme_images/Wireframes/Product_detail_Page.png)
    - [Checkout Page](https://github.com/Leefarmer83/ievas_fragrances/blob/master/assets/readme_images/Wireframes/Checkout_Page.png)
    - [Shopping Basket](https://github.com/Leefarmer83/ievas_fragrances/blob/master/assets/readme_images/Wireframes/Shoping_Basket_Page.png)
    - [Complete Order](https://github.com/Leefarmer83/ievas_fragrances/blob/master/assets/readme_images/Wireframes/Complete_Order_Page.png)
    - [Order Summary](https://github.com/Leefarmer83/ievas_fragrances/blob/master/assets/readme_images/Wireframes/Order_Summary_Page.png)

# Design

## Database Structure
![Database Structure ](/assets/readme_images/database_structure.png)

- [Database Structure](https://github.com/Leefarmer83/ievas_fragrances/blob/master/assets/readme_images/database_structure.png)

## Features

In this section, you you will see the different parfeaturests of my project.
 
### Existing Features

#### index.html (Home)

The home page features a slider that clearly illustrates the purpose of the site to users. There are six categories of fragrance for users to choose from when selecting wax melts. There is also a ‘specials’ section for users to navigate to wax burners, packages and combination packs, In addition, there is a search bar for keyword search, a subscribe option, and an account section. 

##### User story addressed:
1. As a user I want to know what the website is about.
2. As a user, I want to be able to navigate through the website and easily access all of its features.
3. As a user, I want a text bar to search for products using keywords.

#### sign up
On the register page, the user creates a username and password for successful registration. Once the user has chosen a username and password, they click the Sign Up button to enter the site. If a user chooses an email or a username that already exists in the system, a message loads to let them know the email or username is not available. 
##### User story addressed:
11. As a user, I want to be able to create an account.

#### Sign in
On the login page, users can input their username and password, and select the log in button to login. If a user enters an incorrect username or password, a message loads to let them know they have entered an incorrect credential. When a user logs out, a message loads to let them know they have logged out successfully. Users can also use their Google account credentials to authenticate into the site. 

##### User story addressed:
12. As a user, I want to be able to log in and out of an account.
13. As a user, I want to be able to authenticate with my Google account.

#### logout
When a user chooses to logout, they are taken to the logout page where they are asked to confirm their decision to logout. Once they have logged out, a message pops up to tell them they have successfully logged out of the site. 
##### User story addressed:
20. As a user, I want to be able to log out when I am done.

#### profile
On the My Profile page, users can input their contact telephone number, and their delivery address, as well as edit their details by selecting the Update Information button. Users can also see their order history on this page including the order number, date, items and order total. 
##### User story addressed:
22. As a user, I want to be able to edit my personal details.
25. As a user, I want to be able to see my order history.

#### product
When a user clicks on the product page, they can select a product. When the user selects a product to view, they can see an image and details of that individual product, including the price and quantity they have selected. These can also be removed or edited. 
##### User stories addressed:
3. As a user, I want to see images with easy descriptions of each product.
4. As a user, I want to see details about the product/s.
8. As a user, I want to see the quantity of each product/s I have selected.

#### sort
When a user is on the product page, they can click on the Sort menu. The user can sort by price (low to high, and high to low), rating (low to high, and high to low), name (A-Z and Z-A) or category (A-Z or Z-A). The user can click on sort by price high to low, and the products will display with those with the  highest price at the top of the page descending to those with the lowest price. The user can click on sort by low to high, and the products on the page will display with those with the lowest price at the top of the page descending to those with the highest price. 
##### User story addressed:
6. As a user, I want to be able to sort products by price and category.

#### category
When a user clicks on Category on the home page, the category drop down launches, and the user can select one of the six fragrance categories, or choose to see all the products. When a user selects a specific fragrance family category, they are taken to a page where the products that meet those criteria are displayed. 
##### User story addressed:
5. As a user, I want to be able to see and navigate to the product/s I want to buy.

#### bag
When a user selects a product and clicks the Add to Basket button, the product will be added to their basket. Users can view the product in the basket, and can edit the basket, increasing or decreasing quantity as well as removing items. Users can also opt to ‘Keep Shopping’ and will be returned to the product page. 
##### User story addressed:
8. As a user, I want to see the quantity of each product/s I have selected.
16. As a user, I want to see a detailed shopping basket.
18. As a user I want the ability to edit my shopping basket.

#### checkout
Users can enter their details and state what wax melts they would like (if in package), review their delivery address details, and add their payment details on this page. Users can also see a summary of their order before they complete their order. 
##### User story addressed:
17. As a user, I want to be able to see a summary of my order before I place it.
19. As a user, I want to securely add my payment information.

#### reviews
When a user is on a product page, they can navigate to the reviews for that product by clicking on ‘Customer Reviews’. Here they can see reviews from other customers. If the product listing has no reviews, the user will be invited to write their own review.

##### User story addressed:
9. As a user, I want to see reviews on products to give me confidence in the product/s.
24. As a user, I would like to leave and edit my own review of the product


#### Contact Us
Users can find the contact email address on the footer on each page
##### User story addressed:
10. As a user, I want to be able to contact the company if I have a question.

#### admin
The site owner can log into the admin page as a super user to see all orders, edit orders, create, delete and edit products, see who has subscribed, read reviews and look up users details.

##### User story addressed:
26. As the Admin of the store, I want to be able to edit, add, and delete products in the website’s UI.
27. As the Admin of the store, I want to be able to easily access, maintain and edit all the data associated with the website.


#### Order confirmation
Once the User succesfully completes an order, he/she will get an automated email.

##### User story addressed:
28. As the Admin of the store, I want to be able to send order confirmations.


#### Subscribe
By clicking on the subscribe button the user is asked for their email address. Once the site admin have this they will be able to send product offerings

##### User story addressed:
21. As a user, I want to be kept up to date with the latest offers. 
29. As the Admin of the store, I want to be able to send offers to existing and potential customers. 


### Features Left to Implement
- Allow users to edit their reviews.
- Setup deliver options instead of a discount. 
- Setup the password reset fiunctuonality, today users need to send an email to have it reset.
- Order confirmatiuon email to the store owner.
- Create a functionality for the owner to give discount codes to its users.
- Paginmation - On bothe the products page and review tab.
- Social media login.
- In stock messaging.

## Technologies Used

* [Gitpod](https://www.gitpod.io/) is the IDE used for developing this project.
* [Django](https://www.djangoproject.com/) as python web framework for rapid development and clean design.
* [Stripe](https://stripe.com/gb) as payment platform to validate and accept credit card payments securely.
* [AWS S3 Bucket](https://aws.amazon.com/)  to store static files and images entered into the database.
* [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) to enable creation, configuration and management of AWS S3
* [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) to style django forms.
* [Heroku](https://www.gitpod.io/) Heroku for deployment
* [Gunicorn](https://pypi.org/project/gunicorn/) WSGI HTTP Server for UNIX to aid in deployment of the Django project to heroku.
* [Pillow](https://pillow.readthedocs.io/en/stable/) as python imaging library to aid in processing image files to store in database.
* [Psycopg2](https://pypi.org/project/psycopg2/) as PostgreSQL database adapter for Python.
* [PIP](https://pip.pypa.io/en/stable/installing/) for installation of tools needed in this project.
* [Github](https://github.com/) to store and share all project code remotely.
* [Canva](https://www.canva.com/) to resize images. 
* [Balsamiq/](https://balsamiq.com/)to create the wireframes for this project.

### Databases
[PostgreSQL](https://www.postgresql.org/) for production database, provided by heroku.
[SQlite3](https://www.sqlite.org/index.html) for development database, provided by django.



## Testing

All testing can be found here [View TESTING.md](TESTING.md)

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:
- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.


## Credits

### Content
- The text for section Y was copied from the [Wikipedia article Z](https://en.wikipedia.org/wiki/Z)

### Media
- The photos used in this site were obtained from ...

### Acknowledgements

- I received inspiration for this project from X