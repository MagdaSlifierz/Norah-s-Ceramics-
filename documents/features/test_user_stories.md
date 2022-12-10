# TESTING USER STORIES

[Return to main README file](/README.md#testing-user-stories)

- ## **As a new user:**

  - ### **User stories**

  > As a new user, I want to easily navigate across the site so that I can find the information I need.

  - The website features a navigation menu on top of the page to allow users to navigate throughout the website easily. The navigation is also collapsible on mobile devices for better visibility.
  - Once a user is logged in, the navigation menu will update to allow users to access all features related to them, such as their profile page or adding items if the user is the shop owner.
  - In the footer, the user can find a 'quick links' list, which leads to sections of the website, which also helps in the smooth navigation of the website.
  - When the user starts scrolling down, on the right side appears the 'back to top button', which, when pressed, leads to the home page
  - The layout and menu of the website will resize according to the device used for better visibility and user experience. The navigation is collapsible on mobile devices for better visibility.

  ![navbar mobile](/documents/navbar-mobile.png)

  ![navbar desktop](/documents/navbar-desktop.png)

  ![back to top button](/documents/back-to-top-button.png)


  > As a new user, I want to locate social media links to find opinions about the company and check how trusted and known they are.

  - In the footer, the user can find social media icons that link to the company's social media websites

  ![footer social icons](/documents/footer.png)


  > As a new user, I want to easily understand the main purpose of the website.

  - The hero section contains images that are related to the activities of the company.
  - The hero section contains a text that indicates what the company does.
  - Featured at the top of the page is the company logo

  ![home](/documents/home.png)


  > As a new user I want to have option to see passwords so I will not make a mistake typing it.

  - The register and login page contains option which after clicking show password.

  ![register](/documents/register.png)

  ![log in](/documents/log-in.png)


  > As a new user , I want to view all the products available so that I can quickly have an overview of what is on offer.

  - The hero section contains link 'shop all now' which leads to all available products.


  > As a new user, I want to view available products by specific category so that I can quickly find products I’m interested in.

  - The navbar contains links to each category.


  > As a new user , I want to find a section describing the company to find out when it was founded and the rest of the pertinent information about this company.

  - The 'about' section contains information about company.

  ![about](/documents/about.png)

- ## **As a frequent user:**

  - ### **User stories**

  > As a frequent user, I want to view the product details so that I can make an informed decision.

  - Product details page contains:
    - product image
    - product name
    - product price
    - product overall rating displays as stars
    - link - qty of reviews
    - link - write review
    - product details like: height, width, length, volume
    - product description
    - 'add to basket' button

  ![product details](/documents/product-details.png)


  > As a frequent user, I want to know what products are new arrivals, so I can be up to date with the new products.

  - This section is located in the home section.
  - Displays the ten most recently added products.

  ![new arrivals](/documents/new-arrivals.png)


  > As a frequent user, I want to sort the list of products so that I can find a piece within my price range.

  - 'sort by' option is located inside the 'filters' box.
  - The user can sort products by:
    - name A-Z
    - name Z-A
    - price low to high
    - price high to low

  ![filters](/documents/filters.png)


  > As a frequent user, I want to review items in my shopping bag so that I can adjust quantities ordered.

  - The shopping basket features a summary list all the items added by the user, including quantity and prices.
  - The user will be able to add / subtract / delete all products.
  - When adjusting / removing an item in/from the shopping basket, the totals and subtotals will adjust accordingly and a toast message will inform the user about their action and the content of the shopping basket.
  - The shopping basket a also features a button "Proceed" which leads to order summary part.

  ![basket](/documents/basket.png)

  - When the shopping basket is empty, an information appears on the screen.

  ![basket](/documents/empty-basket.png)


  > As a frequent user, I want to see messages after logging in, logging out, or register so I will know what is happening.

  - While using the website, each activity is described by toast messages appearing on the screen.
  - After registering, the user receives a message to their email with a verification link that allows verifying whether the email is correct.


  > As a frequent user, I want to be able to create my profile so I can update my personal information.

  - User can see their profile only after log in.
  - Profile page features the user's personal information, orders history and reviews history.
  - The user can update personal information and address information. The page will be updated upon submitting the new information.

  ![profile icon](/documents/profile-icon.png)


  > As a frequent user, I want to be able to delete my profile so my personal information is removed from the website.

  - User can find 'delete account' button in the 'personal information' section after log in into their account.
  - Before the users delete the account, they are asked if they are sure they want to delete it.

  ![delete account](/documents/delete-account.png)


  > As a frequent user, I want to verify the forgotten password so I can confirm my request on the recovery link.

  - The user can recover the forgotten password in the 'login' section.
  - The user will be asked for their email, and a reset link with a token will be sent to the email address provided should it exist in the database.
  - Once clicking on the reset link, the user is redirected to a form prompting for a new password and confirmation of that password.
  - Upon submitting the new password, the user is redirected to the login page.

  ![forgot password](/documents/forgot-password.png)
  ![reset password](/documents/reset-password.png)


  > As a frequent user, I want to have the ability to change my password so I can keep my account safe.

  - User can change password in the 'personal information' section after log in into their account.

  ![change password](/documents/change-password.png)


  > As a frequent user, I want to know which products are best sellers, so I can make better decision.

  - Displays six products which are selling the most.

  ![best sellers](/documents/best-sellers.png)


  > As a frequent user, I want to enter payment information in a safe and secure way so that I can checkout quickly with confidence.

  - Checkout is proceed with Stripe.
  - After clicking button 'go to secure payment' in order summary section, the user is moving to Stripe page, where their can make secure payment.
  - Stripe page contains:
    - order summary
    - email input
    - shipping address form
    - shipping method to choose
    - payment details inputs
    - 'pay' button

  ![payment](/documents/payment.png)


  > As a frequent user, I want to receive confirmation for my order so that I can have a proof of purchase.

  - After success payment, the user is moving to page, where their can see its order number.

  ![order no](/documents/order-no.png)


  > As a frequent user, I want to be able to write products review , so I can help others users with choosing the products.

  - The 'write review' button lead to new form where user can write a review about the product.

  ![write review](/documents/write-review.png)

  - To give a rating, the user should press the appropriate number of stars.
  - There is also a text area under the stars where users can write their opinions.

  ![review](/documents/leave-rev.png)

  - Review does not appear immediately in the product details page.
  - To be displayed, it must first be approved by the admin.


  > As a frequent user, I want to sign up for the Newsletter to email any major updates and/or changes to the website or organization.

  - The newsletter section is located in the bottom of home page.
  - After clicking the 'subscribe' button, a toast message appears with thanks for subscribing to the Newsletter and disappears by itself after a while.

  ![newsletter](/documents/newsletter.png)


  > As a frequent user, I want to be able to contact the platform owner so I can report any problems or ask questions.

  - In the contact section is a form that allows the user to send a message to the company owner.

  ![contact form](/documents/contact-form.png)


  > As a frequent user, I want to log in and logout so that I can access my profile safely.

  - The menu contains the 'login' option, which leads to the login form when pressed.
  - After entering their data, the user can log in to their profile.
  - After logging in, an 'logout' link appears in the 'my profile' menu that, when pressed, allows the user to log out.
  - Before the users log off, they are asked if they are sure they want to log out.

  ![log out question](/documents/log-out-q.png)
  

  > As a frequent user, I want to register for an account so I can make purchase.

  - The register page features a form asking users for their email address, and password.
  - Once submitted users will be asked to confirm their email address to complete the registration process.
  - Users will also be able to navigate to the login page, if they already have an account.
  - Once completed, the user is redirected to a home page.

  ![register page](/documents/register.png)
