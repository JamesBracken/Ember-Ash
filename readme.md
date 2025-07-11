
# Ember & ash

## [ --> View the live deployed project here <--](https://ember-and-ash-58ab64713078.herokuapp.com/)

## Table of contents

- [UX](https://github.com/JamesBracken/Ember-Ash?tab=readme-ov-file#ux)
    - [Strategy](https://github.com/JamesBracken/Ember-Ash?tab=readme-ov-file#strategy)
        - [Project Overview](https://github.com/JamesBracken/Ember-Ash?tab=readme-ov-file#project-overview)
        - [Completed project goals](https://github.com/JamesBracken/Ember-Ash?tab=readme-ov-file#completed-project-goals)
        - [Uncompleted/Undone project goals](https://github.com/JamesBracken/Ember-Ash?tab=readme-ov-file#uncompletedundone-project-goals)
    - [Scope](https://github.com/JamesBracken/Ember-Ash?tab=readme-ov-file#scope)
        - [Consistent features implemented](https://github.com/JamesBracken/Ember-Ash?tab=readme-ov-file#consistent-features-implemented)
        - [Unique features implemented](https://github.com/JamesBracken/Ember-Ash?tab=readme-ov-file#unique-features-implemented)
        - [Development life cycle](https://github.com/JamesBracken/Ember-Ash?tab=readme-ov-file#development-life-cycle)
    - [Structure](https://github.com/JamesBracken/Ember-Ash?tab=readme-ov-file#structure)
        - [Database model](https://github.com/JamesBracken/Ember-Ash?tab=readme-ov-file#database-model)
        - [Security](https://github.com/JamesBracken/Ember-Ash?tab=readme-ov-file#security)
        - [Applications](https://github.com/JamesBracken/Ember-Ash?tab=readme-ov-file#applications)
    - [Skeleton](https://github.com/JamesBracken/Ember-Ash?tab=readme-ov-file#skeleton)
    - [Surface](https://github.com/JamesBracken/Ember-Ash?tab=readme-ov-file#surface)
        - [Colour scheme](https://github.com/JamesBracken/Ember-Ash?tab=readme-ov-file#colour-scheme)
        - [Typography](https://github.com/JamesBracken/Ember-Ash?tab=readme-ov-file#typography)
        - [Imagery](https://github.com/JamesBracken/Ember-Ash?tab=readme-ov-file#imagery)
- [Testing](https://github.com/JamesBracken/Ember-Ash?tab=readme-ov-file#testing)
- [Deployment](https://github.com/JamesBracken/Ember-Ash?tab=readme-ov-file#deployment)
    - [Github guide](https://github.com/JamesBracken/Ember-Ash?tab=readme-ov-file#github-guide)
    - [Additional setup DB, Cloudinary, Heroku, env.py](https://github.com/JamesBracken/Ember-Ash?tab=readme-ov-file#additional-setup-db-cloudinary-heroku-envpy)
- [Credits](https://github.com/JamesBracken/Ember-Ash?tab=readme-ov-file#credits)
    - [Content](https://github.com/JamesBracken/Ember-Ash?tab=readme-ov-file#content)
    - [Technologies used](https://github.com/JamesBracken/Ember-Ash?tab=readme-ov-file#technologies-used)
    - [Code and resources used](https://github.com/JamesBracken/Ember-Ash?tab=readme-ov-file#code-and-resources-used)
    - [Acknowledgements](https://github.com/JamesBracken/Ember-Ash?tab=readme-ov-file#acknowledgements)
## UX
### Strategy
#### Project overview
Welcome to Ember & Ash, want a fine dining, elegant and fantastic customer experience? Look no further! With our website you can see the amazing offers we have. All of our fantastic cuisine is all up to date on our online menus. Want to give us a visit? You can book online, any time for whenever you want.

The main components of the website is the home page, the menu, my profile and the booking pages. The project was made with a simplistic and yet an elegant feel and a posh look in mind. Eating out and finding instagramable food and experiences is the wants of the many nowadays. A fine dining experience would entail higher costs than the normal day out hence what I found with my extensive research is that our general customer base and targets would be young adults and mature adults. Simple and elegant is the focus of the website.

#### Project goals
For the goals of this project I have implemented a kanban board for organisation found [Here!](https://github.com/users/JamesBracken/projects/13/views/1). My project has also been organised with the moscow method separating each user story into must have, should have, could have and wont have. By organising my content with importance I can focus my attention on the most important components at any given time and stay on target([More on the moscow method here](https://github.com/JamesBracken/Ember-Ash?tab=readme-ov-file#development-life-cycle)).

My project goals are also displayed below

#### Completed project goals

*User story goals*

**User story 1: Home page(Must have)**
- As a user I first see a home page so that I can immediately understand the purpose of the website

**User story 2: User login and signup(Must have)**
- As a potential user, I would like to have the ability to make my own account and login

**User story 3: Full CRUD for menu items (Must have)**
- As an Admin I can Create, read, update and delete menu items so that I can keep the menu updated

**User story 4:Full CRUD for bookings (Must have)**
- As a user I can create, read update and delete bookings so that I can have a reserved table when I need

**User story 5: Restaurant menu(Must have)**
- As a potential client, I would like to be able to view the menu so that I can see if the menu is to my liking

**User story 6: Responsive website(Must have)**
- As a user, I would like the website to be responsive so I can use it on different devices

**User story 7: Navigation and footer(Must have)**
- As a user I can access a navigation bar and footer so that I can navigate around the website and find the information I need

#### Uncompleted/Undone project goals

**User story 8: View client booking details(Could have)**
- As a manager, I would like to be able to see individual client details on each booking so I can cater the customer experience to the client

**User story 9: Admins CRUD for user bookings(Should have)**
- As a manager, I would like to be able to read, delete and create bookings so I can correct any errors or cancel bookings

**User story 10: Improved display of available bookings(Should have)**
- As a signed-in user, after selecting a date there is a consolidated view of available times displayed so I can better understand the restaurant availability

**User story 11: View daily bookings(Should have)**
- As a manager, I would like to have a consolidated view of daily bookings details so I can organise seating

**User story 12: Newsletter(Should have)**
- As a owner, I would like to offer a newsletter so that I can keep our clients interested and help drive footfall and increase customer retention

**User story 13: Advanced alcohol orders(Could have)**
- As a signed-in user, I would like to be able to order wines and other alcohols ahead of my booking so I can have it served on arrival

**User story 14: Updated profile details(Could have)**
- As a user, I can edit my personal information so that I can keep it up to date

**User story 15: Table management system(Could have)**
- As a manager, I can view the tables which are booked and not booked from a table management system so I can organise my service

**User story 16: About page(Could have)**
- As a user, I would like to view more information about the website on an about page

**User story 17: Gallery(Could have)**
- As a user I can see images of the food so that I can get a better understanding each menu item and get enticed

### Scope
#### Consistent features implemented

**Navbar**
![Navbar image when a user is logged out, smaller devices](./static/images/readme/navbar-consolidated.PNG)

![Navbar image when a user is logged out, larger devices](./static/images/readme/navbar-large.PNG)

For navigating around the website I used a bootstrap navbar and implemented this within the base.html to follow DRY(Dont repeat yourself). I added our company logo to further the mission of spreading awareness of our company and help drive footfall. All navigation across the website, any page which we can direct to is found in the navigation. The navigation is visible no matter which page you are on and no matter where you are on the page. The nav is always visible to help improve UX and to ease navigation around different pages of the site. The navigation follows the simplistic elegant look that the page has.

![Nav items](./static/images/readme/nav-link.PNG)

To improve UX, nav items are underlined on hover.

![Nav items on hover](./static/images/readme/navbar-link-hovered.PNG)

CTA links

![CTA link](./static/images/readme/cta-link.PNG)

To improve UX, CTA link items underlines are removed on hover.

![CTA link on hover](./static/images/readme/cta-link-hovered.PNG)

![Navbar image when a user is logged in](./static/images/readme/navbar-logged-in.PNG)

When a user logs in the navbar updates to include user logged-in features. After login the user can now create bookings for our restaurant to ensure they have their own space. They can also access these bookings within the my profile section which also appears on login. The my profile section enables the display of already created user bookings and the updating and deleting of each of these. 

![CTA Booking](./static/images/readme/cta-link.PNG)
![CTA Login](./static/images/readme/cta-login-link.PNG)

Our Call to action buttons are also located within the navbar. These further our company's interests by helping to drive customers to the company goals of translating website visitors into account holding users and increasing bookings. The CTA navigation items are also underlined to attract focus to these buttons.

**Buttons**

![Buttons](./static/images/readme/button.PNG)

Buttons across our website use the same design to keep a consistent feel to the website. They have a nice light brown color.

**Social media section**

![Social media section](./static/images/readme/social-media-section.PNG)

A section which is a component of our footer, which is also found just above the footer on every page. Social media is a crucial component of every company nowadays, making sure your company has social media exposure can make or break a company. Social media is especially influential in the hospitality industry. Using the social media icons, users can be redirected to our social media pages where users can find more information about us  and help drive user interest in our company.

**Footer**

![Footer](./static/images/readme/footer.PNG)

Our footer is found at the bottom of every page. Here we help ensure our customers are aware of our opening times and how they can get into contact with us.

**Login modal**

![Login image](./static/images/readme/login-modal.PNG)

The login modal is found on every page on the navbar. A user can easily find the login link and login to their account. The login modal was made with ajax incorporated for error handling.

**Signup page**

![Signup image](./static/images/readme/signup-page.PNG)

The signup page, anyone can create an account for our website here. The page was made with django allauth.



**Django messages(user feedback)**

![Django messages](./static/images/readme/django-messages.PNG)

To improve UX we display feedback messages for our users at the top of our page. These feedback messages stand out so our users are able to immediately see the feedback and can understand what is happening. Users are able to understand if something worked or didnt and we can reduce user frustration by keeping them updated.


#### Unique features implemented 

**Home page** 

![Home page](./static/images/readme/home-page.PNG)

The landing page of our website, absolutely pivotal to a great first impression of a user visiting our website. The user can immediately understand the websites purpose through images and website content.


**Navigation cards(Home page)**

![Navigation cards](./static/images/readme/navigation-cards.PNG)

To help increase user interest upon visiting the site we have our navigation cards which are located on the home page. These help intrigue users into looking further into our website, linking to the menu, booking page and to also leave a review for us on Tripadvisor after a satisfied visit.


**Menu page(Main menu page)**

![Menu page](./static/images/readme/menu-page.PNG)


**Admin** menu page

![Menu page](./static/images/readme/admin-menu.PNG)

The main navigation for our menu's, here you can navigate to either the lunch or the dinner page.

**Add menu item(Main menu page)**

![Add menu button](./static/images/readme/add-menu-icon.PNG)

Using this add button, admins are easily able to add menu items. The add icon is only visible to admins so regular users are unable to add menu items. Admins only need to fill out the following form and items are instantly added to the lunch or dinner menu.

**Add menu item page**

![Add menu item page](./static/images/readme/add-menu-item-page.PNG)

This is the form to add items to either the lunch or the dinner menu. Admins can use this page to easily create dinner and lunch menu items. For each the admin is able to add descriptive text to grab customer interest and add beautiful imagery of each food item.

**Menu items**

![Menu item card](./static/images/readme/menu-item.PNG)

*Admin* menu item
![Menu item card](./static/images/readme/admin-menu-item.PNG)

Each menu item is created in a the same style each time. The user can get a consistent feel to the website across both menu's.

**Lunch menu page**

![Lunch menu page](./static/images/readme)

Any lunch menu item added by admins appear here. Each item gives descriptive text and beautiful imagery to further interest potential clients.


**Dinner menu page**

![Dinner menu page](./static/images/readme/dinner-menu-page.PNG)

**Admin** version of the page

![Dinner menu page](./static/images/readme/admin-dinner-menu-page.PNG)

Any dinner menu item added by admins appear here. Each item gives descriptive text and beautiful imagery to further insterest potential clients.

**Edit menu item icon**

![Edit menu item icon](./static/images/readme/edit-menu-item-button.PNG)

On each menu item in both the lunch and dinner pages, there is an edit icon which is accessible to site admins. Admins are able to update any information they want about the menu with a simple click of a button. They can add new images, change out text etc.

![Edit menu item form](./static/images/readme/edit-menu-item-form.PNG)

On click of the edit menu item icon, the user is directed to the form page where these items are also created. The data from the item is automatically added to the form to ease updating of each item.

**Delete menu item icon**

![Delete menu item icon](./static/images/readme/delete-menu-item-icon.PNG)

On each menu item in both the lunch and dinner pages, there is a delete icon which is accessible to site admins. Admins are able to delete outdated and no longer wanted items from the menu with ease.

![Confirm delete modal](./static/images/readme/delete-menu-item-confirmation-modal.PNG)

To ensure there is no accidental deletion users are also prompted one extra time to confirm deletion of any menu item.

**Make a booking page**

![Booking page](./static/images/readme/create-booking-page.PNG)

The making a booking page is a crucial component of our website. This is where we can translate a website visitor into a paying customer by getting them into our restaurant.
The user can set a time, date and amount of guests for each booking.

![Comments](./static/images/readme/create-booking-page-comments.PNG)

The user can additionally put any extra comments, normally guest allergens. This is crucial to ensure customer health and safety is maintained. Also any special requests can be added.

**My profile page**

![My profile page](./static/images/readme/my-profile-page.PNG)

On the my profile page users can find their details, previous and future bookings

**My details section**

![My details section](./static/images/readme/my-profile-section.PNG)

The users can see their input details, in future iterations of the project we will look to broaden this and add items like if a user wants newsletters and etc.

**My bookings section**

![My bookings section](./static/images/readme/my-bookings-section.PNG)

In the my booking section users are able to see any information about previous and future bookings.


**Edit bookings**

![Edit bookings icon](./static/images/readme/edit-booking-icon.PNG)

If a user wants to make some changes to a booking they are able to do that here. They can update any information about the booking up to a day before the booking. Once the day of the booking arrives users are no longer able to change booking times.

![Edit bookings page ](./static/images/readme/edit-bookings-page.PNG)

After clicking the edit icon the page loads the booking form and passes in the booking information to ease UX and updating bookings.

**Delete bookings**

![Delete bookings icon](./static/images/readme/delete-booking-icon.PNG)

If the worst case scenario happens and a user must delete their booking they can do that up until the day before the booking. Once the day of the booking arrives, users are no longer able to delete bookings. Users are also not allowed to delete any previous bookings.

![Confirm delete modal](./static/images/readme/delete-booking-confirmation-modal.PNG)

On click of the delete icon a user is prompted by a confirm deletion modal. This is to prevent any accidental deletions, after clicking the confirm delete on the modal bookings are deleted.

**Bookings page control**

![Booking page control](./static/images/readme/booking-page-control.PNG)

![Booking page control](./static/images/readme/booking-page-control-2.PNG)

To help improve UX, bookings are spread across multiple pages if there has been more than 5 bookings placed on a profile. Bookings are organised with future bookings at the start and older bookings at the end.

#### Development life cycle

In addition to the being able to visibly see the development life cycle in github through commit messages, I also have created a gantt chart which briefly displays the project life cycle over a few weeks.

**Gantt chart**

![Gantt chart of the development life cycle of the project](./static/images/readme/Gantt%20chart.PNG)

**Agile methodology**
This project followed the Agile methodology due to its much higher success rate and tendency to have better results over other approaches to programming like the waterfall approach. We created User stories at the planning and researching stage of the project which would each help to meet the goals and needs of the business. Each story was prioritised using the moscow method to ensure a MVP for the client in good time(More on the moscow method below). While following each user story for guidance we added features in an iterative manner, adding and improving the site iteratively(little by little) and adjusting the scope rather than adjusting the quality and deadlines of the end product. With this in mind we were able to finish the site within scope, on target deadline and without sacrificing any quality of the end product.  

**Moscow method**

To ensure that we are able to get a MVP(minimum viable product ) we used the moscow method during development to prioritize the most important components of the program first. Each item was organised with a Must have, Should have, Could have and wont have to be able to better organise resources and prioritise tasks. Following the moscow prioritisation helps us keep on track and assists us in project completion by the appointed deadline. 
### Structure

#### Database model

Before creating my database models I planned them out and made an [ERD(check here)](https://lucid.app/lucidchart/901dc3b0-5579-4334-a7fe-ccec98e905c7/edit?viewport_loc=-1103%2C-2521%2C2707%2C1327%2C0_0&invitationId=inv_bceffa0a-ecee-469b-9cc4-b49cac5be1cd). Using the ERD made I was able to better organise and structure my database models. 

My ERD model contains 5 models in total, however we will discount the django allauth model and the Pre ordered alcohol model as this was not made (out of scope). The models that were created within my project are the *Bookings*, *Menu* and *Customer(incomplete, out of scope of project)*. The ERD displays each model containing attributes. Each attribute is characterised by its field type, this dictates the data which can be accepted for example the Booking model's comment attribute which is a CharField, this can store characters in general.

All models within the ERD are inter-connected except for the Menu model which does not connect with any other tables. All fields within each model are required fields excluding the comments field within the booking model and the images which have default placeholders set. The Customer - Bookings models relationship is one to many, each user can have many bookings but each booking can only be tied to one user. The Customer model extracts data from django allauth which is the authentication system we use within this project.

A future iteration I would like to consider is adding in a limit on the amount of bookings per timeslot, as ofcourse a restaurant will have a limit on capacity and should not take more bookings than it is capable of taking.

![Entity relationship diagram](./static/images/readme/erd-diagram.PNG)

#### Security

Django has a lot to offer in terms of its security features, it has a lot built in which is accessible to the developer. In the current information age securing your information is crucial. 

Within this project I have implemented multiple layers of security. User authentication and checks ensures that each individual user can see only their own information. Each user should only be able to read and manipulate their own data.

The implementation of security within this project has been done at a model and a form level to ensure no spoofing is possible. Even if a malicious user attempted to change data within the console(**Spoofing**) they would not be able to submit and propagate this data to the back-end as the model and form requirements would stop it. Additionally to the security on the back-end we also display the errors at the front-end to ensure that users are made aware of any requirements, errors and mistakes. Additional to security measure put in place at the model and forms, we have also placed measures at the view level. Placing security measures at the view level adds another level of security, we can do this with class and function *mixins* and *decorators*.
I opted to use the decorators for this project. The appropriate decorators were added to each view which requires *login* or *admin* permissions. In this way only *logged in* users could access certain functionality and the same goes for *admins* 

#### Applications

Within this project, 3 apps have been created these would be:
- booking - This contains all the bookings functionality, full CRUD but the read component is displayed within the customer model
- menu - This model is for admins to manage which menu items are available on the website for users to see. This contains full CRUD
- customer(incomplete) - This model displays information about the user and is where users can see all the bookings which they have made. In future iterations users might be able to updated their details.

### Skeleton

**Wireframes**

My wireframes were constructed early on in the research phase of the project. Adjusting with scope and the needs of the project some components within the wireframes changed and may look slightly different on the finished product. Some future improvements and iterations of the project are included in the wireframe however are not on the current website. If anything on the website was too different however I did make sure to make this reflect on the wireframes.

- [All pages](https://www.figma.com/design/tnBvzkh8foONfZI9U8Cm8h/Milestone-project-3?node-id=3314-2&t=is3oYhE3KEk57FqV-1)

### Surface

#### Colour scheme

![Colour palette](./static/images/readme/color-palette.PNG)

I went with a lot of black and white for the website to create a simplistic yet elegant feel for the website. To complement these colours the website also used minimal amounts of Isabelline and the buttons were made with a brownish Chamoisee. Within the images is something simillar with dark and light colour schemes.
The colour scheme used in the website consists of colours:

Primary: #F2EEE8

Secondary: #90775A

White: #FFFFFF

Black: #454545


#### Typography

When I was thinking which fonts to go with for my website as I wanted elegant and simplistic. For headings to stand out I went with a nice PT serif, fonts were sourced from [Google fonts](https://fonts.google.com/)

Headings : PT Serif

![PT serif](./static/images/readme/pt-serif-font.PNG)

For the general text within the body I went with a simple and yet classic sans serif so that the general texts would complement the headings and not take attention away from them. This text comprises of majority of the text within the website.

Text/body : sans serif

#### Imagery

As they say "We eat with our eyes". In our digital, everything needs to be instagrammable world images are crucial. The best way to get customers from the website to our seats is to give them very appealing photos. I focused on using pictures with fantastic looking food. A lot of very bright pictures and also some very dark themed ones too, a good mix of both worlds!

I used [Pixabay](https://pixabay.com/) and [Pexels](https://www.pexels.com/) for uncopyrighted images.

Additionally I improved website performance and load times by compressing images with [Tiny png](https://tinypng.com/) and [Tiny jpg](https://tinyjpg.com/)

## Testing

All testing has been performed in a separate Testing.md file within the project, or you can click this [link](https://github.com/JamesBracken/Ember-Ash/blob/main/testing.md) to be brought to the testing md file.

## Deployment

### Github guide

**Cloning**
To clone a repository follow these steps

1. Login in to Github or create an account if you haven't already

2. Go to this project repository [Ember & Ash](https://github.com/JamesBracken/Ember-Ash)

3. Click on the *Code* button and select whether you would like to cline with HTTPS, SSH or the Github CLI and then copy the link shown

4. Open your terminal in your IDE/code editor of choice then change the current working directory to the location you would like to use for the cloned directory

5. Type "git clone" into the terminal and paste the link you copied in the third step then press Enter

6. To install the dependencies you can run **npm install** in your IDE(integrated development environment) terminal, the dependencies you need are listed in the package.json and package-lock.json files

**Commiting and Pushing Changes**

1. Open the termin in the directory of your cloned repository

2. Using "git status" check to see your changes are correct

3. If you are ready to commit  type "git add ." to stage all saved changes to be commited, you can alternatively use "git add YOUR_FILENAME" to stage specific files for commit

4. Using "git commit -m "Write your commit message here" commit your changes with a descriptive message, give a good amount of detail but try not to go over 50 characters

5. Finally use "git push origin main" to push your changes to the main branch of your github repository


**Forking**

To fork this repository follow these steps

1. Setup Git and make sure your git has github authentication

2. Go to the web page repository [Ember & Ash](https://github.com/JamesBracken/Ember-Ash) 

3. Click on *fork* on the upper right portion of the page.

4. This has now forked the repository to your own profile. 

5. Go to your profile and navigate to the forked repository.

6. Click on *Code* above the list of forked files

7. Choose the option you need from the dropdown menu. 

Further assistance can be found [HERE](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) on the github Fork a Repo page

**Local development**

1. Clone your repository from Github, you can find the "Code" button where you can copy the url from

2. Open your IDE and open a terminal, make sure you are in the correct directory where you want to clone the repository to.

3. Type git clone URL, replace URL with the one you just copied in the first step

4. Setup your virtual environment, type the below commands

- python3 -m venv [virtual_environment name]

5. Activate your virtual environment, type the below commands

- Windows: myvenv\Scripts\activate

- Linux/Mac: source myvenv/bin/activate

6. Type the below items into your IDE terminal, this will install all packages
    pip install -r requirements.txt

**If you want to install your own packages** here is some extra step-by-step instructions and examples:

- Type the below items into your IDE terminal
    pip install Django~=3.2 gunicorn (NOTE: try to use pip3 instead if this does not work)
- Install libraries your project will need like Postgresql(Handles database), psycopg2(Adapter for Postgresql), cloudinary storage(Allows long term storage of static files I.E. images) and whitenoise(serves compressed content)
    pip install dj_database_url psycopg2
    pip install dj3-cloudinary-storage
- Create your requirements.txt file, this is a list of your installed packages so everytime you install a new package you will need to update it like this
    pip freeze --local > requirements.txt

7. Setup environmental variables, scroll down to Environmental Variables section

8. Connect your database by typing this in the terminal(This runs your migrations):

- python manage.py migrate

9. Create a superuser account by typing into the terminal:

- python manage.py createsuperuser

10. You can run the app in a local environment by typing:

- python manage.py runserver

11. If you want to open a deployed version of your app see the steps below in 
**Heroku deployment**

### Additional setup DB, CLoudinary, Heroku, env.py
**Adding your database**

1. Navigate to [PostgreSQL from code institute](https://dbs.ci-dbs.net/)

2. Enter your student email address and then submit

3. You will be sent an email with a link, copy the link

4. Back in your workspace, ensure Debug is set to True

5. Create you env.py file if you dont have one already and add this to .gitignore

6. Inside your env.py add the below code and replace "your-database-URL" with the link you copied from the email in step 3

- import os

- os.environ.setdefault(
    "DATABASE_URL", "your-database-URL")

7. If you haven't already do 
- pip3 install dj-database-url~=0.5 psycopg2~=2.9

- pip3 freeze --local > requirements.txt

8. In your settings.py import the packages like below

- import os
- import dj_databse_url
- if os.path.isfile('env.py'):
    import env

9. Still in your settings.py comment out the default django sqlite3 database

10. Add in you own database with the below syntax

- DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

11. Migrate your changes with python manage.py migrate

12. You have now successfully connected your database withthe project and can now add data in your local development. To connect your deployed version on heroku with the database continue with the next steps.

13. If you haven't already, deploy your project to heroku(steps for this are found after database guide)

14. Navigate to the settings tab of your project and press reveal config vars

15. If there is a database added by default by heroku delete this as we will replace it with our own(If heroku has not added one skip to step 18)

16. To remove the heroku database navigate to Resources, go to the drop-down on the top right of the Postgres add-on and click Delete Add-on. Confirm this by typing your app's name into the popuo

17. Navigate back to the settings tab and to config vars

18. Add a new config var with a key of DATABASE_URL and a value of the PostgreSQL link that we copied from the email in step 3

19. You have successfully added your database to the deployed version of your website

**Adding Cloudinary to your project**

1. Install the nevessary packages with the commands below and add them to your requirements.txt file

- pip3 install cloudinary~=1.36.0 dj3-cloudinary-storage~=0.0.6 urllib3~=1.26.15

- pip3 freeze --local > requirements.txt

2. Go to [this link](https://cloudinary.com/users/register_free) to create a cloudinary account

3. In the Cloudinary dashboard, copy the CLOUDINARY_URL

4. In your env.py file add the code below and paste in the copied url from step 3 

- os.environ.setdefault(
    "CLOUDINARY_URL", "URL copied from Cloudinary in last step")

5. Delete the CLOUDINARY_URL= from the start of the URL string as we are using the setdefault() method rather than assigin the value.

6. Navigate to your settings.py and inside the INSTALLED_APPS add the below items

**Important!** cloudinary_storage must be added immediately after django.contrib.staticfiles
- 'cloudinary_storage',

- 'cloudinary',

7. You can now use Cloudinary in any app in your project

**Heroku Deployment**
1. Ensure the project repository has been uploaded to Github.

2. Login to the Heroku dashboard and create a new app.

3. Connect your GitHub repository to your Heroku app.

4. In the Settings tab, ensure that the Python Buildpack is added.

5. Set environment variables in the Config Vars section of the Settings tab.

6. In the Deploy tab, enable automatic deploys from your GitHub repository.

7. Click the "Deploy Branch" button to deploy the app.

8. Once the app has been deployed, click the "Open App" button to view the app.

**Environmental variables**

Environment Variables
For local deployment, you will need to create a .env file in the root directory of the project and set the environment variables in this file. This is to make sure sensitive information is separated from other code.

Ensure the .env file is included in the .gitignore file to exclude it from your GitHub repo to prevent the file and its contents from being publicly exposed.

For Heroku deployment, you will need to set the environment variables through the Heroku CLI or through the Heroku dashboard under 'Config Vars'.

You need to define the following environment variables:

SECRET_KEY(In both Heroku and env.py): The secret key for your Django project. This is a critical setting that's used for cryptographic signing, and should be kept secret at all times. It's used to provide cryptographic signing, and should be a long, random string of bytes.

DEBUG(In both Heroku and env.py): A boolean that turns on/off debug mode. Set to True for development to enable detailed error pages and logging for debugging. Set to False in production to improve performance and security.

DATABASE_URL(In both Heroku and env.py): The URL for your database. This should include the database engine, username, password, host, port, and database name. For a Postgres database, it typically looks like postgres://USER:PASSWORD@HOST:PORT/DB_NAME.

CLOUDINARY_API_KEY: Your Cloudinary account's API key. This key is used to authenticate requests to Cloudinary's services for uploading and managing images and other media assets.

CLOUDINARY_API_SECRET: Your Cloudinary account's API secret. This secret is used alongside the API key to securely sign requests to Cloudinary.

CLOUDINARY_CLOUD_NAME: Your Cloudinary account's cloud name. This is the unique name that identifies your cloud within Cloudinary. It's used in the URL structure for accessing uploaded resources.

Note: The following CLOUDINARY_CLOUD_NAME, CLOUDINARY_API_SECRET and CLOUDINARY_API_KEY can be placed in 1 config var in heroku and need to also be added to the settings.py file in this format: 

Local example:
CLOUDINARY_URL=cloudinary://<CLOUDINARY_API_KEY>:<CLOUDINARY_API_SECRET>@<CLOUDINARY_CLOUD_NAME>

Heroku example:
Key: CLOUDINARY_URL
Value: cloudinary://<CLOUDINARY_API_KEY>:<CLOUDINARY_API_SECRET>@<CLOUDINARY_CLOUD_NAME>

## Credits
### Content

Small pieces of other code has been added into the project, all of this has been acknowledged within the project itself. All links to where the code has been sourced are in comments above the code.

Any larger pieces of code should be added here in any future iterations and any changed within the project.

### Technologies used

1. [Django](https://www.djangoproject.com/) - Django is a high level framework used to rapidly take python projects from start to finish. Using django a developer can use existing codebases and shortcuts to ease and speed up the development process.

2. [PostgreSQL](https://www.postgresql.org/) - PosgreSQL is a powerful, open source object-relational database system.

3. [Code institute provided database generator](https://dbs.ci-dbs.net/) - A database generator provided by Code Institute to store data across projects.

4. [VS code](https://code.visualstudio.com/) - The most widely used IDE across the planet, we use vs code as our integrated development environment.

5. [Cloudinary](https://cloudinary.com/) - An fast scalable online media management platform

6. [Git](https://git-scm.com/) - A version control system designed to handle everything from small to large projects  

7. [GitHub](https://github.com/) - A platform for displaying code project version, deployments and developer profiles

8. [Github desktop](https://desktop.github.com/download/) - An app used to ease version control. 

9. [Figma](https://www.figma.com/) - An application used to make wireframe drawings

10. [TinyPNG](https://tinyjpg.com/) - Converts images into JPG format and compresses files to improve performance

11. [TinyJPG](https://tinypng.com/) - Converts images into PNG format and compresses files to improve performance

12. [Pixabay](https://pixabay.com/) - A media website including free and open source images

13. [Pexels](https://www.pexels.com/) - A media website including free and open source images

14. [Django widget tweaks](https://pypi.org/project/django-widget-tweaks/) - Used to tweak form fields within the project

15. [Gunicorn](https://gunicorn.org/) - A python WSGI HTTP server 

16. [Whitenoise](https://whitenoise.readthedocs.io/en/latest/) - Serves static files for projects in production

17. [Dj Database URL](https://pypi.org/project/dj-database-url/) - Connects our website with the database

18. [Psycopg2](https://www.psycopg.org/docs/) - PostgreSQL database adapter for python

19. [Chatgpt](https://chatgpt.com/) - Used to populate data in the project such as add menu items

20. [Favicon](https://favicon.io/favicon-generator/) - Generates a favicon for websites

21. [Bootstrap](https://getbootstrap.com/) - Used to create the Navigation bar, page structure, styles and responsiveness

22. [Google fonts](https://fonts.google.com/) - Generates fonts for the project

23. [Heroku](https://www.heroku.com/) - Used to deploy and manage a production ready version of the website

24. [Lucidchart](https://www.lucidchart.com/pages/examples/er-diagram-tool) - Used to create entity relationship diagrams 

### Code and Resources used

1. [Stackoverflow](https://stackoverflow.com/questions) - Platform and community where developers can ask questions and get assistance from eachother

2. [W3schools docs](https://www.w3schools.com/) - Lots of useful resources and guides for all programming languages in this project

3. [Mdn docs](https://developer.mozilla.org/en-US/) - Lots of useful resources and guides for all programming languages in this project

4. [Bootstrap docs](https://getbootstrap.com/docs/5.3/getting-started/introduction/) - Documentation for the bootstrap web library 

5. [Django project docs](https://www.djangoproject.com/start/) - Lots of useful documentation and guidance, especially for me to grasp and learn new concepts in the django framework

6. [Kevin powell how to make a color scheme fast](https://www.youtube.com/watch?v=mq8LYj6kRyE&list=PLpAzc76TtoBzvtYIZAhfJzDxvas0GmI7O) - Great guide on how to create your color scheme

7.[Guide to relational databases](https://www.youtube.com/watch?v=fXndSzAL1Nc&list=PLpAzc76TtoBzvtYIZAhfJzDxvas0GmI7O&index=2) - Crucial guide I used to help grasp the concepts of relational databases

8. [Fantastic video about normalizing your database](https://www.youtube.com/watch?v=UrYLYV7WSHM&list=PLpAzc76TtoBzvtYIZAhfJzDxvas0GmI7O&index=5) - A guide to normalise your database, with this I was able to create an optimal schema for my database and separate data into different tables to maximise performance and follow best practices. Best guide I have seen by far on databases. Simple and informative.

9. [Creating a Django restaurant booking site](https://www.youtube.com/watch?v=EI02wQ51GjA&list=PLBTOBXTz1YFZK0moSgoZq93V_AdvrUGSj) - Great guide which I watched to cement my understanding of django and give me inspiration and ideas on how to build my website, simple and straightforward explanations

10. [Guide to how ajax login works with django](https://www.youtube.com/watch?v=DvzE9tVFkSA&list=PLpAzc76TtoBzvtYIZAhfJzDxvas0GmI7O&index=15) - Slightly outdated video, but helped me grasp the concepts of how to use AJAX for error handling in my login modal.

11. Brian macharia(My mentor) - No link provided as these were privately shared resources for his students. Big shoutout to my mentor who provided tons of useful links to useful resources, guides and tutorials for this project. 

12. Code institute codestar project - Through this practice project I was able to cement hte fundamentals of the django framework and get a basis of how to go about implementing some of the functionality in my project.

### Acknowledgements

Again, a big thank you to my mentor **Brian Macharia** who gave me high level guidance for the project and to my teacher **Andre Beckley** who supported me and guided me through the website build.

A thanks as well to all the help and support from stackoverflow and the coding community. The helpfulness and support we all provide eachother was instrumental to making this project possible.

