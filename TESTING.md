# Testing

[return to README.md](https://github.com/Leefarmer83/ievas_fragrances)

# Validation
### Websites used on code:
- [W3C Markup Validation Service](https://validator.w3.org/)
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
- [JSHint](https://jshint.com/)
- [PEP8 Validator](http://pep8online.com/)

# User Story Testing

## As a user, I want to know what the website is about

Action taken|expected result|pass/fail
------------ | --------------- | ---------
Clicked on slider|Value proposition messaging displays over images|pass
Clicked on slider|Images with value proposition messaging rotate|pass
Viewed footer|Description of business displays|pass


- Acceptance Criteria - 
The home page will feature information regarding the purpose of the site, with headings and images consistent with this purpose. 

- Pass - 
The home page features a brief sentence in the slider that describes the site. The menu items also provide an overview of additional content on the site. 

## As a user, I want to be able to navigate through the website and easily access all of its features.

Action taken | expected result | pass/fail
------------ | --------------- | ---------
Clicked on Wax Melt menu | Price, category, rating and all products options display| pass
Clicked on Category menu | Fragrance families display| pass
Clicked on Specials menu | Packages, bundles and wax burner options display| pass
Clicked on Subscribe menu | Modal with sign up instructions launches | pass
Clicked on Shop Now button| Product catalogue page launches| pass
Clicked on My Account | Register and Sign In options display | pass
Clicked on company logo | Taken back to home page | pass


- Acceptance Criteria - The home page will feature menu options that direct the user to the products, product categories, offers and their profile information.  
- Pass - The home page features wax melt filter options, a category menu of fragrance families, a specials menu and the ability to sign up for a newsletter as well as a profile section. 

## As a user, I want to see images with easy descriptions of each product.

Action taken | expected result | pass/fail
------------ | --------------- | ---------
Clicked on Wax Melts - All Products | Product catalogue page with images of each product launches | pass
Clicked on Category Menu-All | Product catalogue page with image and description of product launches | pass
Clicked on Specials Menu-All | Product catalogue page with image and description of product launches | pass
Clicked in individual product listings | Product page with image and description of product launches | pass

- Acceptance Criteria - The product pages will feature images and descriptions of each product. 
- Pass - The product pages feature an image of each product, and a brief description of the product’s fragrance. 

## As a user, I want to see details about the products

Action taken | expected result | pass/fail
------------ | --------------- | ---------
Clicked on Wax Melts - All Products | Product catalogue page with image, category, price and rating launches| pass
Clicked on Category Menu-All | Product catalogue page with image, category, price and rating launches| pass
Clicked on Specials Menu-All | Product catalogue page with image, category, price and rating launches| pass
Clicked in individual product listings | Product page with image, weight, price, category, rating and product detail description launches | pass

- Acceptance Criteria - The product pages will feature detailed descriptions of each product. 
- Pass- The product pages feature an image of each product, and detail on the weight, price, category and rating by customers as well as customer reviews if a product has been reviewed. 

## As a user, I want to be able to see and navigate to the products I want to buy

Action Taken | expected result | pass/fail
------------ | --------------- | ---------
Clicked on Wax Melt menu |Price, category, rating, and all products options display | pass
Clicked on Category menu | Fragrance family and all fragrance options display | pass
Clicked on Shop Now button | Product catalogue page launches| pass
Clicked in Search Bar | Key word entered in search bar returns correct product | pass
 
- Acceptance Criteria - The site will feature a product catalogue on the home page menu with filters, and a category menu. 

- Pass - The wax melt menu has filters by price, category, and rating for easy navigation to products, and users can also view all products. The categories menu allows a user to quickly navigate to products in a fragrance family. 

## As a user, I want to sort products by price and category

Action Taken | expected result | pass/fail
------------ | --------------- | ---------
Clicked on Wax Melts-By Price menu | Products display by price low-to-high | pass
Selected Sort-By Price High-to-low | Products display by price high-to-low| pass
Clicked on Wax Melts-By Category menu | Products display in categories alphabetically A-Z| pass
Selected Sort-By Category Z-A| Product display in categories alphabetically in descending order Z-A| pass

- Acceptance Criteria - The site will feature a sort drop down on the product and category pages. 

- Pass - The wax melt, and category menus both have a sort feature. Users can sort by price high-to-low and low-to-high and by category A-Z and Z-A. 

## As a user, I want a text bar to search for products using keywords.

Action Taken | expected result | pass/fail
------------ | --------------- | ---------
Clicked on search bar | Products with keyword in product name returned | pass
Clicked on search bar| Products with keyword in product description returned | pass

- Acceptance Criteria - The site will feature a search bar for product search by name. 

- Pass - Users can enter their search term in the search bar, and products featuring the key word in the product name or product description will be returned. 

## As a user, I want to see the quantity of each product/s I have selected.


Action Taken | expected result | pass/fail
------------ | --------------- | ---------
Clicked on product listing | Product quantity field displays | pass
Clicked on decrease control in quantity field | Default quantity of one remains unchanged | pass
Clicked on increase control in quantity field | Quantity displayed increases | pass
Clicked on decrease control in quantity field | Quantity displayed decreases | pass
Manually entered quantity in quantity field | Quantity chosen displays | pass

- Acceptance Criteria - 
Each product page on the site will feature a quantity display and the ability for a user to edit. 

- Pass - Each product page has a quantity display, and the user can increase or decrease the quantity using the controls on the display. 

## As a user, I want to see reviews on products to give me confidence in the product/s. 

Action Taken | expected result | pass/fail
------------ | --------------- | ---------
Clicked on Reviews tab | Review of product displays | pass
Clicked on Reviews tab | If no review, message inviting users to leave review displays | pass
Clicked on Wax Melts-By Rating menu | Products with ratings high-to-low display | pass
 
- Acceptance Criteria - Each product page on the site will feature a review section. 
- Pass - When on the product listing page, users can select the Reviews tab to see the reviews that other shoppers have left together with a rating out of 5 for the product. 

## As a user, I want to be able to contact the company if I have a question. 

Action Taken | expected result | pass/fail
------------ | --------------- | ---------
Clicked on footer | Company contact information displayed | pass
Contact email address entered into email provider | User receives automated email confirming receipt of their communication | pass
 
- Acceptance Criteria - The site will list contact information to which users can direct any queries. 

- Pass - The site lists an email address as contact information. When a user sends an email, they receive an automated response thanking them for their query. 

## As a user, I want to be able to create an account. 
Action Taken | expected result | pass/fail
------------ | --------------- | ---------
Clicked on My Account section | Register and Sign In options display | pass
Clicked on Register button | Sign Up page launches | pass
Entered data into Sign Up form | System generates email with confirmation link for user to follow | pass
Clicked on link in user email | Returned to Sign Up page to finalise account setup | pass
 
- Acceptance Criteria - The site will feature a My Account section where users can create an account. 

- Pass - The site has a My Account section where users select the Register button to launch the Sign Up page. Users enter an email address, username and password to register. The system generates an email with a confirmation link for the user to follow. When they click the link, they are brought back to the site to finalise account confirmation. 

## As a user, I want to be able to log in and out of an account.

Action Taken | expected result | pass/fail
------------ | --------------- | ---------
Clicked on My Account section | Register and Sign In options display | pass
Clicked on Sign In | Sign in page with fields for user credentials launches | pass
User credentials entered | User signed in and successful sign in message loads | pass
Incorrect user credentials entered | Message loads to notify user of incorrect credentials | pass
Clicked on Sign Out | System message prompting user to confirm decision to sign out loads | pass
Clicked on Sign Out button| User signed out and successful sign out message loads | pass

- Acceptance Criteria - The site will feature a My Account section where users can sign in and out of their accounts. 

- Pass - The site has a My Account section where users select the Sign In option to login. Users enter their username or email address, and their password to login. The site notifies them of their successful login with a pop up message. Users select the Sign Out option under My Account to sign out of their account. 

## As a user, I want to be able to purchase something without having to create an account. 

Action Taken | expected result | pass/fail
------------ | --------------- | ---------
Anonymous user added product to bag | Pop up message confirming addition of product to bag loads | pass
Anonymous user selected go to secure checkout | Order summary page loads | pass
Anonymous user selected Checkout | Checkout page loads | pass
Anonymous user selects Complete Order | Order information displayed and confirmation email sent | pass
 
- Acceptance Criteria - The site will allow users to select products, and checkout without creating an account. 

- Pass - Users can add products to their shopping bag and complete the checkout procedure without creating an account. Users can view their order, and receive a confirmation email with their order details. 

## As a user, I want to be able to purchase from all devices. 

Action Taken | expected result | pass/fail
------------ | --------------- | ---------
Mobile phone user added product to bag | Pop up message confirming addition of product to bag loads| pass
Mobile phone user selected go to secure checkout | Order summary page loads | pass
Mobile phone user selected Checkout | Checkout page loads | pass
Mobile phone user selects Complete Order | Order information displayed and confirmation email sent | pass
Tablet  user added product to bag | Pop up message confirming addition of product to bag loads | pass
Tablet user selected go to secure checkout | Order summary page loads | pass
Tablet user selected Checkout | Checkout page loads | pass
Tablet user selects Complete Order | Order information displayed and confirmation email sent | pass
Laptop user added product to bag | Pop up message confirming addition of product to bag loads | pass
Laptop user selected go to secure checkout | Order summary page loads | pass
Laptop user selected Checkout | Checkout page loads | pass
Laptop user selects Complete Order | Order information displayed and confirmation email sent | pass

- Acceptance Criteria - The site will be mobile responsive and allow users to make purchases. 

- Pass - Users can add products to their shopping bag and complete the checkout procedure from a mobile phone device, and a tablet device. 

## As a user, I want to see a detailed shopping basket. 

Action Taken | expected result | pass/fail
------------ | --------------- | ---------
Added product to bag | Successful addition of product to bag message loads | pass
Clicked on bag | Shopping bag page with details of products selected including image, product name, price, quantity selected and delivery charges loads | pass

- Acceptance Criteria - The site will have a Shopping Bag feature where users can see the products added to their bag. 

- Pass - Users can add products to their shopping bag. When the user selects their Shopping Bag, they can see an image, product name, price, quantity selected and delivery charges added. 

## As a user, I want to be able to see a summary of my order before I place it. 

Action Taken | expected result | pass/fail
------------ | --------------- | ---------
Clicked on Secure Checkout | Checkout page with Order Summary detail loads | pass
 
- Acceptance Criteria - The site will have an order summary facility on the checkout page for users to review before purchase. 
- Pass - When users select secure checkout, the summary of their order is displayed on the page including the items, quantity, subtotal, delivery charges and total amount of order. 

## As a user, I want to be able to edit my shopping bag. 

Action Taken | expected result | pass/fail
------------ | --------------- | ---------
Clicked on Shopping Bag | Shopping bag page loads | pass
Clicked on quantity increase controls | Quantity in shopping bag increases after update | pass
Clicked on quantity decrease control | Quantity in shopping bag decreases after update | pass
Clicked on Remove button | Product removed from basket and product removal message loads | pass
 
- Acceptance Criteria - The site will offer users the ability to edit their shopping basket. 

- Pass - When users select their basket, they have the ability to change quantities by increasing or decreasing the quantity, and to delete items from the basket. 

## As a user, I want to be able to securely add my payment information. 

Action Taken | expected result | pass/fail
------------ | --------------- | ---------
Clicked on Secure Checkout | Checkout page loads | pass
Entered valid payment information |Successful order process message loads | pass
Entered incomplete payment information | Message loads prompting user to correct information| pass
Entered invalid payment information | Message loads prompting user to correct information | pass

- Acceptance Criteria - The site will allow users to enter their payment information on a secure page. 

- Pass - On the checkout page, users can enter their credit card information. If a user enters an incomplete or invalid card number, they are prompted by the system to correct their error. 

## As a user, I want to be able to log out when I am done. 

Action Taken | expected result | pass/fail
------------ | --------------- | ---------
Clicked on My Account when logged in | My Profile and Sign Out options display | pass
Clicked on Sign Out menu option | System message requesting sign out confirmation loads | pass
Clicked on Sign Out button | System message confirming successful Sign Out loads | pass
 
- Acceptance Criteria - The site will feature a Sign Out feature for users to securely exit the site. 

- Pass - When a user selects the Sign Out option from the My Account menu, they receive a message to confirm they wish to sign out. Once they confirm, they are signed out of the site and a message loads to let them know their sign out was successful.

## As a user, I want to be kept up to date with the latest offers. 

Action Taken | expected result | pass/fail
------------ | --------------- | ---------
Clicked on Subscribe menu option | Modal with field for email entry loads | pass
Clicked on Subscribe button without entering email| Pop up message prompting data input to field loads | pass
Clicked on Subscribe button with email field populated | Confirmation of successful subscription message loads | pass

- Acceptance Criteria - The site will feature a Subscription service where users can sign up for information and offers. 

- Pass - When a user clicks on the Subscribe option, a modal launches where they can enter their email address. Once they enter their email, a confirmation message launches to let the user know that they have been added to the mailing list for offers.

## As a user, I want to be able to edit my personal details. 

Action Taken | expected result | pass/fail
------------ | --------------- | ---------
Clicked on My Account without signing in | My profile menu option does not display | pass
Signed In | My profile menu option displays under My Account | pass
Clicked on My Profile menu option | My Profile page loads | pass
Entered data into form fields and clicked update | System message confirming successful update loads | pass
 
- Acceptance Criteria - The site will feature a profile section where users can capture their details. 

- Pass - Once a user signs in, the My Profile option is available under the My Account section. Users can enter their contact telephone number and address. 

## As a user, I want to be able to reset my password. 

Action Taken | expected result | pass/fail
------------ | --------------- | ---------
Clicked on Sign In | Sign In page loads | pass
Clicked on Forgot Password button | Password reset page loads| pass
Entered email in form field | If email associated with an account in the system, users receive email with password reset link | pass

- Acceptance Criteria - The site will allow users to request a password reset if they forget their password. 

- Pass - On the Sign In page, users can click on the Forgot Password button if they need to request a password reset. Once the user has entered their email, and if the email is associated with an account in the system, the users will receive an email with a password reset link. 

## As a user, I want to be able to leave my own review of the product 

Action Taken | expected result | pass/fail
------------ | --------------- | ---------
Anonymous user clicked on Write Review tab | Message requesting user to sign in loads | pass
Registered user clicked on Write Review tab | Add review modal loads | pass
Entered all required information into review modal | System generated confirmation of review added | pass
Clicked on Reviews tab | Review text present | pass
Entered incomplete information into review modal | System generated message prompts input of required information | pass

- Acceptance Criteria - The site will offer the ability for users to give products a rating out of 5, and write reviews of products to assist other users in making selections, or deciding to purchase from the site. 

- Pass - When clicking review the user has a pop up screen that allows them to rate and review the product.

## As a user, I want to be able to see my order history. 

Action Taken | expected result | pass/fail
------------ | --------------- | ---------
Clicked on My Profile user with purchase history | Order history displays | pass
Clicked on Order Number link in Order History | Order Thank You page loads | pass
Clicked on My Profile user with no purchase history | Order history blank | pass
 
- Acceptance Criteria - The site will feature an Order History section under the user’s account profile. 

- Pass/ - When a user has made a purchase, they can view their Order History under the My Profile section of the site. The Order History displays their order number, date of orders, items in order and the order total. If the user clicks on the order number in the history, they are taken to a copy of the order confirmation email that shows the delivery address and contact information. 

## As the Admin of the store,  I want to be able to edit, add, and delete products in the website’s UI. 

Action Taken | expected result | pass/fail
------------ | --------------- | ---------
Logged in as Store Admin | Product management menu option displays under My Account | pass
Clicked on Product Management | Add a product page loads | pass
Clicked Add Product mandatory fields not complete | Message loads to prompt admin to fill in mandatory fields | pass
Clicked Add Product mandatory fields complete | Message loads to confirm successful addition of product | pass
Clicked on Delete Product | Message loads to confirm successful deletion of product | pass
Clicked on Edit Product | Edit a product page loads | pass
Clicked on Update Product | Message loads to confirm successful update of product | pass

- Acceptance Criteria - The site will feature a Product Management facility for store owners to manage the product catalogue. 

- Pass - When a store admin logs in, they can navigate to the Product Management option under My Account. Store admins can select a category, enter a SKU, the name, description and price of a product, as well as images to add a new product. Existing products listings display edit and delete buttons in this mode, and store admins can edit and update existing listings.


