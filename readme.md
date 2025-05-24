
# Ember & ash

## [ --> View the deployed project here <--](https://ember-and-ash-58ab64713078.herokuapp.com/)
## UX
### Strategy
#### Project overview
Welcome to Ember & Ash, want a fine dining, elegant and fantastic customer experience? Look no further! With our website you can see the amazing offers we have. All or our fantastic cuisine is all up to date on our online menu's. Want to give us a visit? You can book online, any time for whenever you want.

The main components of the website is the home page, the menu, my profile and the booking pages. The project was made with a simplistic and yet an elegant feel and a posh look in mind. Eating out and finding instagramable food and experiences is the wants of the many nowadays. A fine dining experience would entail higher costs than the normal day out hence what I found with my extensive research is that our general customer base and targets would be young adults and mature adults. Simple and elegant is the focus of the website.

#### Project goals
For the goals of this project I have implemented a kanban board for organisation found [Here!](https://github.com/users/JamesBracken/projects/13/views/1). My project has also been organised with the moscow method separating each user story into must have, should have, could have and wont have. By organising my content with importance I can focus my attention on the most important components at any given time and stay on target.

My project goals are also displayed below

#### Completed project goals

*User story goals*

**User story 1: Home page(Must have)**
- As a user I first see a home page so that I can immediately understand the purpose of the website

**User story 2: User login and signup(Must have)**
- As a potential user, I would liek to have the ability to make my own account and login

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

#### Uncompleted project goals

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

**User story 17: Gallery()**
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

To improve UX, nav items underlines are removed on hover.

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

To help increase user interest upon visiting the site we have our navigation cards which are located on the home page. These help intrigue users into looking further into our website, linking to the menu, booking page and to also leave a review for us on google after a satisfied visit.


**Menu page(Main menu page)**


![Menu page](./static/images/readme/admin-menu.PNG)

*Admin* menu page
![Menu page](./static/images/readme/menu-page.PNG)

The main navigation for our menu's, here you can navigate to either the lunch or the dinner page.

**Add menu item(Main menu page)**

![Add menu button](./static/images/readme/add-menu-icon.PNG)

Using this add button, admins are easily able to add menu items. The add icon is only visible to admins so regular users are unable to add menu items. Admin only need to fill out the following form and items are instantly added to the lunch or dinner menu.

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

*Admin*
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

### Structure

#### Database model

Before creating my database models I planned them out and made an [ERD(check here)](https://lucid.app/lucidchart/901dc3b0-5579-4334-a7fe-ccec98e905c7/edit?viewport_loc=-1103%2C-2521%2C2707%2C1327%2C0_0&invitationId=inv_bceffa0a-ecee-469b-9cc4-b49cac5be1cd). Using the ERD made I was able to better organise and structure my database models. 

My ERD model contains 5 models in total, however we will discount the django allauth model and the Pre ordered alcohol model as this was not made (out of scope). The models that were created within my project are the *Bookings*, *Menu* and *Customer(incomplete, out of scope of project)*. The ERD displays each model containing attributes. Each attribute is characterised by its field type, this dictates the data which can be accepted for example the Booking model's comment attribute which is a CharField, this can store characters in general.

All models within the ERD are inter-connected except for the Menu model which does not connect with any other tables. All fields within each model are required fields excluding the comments field within the booking model and the images which have default placeholders set. The Customer - Bookings models relationship is one to many, each user can have many bookings but each booking can only be tied to one user. The Customer model extracts data from django allauth which is the authentication system we use within this project.

![Entity relationship diagram](./static/images/readme/erd-diagram.PNG)

#### Applications

Within this project, 3 apps have been created these would be:
- booking - This contains all the bookings functionality, full CRUD but the read component is displayed within the customer model
- menu - This model is for admins to manage which menu items are available on the website for users to see. This contains full CRUD
- customer(incomplete) - This model displays information about the user and is where users can see all the bookings which they have made. 

### Skeleton
**Wireframes**
- [Home page]()
- [Menu page]()
- [Login]()
- [Signup]()
- [My profile]()
- [Booking form page]()
- [Add menu item form page]()

ADD ANY OTHER PAGE IE IF WE MAKE A CONFIRM SIGNOUT PAGE ETC.
- []()
- []()

Here is your wireframe and your ERD, a low fidelity guide for your project
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

When I was thinking which fonts to go with for my website as I wanted elegant and simplistic I went with a very classic Sans serif for the body content. For headings to stand out I went with a nice PT serif, fonts were sourced from [Google fonts](https://fonts.google.com/)

Headings : PT Serif

![PT serif](./static/images/readme/pt-serif-font.PNG)

Text/body : sans serif


#### Imagery

As they say "We eat with our eyes". In our digital, everything needs to be instagrammable world images are crucial. The best way to get customers from the website to our seats is to give them very appealing photos. I focused on using pictures with fantastic looking food. A lot of very bright pictures and also some very dark themed ones too, a good mix of both worlds!

I used [Pixabay](https://pixabay.com/) and [Pexels](https://www.pexels.com/) for uncopyrighted images.

Additionally I improved website performance and load time by compressing images with [Tiny png](https://tinypng.com/) and [Tiny jpg](https://tinyjpg.com/)

## Testing

All testing has been performed in a separate Testing.md file which can be found in this project 
## Deployment

### Github guide

**Cloning**
To clone a repository follow these steps

1.Login in to Github or create an account if you haven't already

2.Go to this project repository [Ember & Ash](https://github.com/JamesBracken/Ember-Ash)

3.Click on the *Code* button and select whether you would like to cline with HTTPS, SSH or the Github CLI and then copy the link shown

4.Open your terminal in your IDE/code editor of choice then change the current working directory to the location you would like to use for the cloned directory

5.Type "git clone" into the terminal and paste the link you copied in the third step then press Enter

6.To install the dependencies you can run **npm install** in your IDE(integrated development environment) terminal, the dependencies you need are listed in the package.json and package-lock.json files

**Commiting and Pushing Changes**

1.Open the termin in the directory of your cloned repository

2.Using "git status" check to see your changes are correct

3.If you are ready to commit  type "git add ." to stage all saved changes to be commited, you can alternatively use "git add YOUR_FILENAME" to stage specific files for commit

4.Using "git commit -m "Write your commit message here" commit your changes with a descriptive message, give a good amount of detail but try not to go over 50 characters

5.Finally use "git push origin main" to push your changes to the main branch of your github repository


**Forking**

To fork this repository follow these steps

1.Setup Git and make sure your git has github authentication
2.Go to the web page repository [Ember & Ash](https://github.com/JamesBracken/Ember-Ash) 
3.Click on *fork* on the upper right portion of the page.
4.This has now forked the repository to your own profile. 
5.Go to your profile and navigate to the forked repository.
6.Click on *Code* above the list of forked files
7.Choose the option you need from the dropdown menu. 

Further assistance can be found [HERE](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) on the github Fork a Repo page

**Local development**
1.Clone your repository from Github by, you can find the "Code" button where you can copy the url from
2.Open your IDE and open a terminal, make sure you are in the correct directory where you want to clone the repository to.
3.Type git clone URL, replace URL with the one you just copied in the first step
4.Setup your virtual environment, type the below commands
    python3 -m venv [virtual_environment name]
5.Activate your virtual environment, type the below commands
Windows: myvenv\Scripts\activate
Linux/Mac: source myvenv/bin/activate
6.Type the below items into your IDE terminal, this will install all packages
    pip install -r requirements.txt

If you want to install your own packages here is some extra step-by-step instructions:

- Type the below items into your IDE terminal
    pip install Django~=3.2 gunicorn (NOTE: try to use pip3 instead if this does not work)
- Install libraries your project will need like Postgresql(Handles database), psycopg2(Adapter for Postgresql), cloudinary storage(Allows long term storage of static files I.E. images) and whitenoise(serves compressed content)
    pip install dj_database_url psycopg2
    pip install dj3-cloudinary-storage
- Create your requirements.txt file, this is a list of your installed packages so everytime you install a new package you will need to update it like this
    pip freeze --local > requirements.txt

7.Setup environmental variables, scroll down to Environmental Variables section
8.Connect your database by typing this in the terminal(This runs your migrations):
    python manage.py migrate
9.Create a superuser account by typing into the terminal:
    python manage.py createsuperuser
10.You can run the app in a local environment by typing:
    python manage.py runserver
11.If you want to open a deployed version of your app see the steps below in Heroku deployment

**Heroku Deployment**
1.Ensure the project repository has been uploaded to Github.
2.Login to the Heroku dashboard and create a new app.
3.Connect your GitHub repository to your Heroku app.
4.In the Settings tab, ensure that the Python Buildpack is added.
5.Set environment variables in the Config Vars section of the Settings tab.
6.In the Deploy tab, enable automatic deploys from your GitHub repository.
7.Click the "Deploy Branch" button to deploy the app.
8.Once the app has been deployed, click the "Open App" button to view the app.


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
### Technologies used
### Media
### Code used
### Acknowledgements

* For my modal I copied code from the Bootstrap docs and tweaked it
[Bootstrap Modals](https://getbootstrap.com/docs/4.0/components/modal/)

* For the time for loop adding in the available booking times 
[Time for loop](https://stackoverflow.com/questions/51164326/how-can-i-add-choices-to-a-timefield-in-a-django-form)
HOUR_CHOICES = [(datetime.time(hour=x), '{:02d}:00'.format(x)) for x in range(9, 23)]


### Acknowledgements
Separate md Testing