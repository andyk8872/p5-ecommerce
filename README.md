## [Table of Contents](#table-of-contents)
* [Purpose](#purpose)
* [User Experience Design (UX)](#user-experience-design)
  * [Epics and User Stories](#epics-and-user-stories)
* [Agile Methodology](#agile-methodology)     
* [Design](#design)
  * [Wireframes](#wireframes)
  * [Colour Scheme](#color-scheme)
  * [Typography](#typography)
  * [Database Schema](#database-schema)
* [Business Model](#business-model)  
* [Structure](#structure)
  * [Logic](#logic)
* [Features](#features)
  * [Home Page](#home-page)
  * [Navigation](#navigation)
  * [Footer](#footer)
  * [Login/Logout/Register](#login-logout-register)  
  * [Make Booking](#make-booking)
  * [Delete Booking](#delete-booking)
  * [Edit Booking](#edit-booking)
  * [View Booking](#view-booking)
  * [Contact](#contact)
  * [Make Review](#make-review)
  * [View Review](#view-review)
  * [Administration](#administration)
* [Technologies Used](#technologies-used)
* [Libraries](#libraries)
* [Security and Authentification](#security-and-authentification)
* [Testing](#testing)
  * [Manual Testing](#manual-testing)
    
* [Bugs](#bugs)
* [Credits](#credits)
* [Deployment](#deployment)
* [Credits](#credits)
   * [Code and Tutorials](#code-and-tutorials)
* [Acknoledgements](#acknowledgements)

# AJK FURNITURE SITE
## Purpose:
### Goal:
#### To allow individuals customers to visit the site view the furniture suites available and purchase via an online payment system.
#### To provide a visual and interactivity so that the user will be able to fulfil their objectives.
This is a furniture suite shopping site where customers can view furniture suites for various rooms. They can also view the individual details and view the reviews given by previous customers. They can register as site members and view previous purchases as well as make their own reviews. They can also create a shopping bag and arrange online payment.

### Business Goals:

The main goal of this project is to give a user the ability to make bookings. User should also should also be able to make updates to their account in via their account. The user should also be able to give a review.

### Target Audience:

The target audience are customers that they feel would benefit with the ease from shopping online, be able to view the suites visually as well as look at the reviews from previous customers.

* [Back to contents](#table-of-contents)

The live website can be found [here](https://ajk-furniture.herokuapp.com/).

*** 
## User Experience Design

## Agile Methodology

### Github Project Board

* Although not specially designed for this the project board in github works well enabling me to track my user stories.
* This enabled me to manage the project by breaking it up into several phases.
* Once the project had started it allowed me to cycle through the process to planning, executing and evaluating.
* The framework used is the Kanban board - a form of visual project management.

### Epics and User Stories

* #### Epic 1 - Home Page (Milestone 1)
    |  User Story ID  |    User Type   |  Content  |   App   | MoSCoW Label |
    | --------------- | -------------- | --------- | --------| -------------|
    | [#1](https://github.com/andyk8872/p5-ecommerce/issues/1)  | As a customer | As a user I can view the site so that I can determine the function/purpose of the site | Home | Must Have |
    |  [#2](https://github.com/andyk8872/p5-ecommerce/issues/2)  | As a customer | As a user I can traverse the site so that I can fulfil my aims | Home | Must Have |
* #### Epic 2 - Products (Milestone 1)
    |  User Story ID  |    User Type   |  Content  |   App   | MoSCoW Label |
    | --------------- | -------------- | --------- | --------| -------------|
    [#3](https://github.com/andyk8872/p5-ecommerce/issues/3)  | As a customer | As a user I can view the products so that I can view their description, price and image | Products | Must Have
    [#4](https://github.com/andyk8872/p5-ecommerce/issues/4)  |  As a customer | As a user I can search the products so that view and compare descriptions, prices and types. | Products | Must Have
    [#8](https://github.com/andyk8872/p5-ecommerce/issues/8)  | As a customer | As a user I can view the details of each product and add it to my shopping cart so that get a more detail on the product and add to my cart to possibly purchase at a later stage | Products | Must Have
* #### Epic 3 - Profile/Account (Milestone 1)
    |  User Story ID  |    User Type   |  Content  |   App   | MoSCoW Label |
    | --------------- | -------------- | --------- | --------| -------------|
    [#5](https://github.com/andyk8872/p5-ecommerce/issues/5)  | As a customer | As a user/administrator I can register an account so that I can manage my activities related to my account. | Profiles | Must Have
    [#6](https://github.com/andyk8872/p5-ecommerce/issues/6)  | As a customer | As a user/administrator I can receive an email so that I can confirm my identity | Profiles | Must Have
    [#7](https://github.com/andyk8872/p5-ecommerce/issues/7)  | As a customer | As a user/administrator I can reset my password so that I can retrieve my account if password forgotten | Profiles | Must Have
* #### Epic 4 -  Shopping Cart (Milestone 1)
    |  User Story ID  |    User Type   |  Content  |   App   | MoSCoW Label |
    | --------------- | -------------- | --------- | --------| -------------|
    [#9](https://github.com/andyk8872/p5-ecommerce/issues/9)  | As a customer | As a user I can view the shopping cart so that I can see what products I have, the quantity and the total/individual cost | Cart | Must Have
    [#10](https://github.com/andyk8872/p5-ecommerce/issues/10)  | As a customer | As a user I can update the shopping cart so that I can add, subtract or remove products before going to checkout. | Cart | Must Have
    [#11](https://github.com/andyk8872/p5-ecommerce/issues/11)  | As a customer | As a customer I can view a summary of my shopping cart including the amounts so that when I proceed to payment I know what I am buying and for how much | Cart | Must Have
* #### Epic 5 -  Checkout (Milestone 1)
    |  User Story ID  |    User Type   |  Content  |   App   | MoSCoW Label |
    | --------------- | -------------- | --------- | --------| -------------|
    [#12](https://github.com/andyk8872/p5-ecommerce/issues/12)  | As a customer | As a user I can fill in my delivery and payment details so that I can arrange delivery details a pay for the items in my shopping bag. | Checkout | Must Have
    [#13](https://github.com/andyk8872/p5-ecommerce/issues/13)  | As a customer | As a user I can view the shopping cart so that **I can see what I am looking to purchase ** | Profiles | Must Have
    [#14](https://github.com/andyk8872/p5-ecommerce/issues/14)  | As a customer | As a user I can enter my credit card details and delivery details so that arrange payment and delivery of purchases | Checkout | Must Have
    [#15](https://github.com/andyk8872/p5-ecommerce/issues/15)  | As a customer | As a user I can receive confirmation of my order so that I know my purchase has been processed and payment received | Checkout | Must Have

* [Back to contents](#table-of-contents)  

***

## Design
### Wireframes:
***
### Color Scheme:
***
### Typography:
***
## Structure
### Logic/ERD (diagrams)
***
## Features
***
# Business Model

#### Business Overview

The business is a B2C e-commerce platform whose goal is to provide products to it's diverse range of customers through an online store.

The benefits for the business owner are:

1. Easy to scale the business as it grows.
2. No need to set up a physical location.
3. Can cater to customers globally or locally with equal ease.
4. With the sales portal only online changes with the market, either global or local can be ajusted to with relative ease.
5. Relatively low cost in starting up which allows for a larger portion of the budget to be used for customer aquisition. ie Ads / marketing
6. Low price point would encourage impulse buying from customers who may be considering purchasing from the business.


The cons of this business model are:

1. Getting customers initally can be difficult due to saturation in certain industries
2. Establishing a brand from the ground up takes time and immediate results are unlikely without a sound marketing strategy.
3. Getting customers organically takes time so the business would need to manually market the business or use paid advertising.
4. Not having a physical business can make it harder to build trust and loyalty with customers without offering discounts and offers.

A subscription model would not be viable initially. This could only be addressed after a period of time and with the possibility of additional services. 


* [Back to contents](#table-of-contents)
---

#### Site User
User 1: The typical site user would be a male/female aged between 18 and 70 who has an interest in tailoring, clothes designing and presenting a good outfit. 

User 2: Additional site users could be partners of user 1 and may be browsing the site to purchase gifts for them.

---

####  Goals for the website
The goals for the website are:
- An easy to navigate website with clear purpose
- Provide users with products that meet their expectations
- Allow users to view, read and comment on articles that may help or interest them.
- Allow users to give their review on any product.
- Allow users to add products to a wishlist of theirs.
- To provide users with insights or tips on  machine maintenance and tips to choose the right fabrics for clothing.
- Allow users to checkout quickly and easily
- To allow users to create a profile to view past orders and update profile information

---

#### Marketing Strategy
The businesses marketing strategy going forward is:

1. Promote the store through it's facebook business page. This can be viewed in the SEO section.
2. Utilise various social media platforms, and using Google ads and other paid services budget allowing.
3. Have a soft online launch sale to encourage early adoption and purchases from prospective clients
4. Utilizing services such as mailchimp, create a regular newsletter, blog site and create an extensive mailing list.
5. Write meaningful and helpful articles / blog articles to help with SEO ranking in search engines like google.
6. Set up multiple ads with a different product as the cover image, track the click through rate and stick with the high peformers.
7. Depending on budget the business may look at promoting it's custom made products to influencers in the brands niche, offering complimentary goods or a small fee for a shout out  or review. Ideally targetting low to medium influencers with a following of at least 10k in target niche. This would be realistic with a low budget for the business starting off and can start pushing traffic towards the site. 

* [Back to contents](#table-of-contents)
***
## Deployment
The project has been deployed to Heroku. Detail of the steps taken to deploy the project can be found [here](DEPLOYMENT.md)