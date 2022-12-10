# **NORAH'S CERAMICS WEBSITE**

## **INTRODUCTION**

![mockup](/documents/responsive.png)

Norah's Ceramics - an online shop with handmade ceramic and glass products and also zero waste accessories for kitchen and bathroom.
This e-commerce business is B2C oriented, so the owner is selling their products to individual customers.
The company's goal is to promote environmentally friendly products and reduce environmental pollution with plastic.
The website owner and main artist is a woman, so the website is targeted mainly at women. The design is very feminine. Due to the fact that Norah's Ceramics is a new company on the market and it does not have many customers yet, the products are produced on an ongoing basis. In case of a need to increase production in the future, the 'stock' option will be introduced to keep track of stocks.

Using the principles of UX design, this fully responsive and interactive website was developed using HTML, CSS, JavaScript and Python, and Django as a framework.

- ### **Strategy**

  More and more people are becoming aware of the pollution of our planet with plastic.
  The purpose of the created online store is to promote items that are handcrafted from environmentally friendly ingredients and to minimize the use of plastic.
  Zero waste accessories are made of recycled products or natural materials.

  - #### **Site owner goal**

    - To increase online presence
    - To promote eco friendly products.
    - To find as many customers as possible.
    - Convert interest into sales.

  - #### **User goals**
    - To access a user-friendly website across multiple devices.
    - To discover eco-friendly products for everyday use.
    - Reduce plastic pollution.
    - Find unusual products.

  - #### **Organization of functionality and content**

    - Header: Logo and a collapsible menu with navigational links.
    - Homepage: Give an overview of the website purpose, including hero images and text, three links for three product categories, and a link for 'shop all', which leads to all products.
    - Best Sellers: Displays six best-selling products.
    - New collection: Information about new ceramic decor collection with link which leads to list of this products.
    - Why us?: Information on the benefits of purchases in store.
    - Our values: Information about store values.
    - About: Information about the owner and company.
    - Contact: The form allows users to send an inquiry to the website owner.
    - Product page: Display product details.
    - Register: This contains the form for registering an account.
    - Login: This contains the form for logging in to the account.
    - Shopping bag: Display items added in the bag.
    - Newsletter: Form for subscribing to the newsletter.
    - My profile - Personal Information: Contain forms for update personal and address information, link to change password and link to delete account.
    - My profile - Orders: Contain information about user orders history.
    - My profile - Reviews: Contain information about user reviews history.
    - Footer: Links to social media, policies and contact information.

    - **User**

      - The Django default User model is replaced by the custom AbstractUser.
      - During authentication, the application uses an email address to identify uniquely.
      - Stores users' registration information provided upon signing up.

    - **AddressDetails model**

      - Stores site users' detailed address information.
      - Address using a one-to-one relationship with the user model.
      - This model is used to generate an address form in the user profile.

    - **Productrreview model**

      - Stores review details about the product such as stars rating and review description.
      - Related to the product model and user model.

    - **Product model**

      - Stores detailed information about a product to be displayed in product detail page.
      - Related to the subcategory and color model.

    - **Category model**

      - Stores product categories.
      - Related to the subcategory model.

    - **Subcategory model**

      - Stores product subcategories.
      - Related to the category model.

    - **Color model**

      - Stores product colors.

    - **Newsletteruser model**

      - Stores users subscribed to the newsletter.
      - Connected via webhook with "Mailchimp" service.
      - If the user resigns from receiving the newsletter, "Mailchimp" creates a request to the webhook, and the endpoint changes subscription status in the database.

    - **Basket model**

      - Contains all logic related to basket operations: add product, subtract product, delete product, total basket price, total basket products qty, basket summary.
      - Related to the user model.

    - **Basketproduct model**

      - Stores basket products.
      - Related to the basket model and product model.

    - **Order model**

      - Contains all information about order.
      - Related to the user model.

    - **Orderproduct model**

      - Stores ordered products.
      - Related to the order model and product model.

## **CRUD operations and defensive design**

- ### **CRUD operations**

  | Operations                       | all users | auth. user | superuser |
  | -------------------------------- | --------- | ---------- | --------- |
  | View homepage                    | Yes       | Yes        | Yes       |
  | View about page                  | Yes       | Yes        | Yes       |
  | View contact page                | Yes       | Yes        | Yes       |
  | View newsletter page             | Yes       | Yes        | Yes       |
  | Add/edit/delete profile          | No        | Yes        | Yes       |
  | Add/edit/delete a products       | No        | No         | Yes       |
  | View product details             | Yes       | Yes        | Yes       |
  | Add/edit/delete product category | No        | No         | Yes       |
  | Login                            | No        | Yes        | Yes       |
  | Register                         | Yes       | No         | No        |
  | Edit/delete reviews              | No        | No         | Yes       |
  | View all reviews                 | No        | Yes        | Yes       |
  | Add a review                     | No        | Yes        | Yes       |
  | View order history and details   | No        | Yes        | Yes       |
  | View shopping basket             | Yes       | Yes        | Yes       |
  | Checkout page                    | Yes       | Yes        | Yes       |

## **TECHNOLOGIES USED**

- ### **Languages**

  - [HTML](https://html.spec.whatwg.org/multipage/)
  - [CSS](https://www.w3.org/Style/CSS/Overview.en.html)
  - [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
  - [Python](https://www.python.org/)

- ### **Databases platform and cloud storage**

  - [Postgres](https://www.postgresql.org/): database engine used during development.

- ### **Libraries and frameworks**

  - [Django](https://www.djangoproject.com/): Python web framework for rapid development and clean, pragmatic design.
  - [Django Phonenumber Field](https://pypi.org/project/django-phonenumber-field/0.2a3/): uk phone numbers validation.
  - [Django cleanup](https://pypi.org/project/django-cleanup/): to automatically delete images / files when an ImagField is removed / updated or deleted.
  - [Flake8](https://pypi.org/project/flake8-django/): A plugin to detect bad practices on Django projects.

- ### **Other technologies**

  - [Google fonts](https://fonts.google.com/): used for body and headings font.
  - [Font Awesome](https://fontawesome.com/): used for icons throughout the website.
  - [Mailchimp](https://mailchimp.com/): Marketing platform used for newsletter.
  - [Stripe](https://stripe.com/gb): Payment.
  - [Termly](https://termly.io/): Policies.
  - [Dbdiagram.io](https://dbdiagram.io/home): to design schema of relational database.
  - [W3C Markup Validation Service](https://validator.w3.org/): to check there's not error in HTML.
  - [W3C CSS Validator](https://jigsaw.w3.org/css-validator/): This tool was used to check there's no error in the CSS code.
  - [PEP8 online](http://pep8online.com/): to validate python syntax.
  - [Chrome DevTools](https://developer.chrome.com/docs/devtools/): Google inspect was used to test and fix code and page responsiveness.
  - [Visual Studio Code](https://code.visualstudio.com/): was used to create and store code.
  - [GitHub](https://github.com/): used to store the code of the project.

- ### **Media and content**

  - Text and products photos was taken from [wearth](https://www.wearthlondon.com/) website.

  - [Unsplash](https://unsplash.com/): for images
  - [Lottiefiles](https://lottiefiles.com/): for used animations
  - [Pixlr](https://pixlr.com/pl/): was used to process used photos
  - [CSS Scan](https://getcssscan.com/css-box-shadow-examples): for box shadow example
  - [Free Frontend](https://freefrontend.com/): for CSS and JavaScript inspirations
  - [Crello](https://create.vista.com/pl/home/): for create the logo
  - [Mdigi](https://mdigi.tools/): for create gradients
  - [Freepik](https://www.freepik.com/): for images
