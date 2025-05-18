
# Ember & ash

## UX
### Strategy
#### Project overview
Welcome to Ember & Ash, want a fine dining, elegant and fantastic customer experience? Look no further! With our website you can see the amazing offers we have. All or our fantastic cuisine is all up to date on our online menu's. Want to give us a visit? You can book online, any time for whenever you want.

The main components of the website is the home page, the menu, my profile and the booking pages. The project was made with a simplistic and yet an elegant feel and a posh look in mind. Eating out and finding instagramable food and experiences is the wants of the many nowadays. A fine dining experience would entail higher costs than the normal day out hence what I found with my extensive research is that our general customer base and targets would be young adults and mature adults. Simple and elegant is the focus of the website.

#### Project goals
For the goals of this project I have implemented a kanban board for organisation found [Here!](https://github.com/users/JamesBracken/projects/13/views/1)
My project goals are also displayed below


### Scope
#### Consistent features implemented

**Navbar**
![Navbar image when a user is logged out]()

For navigating around the website I used a bootstrap navbar and implemented this within the base.html to follow DRY(Dont repeat yourself). I added our company logo to further the mission of spreading awareness of our company and help drive footfall. All navigation across the website, any page which we can direct to is found in the navigation. The navigation is visible no matter which page you are on and no matter where you are on the page. The nav is always visible to help improve UX and to ease navigation around different pages of the site. The navigation follows the simplistic elegant look that the page has.

![Nav items on hover]()

To improve UX, nav items are underlined on hover.

![CTA on hover]()

To improve UX, nav items underlines are removed on hover.

![Navbar image when a user is logged in]()
When a user logs in the navbar updates to include user logged-in features. After login the user can now create bookings for our restaurant to ensure they have their own space. They can also access these bookings within the my profile section which also appears on login. The my profile section enables the display of already created user bookings and the updating and deleting of each of these. 

![CTA Booking]()
![CTA Login]()
Our Call to action buttons are also located within the navbar. These further our company's interests by helping to drive customers to the company goals of translating website visitors into account holding users and increasing bookings. The CTA navigation items are also underlined to attract focus to these buttons.

**Buttons**

![Buttons]()
Buttons across our website use the same design to keep a consistent feel to the website. They have a nice light brown color.


**Social media section**
![Social media section]()

A section which is a component of our footer, which is also found just above the footer on every page. Social media is a crucial component of every company nowadays, making sure your company has social media exposure can make or break a company. Social media is especially influential in the hospitality industry. Using the social media icons, users can be redirected to our social media pages where users can find more information about us  and help drive user interest in our company.

**Footer**
![Footer]()

Our footer is found at the bottom of every page. Here we help ensure our customers are aware of our opening times and how they can get into contact with us.

**Login(maybe modal)**
![Login image]()

**Signup(maybe modal)**
![Signup image]()

**Messages(user feedback)**

![]()

To improve UX we display feedback messages for our users at the top of our page. These feedback messages stand out so our users are able to immediately see the feedback and can understand what is happening. Users are able to understand if something worked or didnt and we can reduce user frustration by keeping them updated.
#### Unique features implemented 
#### Features left to implement

### Structure
#### Database model
#### Applications
The flow of information layout of your project, talk about how you place things to attract people to certain items like cta and the organisation of the nav, footer and page info
### Skeleton
#### Wireframes
Here is your wireframe and your ERD, a low fidelity guide for your project
### Surface
#### Colour scheme
#### Typography
#### Imagery
Talk about the appearance and design of your website, chosen design strategies, color palette etc

## Testing
Describe the other testing md file
## Deployment
### How to run this project locally

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