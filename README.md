![Ieva's Fragrances Logo ](/media/ievalogo.png)
# Milestone Project 4 - Ieva's Fragrances

This app was built using [GitHub](https://pages.github.com/) and deployed to [Heroku](https://www.heroku.com/).

[View Site](https://ievas-fragrances.herokuapp.com/)

# Table of Contents

- [UX](#ux)
    - [Development Planes](#development-planes)
        - [The Strategy Plane](#the-strategy-plane)
        - [The Scope Plane](#the-scope-plane)
        - [Skeleton plane](#skeleton-plane)
        - [Surface Plane](#surface-plane)
    - [User Stories](#user-stories)
    - [Wireframe](#wireframe)
    - [Database Structure](#database-structure)
- [Existing Features](#existing-features)
    - [Features Left to Implement](#features-left-to-implement)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
    - [Content](#content)
    - [Acknowledgements](#acknowledgements)

# UX

My inspiration for this project came from a combination of my enjoyment of online shopping and technology, and my desire to help my fiance launch her own business. I decided to build a website where she could display, and market her range of hand picked wax melts, and wax melt warmers. This site aims to give users an opportunity to transform their environment through the medium of scent by easily identifying products in fragrance families. Wax melts are smaller than candles, but they also make great gifts, so value packs are also on offer, as well as accessories such as wax melt burners. 

# Development Planes

## The Strategy Plane
Agile design was used to lay out a catalogue for wax melts and accessories with a simple and secure ordering, payment and delivery workflow which is attractive to individual users but also satisfies the requirements of bulk purchase users. 
The strategy is to enable users to select from a range of wax melts, curated into different fragrance families, to bring a unique scent and mood to their home. In addition, wax melt holders in a range of styles are also available. Wax melts and wax melt holders can be purchased individually, or as value pack bundles.  Users can filter product options by fragrance family category, by price and by reviewer rating. 
The site features a clean design with an intuitive interface for users using both a desktop, tablet or a mobile device to purchase. A website is an effective channel to reach a wide base of customers. The market, and demographic for wax melts is broad, from business owners to individuals. Many users are still more familiar with purchasing via a website over purchasing through an app on their tablet or phone. Ensuring that the site is mobile responsive gives users coming from a tablet or mobile device the best user experience. It also saves outlay for a sole trader or small business owner as they don’t need to invest in iOS, Windows or Android native apps, but can still capture sales from users of those devices.

## The Scope Plane
The scope of the site is to attract users by offering a quick and simple way to identify products by keyword search, categories of scents, and specials available. In addition to offering a simple, secure and reliable payment process, users can also be notified of new offers through a newsletter. There is no requirement for an account in order to make a purchase. 
Store owner will also have an admin feature for manageing orders, product inventory and subscriptions.

The site is structured to guide the user through product selection to payment as seamlessly as possible. 

## Skeleton plane
The design of the home page directs the user to the product catalogue, specials, and to subscribe.

The menu guides the user intuitively from the home page to the wax melt filter options, categories, specials and subscription feature. 

The information architecture is designed to support the user goals for the site;simplifying the choice of a product, and minimising the number of decisions a user needs to make before successfully checking out. Static files including images are stored in an AWS S3 bucket.

## Surface Plane
The images, fonts, colour palette and appearance were all chosen for an elegant modern feminine feel.
All forms were kept clean and simple with a focus on collecting only the most pertinent information. 
The font was chosen to convey elegance while simultaneously being easy to read. The logo features an incorporated flame that plays on the wax burner and melt product theme. 
Sourced images were mixed with original images of actual wax melt products and wax melt burners available on the site. 


# User Stories

### First time user
- As a user I want to know what the website is about.
-  As a user, I want to be able to navigate through the website and easily access all of its features.
-  As a user, I want to see images with easy descriptions of each product.
-  As a user, I want to see details about the product/s.
-  As a user, I want to be able to see and navigate to the product/s I want to buy.
- As a user, I want to be able to sort products by price and category.
- As a user, I want a text bar to search for products using keywords.
- As a user, I want to see the quantity of each product/s I have selected.
- As a user, I want to see reviews on products to give me confidence in the product/s.
- As a user, I want to be able to contact the company if I have a question.
- As a user, I want to be able to create an account.
- As a user, I want to be able to log in and out of an account.
- As a user, I want to be able to purchase something without having to create an account.
- As a user I want to be able to purchase from all devices.
- As a user, I want to see a detailed shopping basket.
- As a user, I want to be able to see a summary of my order before I place it.
- As a user I want the ability to edit my shopping basket.
- As a user, I want to securely add my payment information.
- As a user, I want to be able to log out when I am done.
- As a user, I want to be kept up to date with the latest offers. 
### Returning user
- As a user, I want to be able to edit my personal details.
- As a user, I would like to leave my own review of the product
- As a user, I would like to rest my password
- As a user, I want to be able to see my order history.
### Admin of the store
- As the Admin of the store, I want to be able to edit, add, and delete products in the website’s UI.
- As the Admin of the store, I want to be able to easily access, maintain and edit all the data associated with the website.
- As the Admin of the store, I want to be able to send order confirmations.
- As the Admin of the store, I want to be able to send offers to existing and potential customers. 

# Wireframe
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
 
## Existing Features

#### index.html (Home)

The home page features a slider that clearly illustrates the purpose of the site to users. There are six categories of fragrance for users to choose from when selecting wax melts. There is also a ‘specials’ section for users to navigate to wax burners, packages and combination packs, In addition, there is a search bar for keyword search, a subscribe option, and an account section. 

##### User story addressed:
- As a user I want to know what the website is about.
- As a user, I want to be able to navigate through the website and easily access all of its features.
- As a user, I want a text bar to search for products using keywords.

#### Sign up
On the register page, the user creates a username and password for successful registration. Once the user has chosen a username and password, they click the Sign Up button to enter the site. If a user chooses an email or a username that already exists in the system, a message loads to let them know the email or username is not available. 
##### User story addressed:
- As a user, I want to be able to create an account.

#### Sign in
On the login page, users can input their username and password, and select the log in button to login. If a user enters an incorrect username or password, a message loads to let them know they have entered an incorrect credential. When a user logs out, a message loads to let them know they have logged out successfully.

##### User story addressed:
- As a user, I want to be able to log in and out of an account.

###ß## Reset
When a user selects ‘forgot password’ on the login page, the password reset page loads. Users enter their email and select the ‘Reset my password’ button. An email is sent to the user with a password reset link. When the user clicks the link, the Change Password page loads, and users can enter and confirm their new password selection. 

##### User story addressed:
- As a user, I want to be able to reset my password.


#### Logout
When a user chooses to logout, they are taken to the logout page where they are asked to confirm their decision to logout. Once they have logged out, a message pops up to tell them they have successfully logged out of the site. 
##### User story addressed:
- As a user, I want to be able to log out when I am done.

#### Profile
On the My Profile page, users can input their contact telephone number, and their delivery address, as well as edit their details by selecting the Update Information button. Users can also see their order history on this page including the order number, date, items and order total. 
##### User story addressed:
- As a user, I want to be able to edit my personal details.
- As a user, I want to be able to see my order history.

#### Product
When a user clicks on the product page, they can select a product. When the user selects a product to view, they can see an image and details of that individual product, including the price and quantity they have selected. These can also be removed or edited. 
##### User stories addressed:
- As a user, I want to see images with easy descriptions of each product.
- As a user, I want to see details about the product/s.
- As a user, I want to see the quantity of each product/s I have selected.

#### Sort
When a user is on the product page, they can click on the Sort menu. The user can sort by price (low to high, and high to low), rating (low to high, and high to low), name (A-Z and Z-A) or category (A-Z or Z-A). The user can click on sort by price high to low, and the products will display with those with the  highest price at the top of the page descending to those with the lowest price. The user can click on sort by low to high, and the products on the page will display with those with the lowest price at the top of the page descending to those with the highest price. 
##### User story addressed:
- As a user, I want to be able to sort products by price and category.

#### Category
When a user clicks on Category on the home page, the category drop down launches, and the user can select one of the six fragrance categories, or choose to see all the products. When a user selects a specific fragrance family category, they are taken to a page where the products that meet those criteria are displayed. 
##### User story addressed:
- As a user, I want to be able to see and navigate to the product/s I want to buy.

#### Bag
When a user selects a product and clicks the Add to Basket button, the product will be added to their basket. Users can view the product in the basket, and can edit the basket, increasing or decreasing quantity as well as removing items. Users can also opt to ‘Keep Shopping’ and will be returned to the product page. 
##### User story addressed:
- As a user, I want to see the quantity of each product/s I have selected.
- As a user, I want to see a detailed shopping basket.
- As a user I want the ability to edit my shopping basket.

#### Checkout
Users can enter their details and state what wax melts they would like (if in package), review their delivery address details, and add their payment details on this page. Users can also see a summary of their order before they complete their order. 
##### User story addressed:
- As a user, I want to be able to purchase something without having to create an account.
- As a user, I want to be able to see a summary of my order before I place it.
- As a user, I want to securely add my payment information.

#### Reviews
When a user is on a product page, they can navigate to the reviews for that product by clicking on ‘Customer Reviews’. Here they can see reviews from other customers. If the product listing has no reviews, the user will be invited to write their own review.

##### User story addressed:
- As a user, I want to see reviews on products to give me confidence in the product/s.
- As a user, I would like to leave and edit my own review of the product


#### Contact Us
When a user navigates to the footer, they can view the contact details for the site, should they have a query. Users can find the contact email address. If the user sends an email to the contact us email address, a message is returned thanking them for their query. 
##### User story addressed:
- As a user, I want to be able to contact the company if I have a question.

#### Admin
The site features a seperate admin area. The UX here is focused on managing store listings, inventory and orders. The store admin can add products, as well as edit categories, descriptions, pricing and images among other features.

##### User story addressed:
- As the Admin of the store, I want to be able to edit, add, and delete products in the website’s UI.
- As the Admin of the store, I want to be able to easily access, maintain and edit all the data associated with the website.
- As the Admin of the store, I want to be able to send order confirmations.
- As the Admin of the store, I want to be able to send offers to existing and potential customers. 

#### Order confirmation
Once the User succesfully completes an order, he/she will get an automated email.

##### User story addressed:
- As the Admin of the store, I want to be able to send order confirmations.


#### Subscribe
When a user clicks on a subscribe menu option, a model launches. User enter their email address into the available field, and are registered to recieve information on the sites latest deals and offers.

##### User story addressed:
- As a user, I want to be kept up to date with the latest offers. 
- As the Admin of the store, I want to be able to send offers to existing and potential customers. 


# Features Left to Implement
- Allow users to edit their reviews.
- Setup deliver options instead of discount. 
- Order confirmatiuon email to the store owner.
- Create a functionality for the owner to give discount codes to users.
- Paginmation - On bothe the products page and review tab.
- Social media login.
- In stock messaging.

# Technologies Used

* [Gitpod](https://www.gitpod.io/) is the IDE used for developing this project.
* [Django](https://www.djangoproject.com/) as python web framework for rapid 
development and clean design.
* [Bootstrap 4](https://getbootstrap.com/) Grid system and classes create the underlining structure.
* [Stripe](https://stripe.com/gb) as payment platform to validate and accept credit card payments securely.
* [AWS S3 Bucket](https://aws.amazon.com/)  to store static files and images entered into the database.
* [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) to enable creation, configuration and management of AWS S3
* [Font Awesome](https://fontawesome.com/) Used for icons
* [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) to style django forms.
* [Heroku](https://www.gitpod.io/) Heroku for deployment
* [JQuery](https://jquery.com/) Used across different pages on the project to create interactive elements.
* [Gunicorn](https://pypi.org/project/gunicorn/) WSGI HTTP Server for UNIX to aid in deployment of the Django project to heroku.
* [Pillow](https://pillow.readthedocs.io/en/stable/) as python imaging library to aid in processing image files to store in database.
* [Psycopg2](https://pypi.org/project/psycopg2/) as PostgreSQL database adapter for Python.
* [PIP](https://pip.pypa.io/en/stable/installing/) for installation of tools needed in this project.
* [Github](https://github.com/) to store and share all project code remotely.
* [Canva](https://www.canva.com/) to resize images. 
* [Balsamiq/](https://balsamiq.com/)to create the wireframes for this project.
* [Google Fonts](https://fonts.google.com/) Imported selected fonts. 



### Languages

-	[HTML5](https://www.w3schools.com/html/default.asp)
-	[CSS3](https://www.w3schools.com/css/default.asp)
-	[JavaScript](https://www.w3schools.com/js/default.asp)
-	[Python](https://www.python.org/)


### Databases
[PostgreSQL](https://www.postgresql.org/) Production database, via heroku.

[SQlite3](https://www.sqlite.org/index.html) Development database, via django.



# Testing

All testing can be found here [View TESTING.md](TESTING.md)

# Deployment

## Run Locally

You will need the below installed:
- Python3 to run application
- PIP to install all app requirements
    - Django
- Git for version control

Navigate to the GitHub [Repository](https://github.com/leefarmer83/ievas_fragrances). The easiest way to copy the repository is to download, navigate to the code tab, this will allow you to download the zip file. Next upload into your new workspace.

## or


Clone the repository:

Information on how to do this can be found  [here.](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)

Install the required dependencies needed to run the app by typing in the command line:

```bash
pip3 install -r requirements.txt
```

Next create an env.py file, and add the env.py file to your .gitignore file in your projects rot directory. variables to included:

```bash
os.environ["STRIPE_PUBLIC_KEY"] 
os.environ["STRIPE_SECRET_KEY"]  
os.environ["STRIPE_WH_SECRET"]
os.environ["SECRET_KEY"] 
os.environ["DEVELOPMENT"] 
```

You will need to sign up to stripe, details below.

Install the required dependencies needed to run the app by typing in the command line:

```bash
pip3 install -r requirements.txt
```

Note - Whenever a model is edited you a migration is needed. Fist test with the below command, then take out --dry-run and --plan to migrate

#### Test migrations

```bash
python3 manage.py makemigrations --dry-run

python3 manage.py migrate --plan
```
####  Migrate


```bash
python3 manage.py makemigrations 

python3 manage.py migrate 
```


---


### Deployment to Heroku

1. Navigate to Heroku.com and login or register for a profile.
1. Select to create new app and put in a unique name.
1. Select region closest to you.

**Set up connection to Github Repository:**

1. Once the app is created, navigate to the deploy tab.
1. Select GitHub - Connect to GitHub to connect heroku to your github where the repository to deploy is stored.
1. Find the github repository to connect to.
1. Enter the repository name for the project you wish to deplot and click search.
1. Once the repo has been found, click the connect button.


**Add PostgreSQL Database:**

1. Along the navigation bar at the top, go to the resources tab.
1. Under Add-ons search for Heroku Postgres and then select it.
1. Select the free hobby plan unless you wish to move to a paid option.

**Set environment variables:**

1. The project uses a number of environment variables to keep sensitive information hidden.

- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- DATABASE_URL
- EMAIL_HOST_PASS
- EMAIL_HOST_USER
- SECRET_KEY
- STRIPE_PUBLIC_KEY
- STRIPE_SECRET_KEY
- STRIPE_WH_SECRET
- USE_AWS

Values are not shown.

**Enable automatic deployment:**
1. If you would like there is an option to enable automatic deploys when you push to github.
1. In the Automatic deploys section, choose the branch you want to deploy from then click Enable Automation Deploys.

### Stripe and AWS Setup

You will also need to set yourself up with a stripe account to handle payments and an AWS to host the static files.

[AWS Documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/setting-up-s3.html)

[Stripe Documentation](https://stripe.com/docs)

## Credits

A huge amount of credit needs to go to the Code Institute, I used their best practices when structuring my code. I have copied a lot of thier code (Bag/checkout/products/profiles/templates) and ajusted to suit the needs of my project, Their code can be found [here](https://github.com/ckz8780/boutique_ado_v1/).

I also used https://testdriven.io/blog/django-custom-user-model/ to help me with the models in newsletter and reviews.

[Bootstrap](https://getbootstrap.com/) framework was used heavily to structure my websit; navbar, footer, classes, toasts.

### Content
- The concept, design and text for this project was created by Lee Farmer and inspired by the mini project boutique ado.

### Media
- The photos used in this site were obtained from Ievas Fragrances and i had permission to use.

### Acknowledgements

- I received inspiration for this project from Boutoque ado, I would also like to that the instructors and the slack community for heling me. Special praise to my mentor Gerard McBride.


