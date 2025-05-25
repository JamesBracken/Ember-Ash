# Testing

## Difficult to solve bugs

When implementing my login modal I experienced problems with my modal. It was appearing behind the modal backdrop. In the documentation Bootstrap stipulates modals tend to act differently when placed into fixed components hence the issues.

![alt text](./static/images/testing/modal_z_index.PNG)

I fixed this problem by taking the modal code out of the header and placing it at the bottom of the body. I also set a z-index for both the modal and modal backdrop as an extra defensive measure.

![alt text](./static/images/testing/modal_z_index_solved.PNG)

## Validator testing

### HTML validator

Testing tool - [W3C HTML Validation website]

I validated all pages across my website, everything was successful and **passed**! 

[Home page](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fember-and-ash-58ab64713078.herokuapp.com%2F) - Passed

[Signup page](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fember-and-ash-58ab64713078.herokuapp.com%2Faccounts%2Fsignup%2F) 
- 1 error displays which is a Duplicate ID error. This can be ignored as there is no conflict here. 1 of the ID's is the signup form, the other is from the login modal which is in the base.html therefore available to every page. The ID attributes of these elements are injected in with Django and allauth and CANNOT be changed

[Booking page](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fember-and-ash-58ab64713078.herokuapp.com%2Fbooking%2F) - Passed

[Main menu page](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fember-and-ash-58ab64713078.herokuapp.com%2Fmenu%2F) - Passed

[Lunch page](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fember-and-ash-58ab64713078.herokuapp.com%2Fmenu%2Flunch_menu%2F) - Passed

[Dinner page](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fember-and-ash-58ab64713078.herokuapp.com%2Fmenu%2Fdinner_menu%2F) - Passed

[My profile page](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fember-and-ash-58ab64713078.herokuapp.com%2Fmy_profile%2F) - Passed

[Logout page](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fember-and-ash-58ab64713078.herokuapp.com%2Faccounts%2Flogout%2F) - Passed

403 page - Did not check, main 404 error page was checked however I left the other error pages out. Attempting to check these was taking way too much time which would take me out of the scope of this project and django security made it very hard to invoke these error pages.

404 page - Passed

![Error 404 page](./static/images/testing/html-validator-404-error-page.PNG)

405 page - Did not check, main 404 error page was checked however I left the other error pages out. Attempting to check these was taking way too much time which would take me out of the scope of this project and django security made it very hard to invoke these error pages.


500 page - Passed

![Error 500 page](./static/images/testing/html-validator-500-error-page.PNG)

### CSS validator

I ran my CSS validation using [Jigsaw W3](https://jigsaw.w3.org/css-validator/)

Since I am not embedding any styles and I am using bootstrap classes for any inline styles (All bootstrap styles are standardized and tested already), there is no need to do multiple tests. The only necessary test here is directly testing the stylesheet. **Passed**

[CSS file](https://jigsaw.w3.org/css-validator/validator?lang=en&profile=css3svg&uri=https%3A%2F%2Fember-and-ash-58ab64713078.herokuapp.com%2Fstatic%2Fcss%2Fstyle.css&usermedium=all&vextwarning=&warning=1) - Passed

### JSHint validator

I validated my JS filed with [JSHint](https://jshint.com/)

All javascript files **passed** with no issues!

[booking.js]() - Passed

- All warning were just to inform that the features are for ES6+

- The undefined bootstrap in this js file is obviously bootstrap, this is the modal which is declared on line 5

![JShint containing the booking.js code](./static/images/testing/jshint-booking.PNG)

[login.js]() - Passed

- All warning were just to inform that the features are for ES6+

- One warning states the body of a for in should be wrapped in an if statement to filter unwanted properties from the prototype. This in fact is wrapped within the *else* block of an if statement to filter what is needed and not needed.

![JShint containing the login.js code](./static/images/testing/jshint-login.PNG)

[menu.js]() - Passed

- All warning were just to inform that the features are for ES6+

![JShint containing the menu.js code](./static/images/testing/jshint-menu.PNG)

### Python validation

booking/admin.py
![Pep8 validation for booking admin.py](./static/images/testing/pep8-booking-admin.PNG)

booking/apps.py

![Pep8 validation for booking apps.py](./static/images/testing/pep8-booking-apps.PNG)

booking/forms.py

![Pep8 validation for booking forms.py](./static/images/testing/pep8-booking-forms.PNG)

booking/models.py

![Pep8 validation for booking models.py](./static/images/testing/pep8-booking-models.PNG)

booking/tests.py

![Pep8 validation for booking tests.py](./static/images/testing/pep8-booking-tests.PNG)

booking/urls.py

![Pep8 validation for booking urls.py](./static/images/testing/pep8-booking-urls.PNG)

booking/views.py

![Pep8 validation for booking views.py](./static/images/testing/pep8-booking-views.PNG)

ember_ash/asgi.py

![Pep8 validation for ember ash .py](./static/images/testing/pep8-ember-ash-asgi.PNG)

ember_ash/context_processors.py

![Pep8 validation for ember ash context_processors.py](./static/images/testing/pep8-ember-ash-context-processors.PNG)

ember_ash/middleware.py

![Pep8 validation for ember ash middleware.py](./static/images/testing/pep8-ember-ash-middleware.py)

ember_ash/settings.py

![Pep8 validation for ember ash settings.py](./static/images/testing/pep8-ember-ash-settings.PNG)

ember_ash/urls.py

![Pep8 validation for ember ash urls.py](./static/images/testing/pep8-ember-ash-urls.py)

ember_ash/views.py

![Pep8 validation for ember ash views.py](./static/images/testing/pep8-ember-ash-views.PNG)

ember_ash/wsgi.py

![Pep8 validation for ember ash wsgi.py](./static/images/testing/pep8-ember-ash-wsgi.PNG)

menu/admin.py

![Pep8 validation for menu admin.py](./static/images/testing/pep8-menu-admin.PNG)

menu/apps.py

![Pep8 validation for menu apps.py](./static/images/testing/pep8-menu-apps.PNG)

menu/forms.py

![Pep8 validation for menu forms.py](./static/images/testing/pep8-menu-forms.PNG)

menu/models.py

![Pep8 validation for menu models.py](./static/images/testing/pep8-menu-models.PNG)

menu/tests.py

![Pep8 validation for menu tests.py](./static/images/testing/pep8-menu-tests.PNG)

menu/urls.py

![Pep8 validation for menu urls.py](./static/images/testing/pep8-menu-urls.PNG)

menu/views.py

![Pep8 validation for menu views.py](./static/images/testing/pep8-menu-views.PNG)

user/admin.py

![Pep8 validation for user admin.py](./static/images/testing/pep8-user-admin.PNG)

user/apps.py

![Pep8 validation for user apps.py](./static/images/testing/pep8-user-apps.PNG)

user/models.py

![Pep8 validation for user models.py](./static/images/testing/pep8-user-models.PNG)

user/tests.py

![Pep8 validation for user tests.py](./static/images/testing/pep8-user-tests.PNG)

user/urls.py

![Pep8 validation for user urls.py](./static/images/testing/pep8-user-urls.PNG)

user/views.py

![Pep8 validation for user views.py](./static/images/testing/pep8-user-views.PNG)

## Lighthouse testing

I used [Chrome lighthouse](https://developer.chrome.com/docs/lighthouse/overview) to lighthouse my project. Initially I had some problems with security of cloudinary sending http instead of https and duplicate id's from the signup page. After fixing these issues I had very high scores all across the board, near perfect. Only area where I really lost points was lack of contrast ratio between the foreground content of my page and the background. I left this as is as I dont want to disrupt the styling of the page by adding extra font weight, this would change the look and feel of the page quite a lot and take attention away from where we want the users to actually be looking.

Home page  - Passed

![Home page](./static/images/testing/lighthouse-home.PNG)

Signup page - Passed

![Signup page lighthouse scores](./static/images/testing/lighthouse-signup.PNG)

Booking page - Passed

![Booking page lighthouse scores](./static/images/testing/lighthouse-booking.PNG)

Main menu page - Passed

![Main menu page lighthouse scores](./static/images/testing/lighthouse-menu.PNG)

Lunch page - Passed

![Lunch page lighthouse scores](./static/images/testing/lighthouse-lunch-menu.PNG)

Dinner page - Passed

![Dinner page lighthouse scores](./static/images/testing/lighthouse-dinner-menu.PNG)

My profile - Passed

![My profile page lighthouse scores](./static/images/testing/lighthouse-my-profile.PNG)

Signout page - Passed

![Signout page lighthouse scores](./static/images/testing/lighthouse-signout.PNG)

403 page - Did not check, main 404 error page was checked however I left the other error pages out. Attempting to check these was taking way too much time which would take me out of the scope of this project and django security made it very hard to invoke these error pages.

404 page - Passed

![404 page lighthouse scores](./static/images/testing/lighthouse-404.PNG) 

405 page - Did not check, main 404 error page was checked however I left the other error pages out. Attempting to check these was taking way too much time which would take me out of the scope of this project and django security made it very hard to invoke these error pages.

500 page -  Did not check, main 404 error page was checked however I left the other error pages out. Attempting to check these was taking way too much time which would take me out of the scope of this project and django security made it very hard to invoke these error pages.

## Manual testing

### Responsiveness

For my responsiveness testing I used the app [Responsively app](https://responsively.app/)

Initially I had a problem with the my profile page on mobile but that was an easy fix and no further problems

|Screen Size|Device Type|Viewport Width|Pass/Fail|
|-----------|-----------|--------------|---------|
|Mobile|Smartphone|375px||
|Tablet|Tablet |768px||
|Laptop|Small Laptop/Desktop|1024px||

### Browser testing
|Browser|Not Functioning|Partial Functioning|Full Functioning|
|-------|---------------|-------------------|----------------|
|<i class="fab fa-chrome"></i>Google Chrome| | ||
|<i class="fab fa-firefox-browser"></i>Mozilla Firefox| | ||
|<i class="fab fa-edge"></i>Microsoft Edge| | ||
|<i class="fab fa-opera"></i>Opera| | ||

### Website testing

Header & Navbar
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail/Potential improvements |
|---------|-------------------|-------------------|--------|-----------|
|Navigation links|On initial open of the page the navbar is immediately visible to the user|Open webpage on incognito|||
|Navbar|The navbar is visible regardless of which page and where you are on these pages|Load different pages and scroll down|||
|Company logo|The company logo stands out|Visual check|||
|Company logo|The logo leads to the homepage on click|Clicked the logo on a page other than home|||
|Nav links|There is a home link which leads to the home page on click|Home button clicked from another page|||
|Nav links|There is a menu link which leads to the main menu page|Click the menu link from another page|||
|Nav links|There is a Make a Booking CTA that leads to the Booking page on click from another page IF the user is logged in|Click the Make a Booking CTA|||
|Nav links|There is a Make a Booking CTA that doesn't link to the Booking page if the user is not logged in|Make sure we are logged out and click|||
|Nav links|If the user is not logged in and clicks the make a booking they get a feedback error message that they must first login|Make sure we are not logged in and click the Booking CTA|||
|Nav links|The Booking CTA stands out and is eyecatching|Visual check of the Booking CTA and check it is underlined to make it stand out from the other buttons|||
|Nav links|The CTA underline transition disappears on hover|Hover mouse over Booking CTA|||
|Nav links|The Booking CTA gets transitions an underline again after mouse exits hover|Hover over Booking CTA and then remove the mouse from hovering|||
|Nav links|On smaller devices the navigation collapses into an expandable navigation|Window resize|||
|Hamburger icon|On click the navigation items display|Click icon|||
|Hamburger icon|If opened, on click the navigation items disappear|Click the icon after opening|||
|Login and Logout button|There is a login button on the right of the nav|Visual check|||
|Login and Logout button|The login button is underlined to stand out|Visual check|||
|Login and Logout button|The login button underline transition removes on hover|Hover mouse over|||
|Login and Logout button|The login button underline transitions back on mouse exit after hover||||
|Login and Logout button|On click of the login button the login modal is opened|Click button|||
|Login and Logout button|On login of the user the login button changes to a logout button|Login and see if the button changes|||
|Login and Logout button|On logout of the user the logout button changes back to the login button|Logout and check|||
|Login and Logout button|The logout button has an underline to attract attention|Visual check|||
|Login and Logout button|The logout button on hover transition removes the underline|Hover mouse over|||
|Login and Logout button|The logout button on mouse exit after hover regains the underline|Hover mouse over then mouse exit|||
|Login and logout button|One link or the other is always present even on smaller devices|Visual check|||
|Regular nav links|Have no underline |Visual check|||
|Regular nav links|Transition underline on hover|Hover mouse over|||
|Regular nav links|Transition remove underline on mouse exit|Hover mouse over then mouse exit|||
|My profile icon|On login the my profile icon is found on the left of the navbar|Visual check|||
|My profile icon|If not logged in the my profile icon is not present|Log out and check if the my profile icon is present|||
|My profile icon|If logged in clicking the my profile icon leads the user to the my profile page|Login and click the my profile icon|||
|My profile icon|If logged in the icon is always present even on smaller devices|Visual check|||
|Button, anchor links, logo and my profile icon|On hover over any of these links the mouse become a pointer|Hover over links, buttons and icon|||
|Responsive|The navbar looks good and functions on many screen sizes|Window resize|||
|Spelling check|There are no spelling errors in any of the links or the company logo within the nav|Read through links and company logo|||
|Active|If a user is on a page an active class is added and the text or icon changes thickness or color|Go to pages and check icon or link|||

Footer
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail/Potential improvements |
|---------|-------------------|-------------------|--------|-----------|
|Responsive|Information displays well on multiple devices|Window resize|||
|Social media links |Each link opens the right page|Click links|||
|Social media links|Each links open the page on a new tab|Click links|||
|Footer availability|Footer is displayed on every page|Check the bottom of each page|||

Home page
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail/Potential improvements |
|---------|-------------------|-------------------|--------|-----------|
|Hero img responsiveness|The hero image looks good on multiple screen sizes|Window resize|||
|Images alt|Images contain alt tags|Check alt tags in console|||
|Navigation cards|Cards are responsive and display well on multiple screen sizes|Window resize|||
|Navigation cards links|On click of the navigation cards these link to the correct website page|Click navigation cards|||
|Review Navigation card |Opens googleon another tab|Click review navigation card|||
|Navigation cards(Menu and booking)|Redirect the current page|Click navigation cards|||

My profile page
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail/Potential improvements |
|---------|-------------------|-------------------|--------|-----------|
|Profile icon|Users who are not logged in cannot see this icon leading to the my profile page|Log out and check nav|||
|Profile icon|Users who are logged in can see the my profile icon|Login and check nav|||
|My profile page|My profile page opens on click of profile icon|Click profile icon|||
|My Bookings|Any bookings I previously made and have not deleted are displayed|Check bookings|||
|My bookings|Any bookings I will make will display in my bookings|Make a booking and check my bookings|||
|My bookings|Any bookings I make will immediately reflect in my bookings|Open 1 tab of my profile, open 1 tab and make a booking, then refresh the my profile tab |||
|My bookings data|Each booking displays the booking date, time, guests and comments|Check each booking|||
|My bookings data|Bookings are displayed in order of farthest in the future first and farthest in the past last|Check booking dates order|||
|Booking edit|Each booking has an edit icon present|Check bookings|||
|Booking edit|Each booking edit icon can be clicked to redirect to edit booking page|Click edit icon|||
|Edit booking page|After redirection to edit page, information that was present on the booking is pre-filled on the edit form|Click edit icon, check inputs|||
|Edit booking page|After editing a booking and submitting the data is immediately reflected in the booking in the my bookings|Edit a booking then check my bookings|||
|Edit booking message|After editing a booking and submitting a success message is displayed|Edit a form and submit then Check if message displays|||
|Edit booking redirect|After editing a booking and submitting user is redirected to the home page|Edit a booking and submit|||
|Edit booking|On click of a booking on the day or before the user is not directed to the edit page|Click edit on a booking in the past or current day|||
|Edit booking|On click of a booking on the day or before the user is displayed an error message|Click edit on a booking in the past or current day|||
|Delete booking Icon|On each booking item a delete booking icon is present|Check bookings|||
|Delete booking|On click of the delete booking icon a confirmation modal opens|Click delete icon|||
|Delete booking confirmation modal|On click of close the modal closes|Click Close|||
|Delete booking confirmation modal|On click of x the modal closes|Click x|||
|Delete booking confirmation modal|On click of Delete the modal closes|Click delete|||
|Delete booking confirmation modal|On click of Delete the booking is deleted|Click delete|||
|Delete booking confirmation modal|On click outside of the modal the modal closes|Click outside of modal|||
|Delete booking confirmation modal|On click of delete and open of modal background greys out|Click delete icon|||
|Delete booking modal|If a user attempts to delete a booking from the past or on the same day as the booking the page just refreshes and does delete the modal|Click the delete button|||
|Delete booking modal|If a user attempts to delete a booking from the past or on the same day as the booking an error message is displayed|Click the delete button|||
|Pagination|If there is more than 5 bookings pagination activates and displays 2 pages at the bottom|Create more than 5 bookings and check my profile page|||
|Pagination|If there is more than 5 bookings pagination activates and displays a next page if there is a next page|Check if next page is present|||
|Pagination|If there is more than 5 bookings pagination activates, on click of next page the user is redirected to the next page|Click next page|||
|Pagination|If there is more than 5 bookings pagination activates, on click of previous page the user is redirected to the previous page|Click previous page|||
|Pagination|If there is more than 1 page pagination displays a counter of pages and shows which page you are on|Check bottom of page|||

Menu page
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail/Potential improvements |
|---------|-------------------|-------------------|--------|-----------|
|Meal cards|Meal cards are displayed|Visual check|||
|Meal cards|When clicking anywhere on the card, navigate to their respective page|Click cards|||
|Meal cards responsiveness|Each card remains the same size on multiple screen sizes|Screen resize|||
|Add menu icon|Clicking the add menu icon navigates the user to the add menu item form|Click the + icon|||
|Add menu icon|Admins can see an add menu icon|Login to an admin account and check|||
|Add menu icon|Regular users cannot see an add menu icon|Login to a normal user account and check|||

Add item page 
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail/Potential improvements |
|---------|-------------------|-------------------|--------|-----------|
|Add menu item|All form fields are required|Test form fields|||
|Add menu item|All form fields have a label|Visual check|||
|Add menu item|Images post to cloudinary and reflect on the item|Add an image and check added item|||
|Add menu item|A meal category must be selected or the form cant submit|Dont select meal category and submit|||
|Add menu item|If an item is added without an image being added the default image is added instead|Check image is added|||
|Add menu item|If a user submits a valid form that data populates the database|Check if item is reflected in lunch or menu page|||
|Title input|Any characters can be placed into the title|Type different characters and numbers etc|||
|Description input|Any characters can be placed into the description|Type different characters and numbers etc|||
|Image input|Users can select a file to be passed in|Add image|||
|Price input|Users can only add numbers|Type characters and numbers|||
|Price input|Users cannot add more than 4 digits before the decimal point|Type numbers|||
|Price input|Users cannot add more than 2 decimal digits|Type decimal digits|||
|Price input|Users cannot add more than 4 digits before the decimal point and 2 decimal digits at the same time|Add digits before and after the decimal point|||
|Mead category|Users can only select Lunch or Dinner|Attempt to type|||
|Unique title|Users cannot add a title which is already in use|Add a title which is already used|||
|Submit button|If the form is filled out correctly on submission of the form the user is redirect back to the menu page|Fill out form and submit|||
|Submit button|If the form is not filled out correctly on submission of the for the user is not redirected to another page|Dont fill out form and submit|||

Lunch Menu page
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail/Potential improvements |
|---------|-------------------|-------------------|--------|-----------|
|Lunch menu items|Items on the page or only data-meal_category = lunch|Check if items are data-meal_category = lunch|||
|Lunch menu items|All data displays properly|Check image, title, description, price|||
|Lunch menu item image|If an image is not selected the default img appears instead|Check image|||
|Menu item card responsiveness|Displays well on across screen sizes|Window resize|||
|Menu item card responsiveness|Items are 2 per row on medium |Check items|||
|Menu item card responsiveness|Items are 1 per row on small devices|Check items|||
|Nav and footer|Nav and footer render correctly||||
|Edit icon|Displays for admins|Visual check|||
|Edit icon|Does not display for normal users|Visual check|||
|Edit icon|On click of the edit icon the user is redirected to the edit form page|Click the edit icon|||
|Delete icon|Displays for admins|Visual check|||
|Delete icon|Does not display for regular users|Visual check|||
|Delete item confirmation modal|On click of the delete icon the delete confirmation modal appears |Click delete icon|||
|Delete item confirmation modal|On click of delete in the modal the item is deleted|Click the button and check|||
|Delete item confirmation modal|On click of delete in the modal the user stays on the dinner page|Click the button and check|||
Image alt|Alt attribute is added automatically and is equal to the description||||

Dinner menu page
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail/Potential improvements |
|---------|-------------------|-------------------|--------|-----------|
|Dinner menu items|Items on the page or only data-meal_category = Dinner|Check if items are data-meal_category = Dinner|||
|Dinner menu items|All data displays properly|Check image, title, description, price|||
|Dinner menu item image|If an image is not selected the default img appears instead|Check image|||
|Menu item card responsiveness|Displays well on across screen sizes|Window resize|||
|Menu item card responsiveness|Items are 2 per row on medium |Check items|||
|Menu item card responsiveness|Items are 1 per row on small devices|Check items|||
|Nav and footer|Nav and footer render correctly||||
|Edit icon|Displays for admins|Visual check|||
|Edit icon|Does not display for normal users|Visual check|||
|Edit icon|On click of the edit icon the user is redirected to the edit form page|Click the edit icon|||
|Delete icon|Displays for admins|Visual check|||
|Delete icon|Does not display for regular users|Visual check|||
|Delete item confirmation modal|On click of the delete icon the delete confirmation modal appears |Click delete icon|||
|Delete item confirmation modal|On click of delete in the modal the item is deleted|Click the button and check|||
|Delete item confirmation modal|On click of delete in the modal the user stays on the dinner page|Click the button and check|||
|Image alt|Alt attribute is added automatically and is equal to the description||||

Login modal
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail/Potential improvements |
|---------|-------------------|-------------------|--------|-----------|
|Login link|On click it opens the login modal|Click link|||
|Login modal|Username and password inputs are present|Visual check|||
|Login modal|Image loads normally on left side |Visual check|||
|Login modal |If user fills out form incorrectly the page does not refresh|Fill out incorrectly and press login|||
|Login modal|If username is not filled out an HTML validation warning appears|Dont fill in and submit|||
|Login modal|If password is not filled out an HTML validation warning appears|Dont fill in and submit|||
|Signup link|There is a signup link present which stands out |Visual check|||
|Login modal error handling|Errors are not present on open of the modal|Open modal|||
|Login modal error handling|If form is filled out incorrectly errors display||||
|Signup link|Link opens the signup page |Click link|||

Signup page
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail/Potential improvements |
|---------|-------------------|-------------------|--------|-----------|
|Signup form|Signup form displays with username, email, password, confirm password inputs||||
||||| 
|Signup form error handling|Username required HTML validation works|Submit without filling in username|||
|Signup form error handling|Email required HTML validation works|Submit without filling in Email|||
|Signup form error handling|Email HTML validation works|Submit without Adding an @ sign|||
|Signup form error handling|Password required HTML validation works|Submit without filling in Password|||
|Signup form error handling|Password(again) required HTML validation works|Submit without filling in Password(again)|||
|Signup form error handling|If password and password(again) are different the form does not submit|Add different passwords and submit|||
|Signup form error handling|If password and password(again) are the same the form submits|Add the same passwords and submit|||
|Signup submit|If the form is filled out correctly the form is submitted|Fill out correctly and submit|||
|Signup submit|If the form is filled out incorrectly the form is not submitted|Fill out incorrectly and submit|||
|Form submission|If the form is filled out correctly and submitted, the user is automatically logged in and directed to the home page|Fill out the form and submit|||


Logout page
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail/Potential improvements |
|---------|-------------------|-------------------|--------|-----------|
|Nav link|Logout nav link gets the active class and becomes bold|Go to logout page and check|||
|Sign out message|Sign out confirmation displays on the logout page|Go to logout page and visually check|||
|Sign out button|Sign out button displays on the logout page|Go to the logout page and visually check|||
|Sign out button|On click of the sign out button the user is signed out and directed to the home page||||
|Sign out message|On user sign out the user is given a feedback message|Sign out and check if a message appears|||

403 page
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail/Potential improvements |
|---------|-------------------|-------------------|--------|-----------|
|403 page|Nav and footer appears in the page|Invoke a 403 page error, check page|||
|403 page|403 error displays|Invoke a 403 page error, check page|||
|Home button|Home button appears in the page|Invoke a 403 page error, check page|||
|Home button redirection|On click the button redirects the user to the home page|Invoke a 403 page error, click the home button|||

404 page
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail/Potential improvements |
|---------|-------------------|-------------------|--------|-----------|
|404 page|Nav and footer appears in the page|Invoke a 404 page error, check page|||
|404 page|404 error displays|Invoke a 404 page error, check page|||
|Home button|Home button appears in the page|Invoke a 404 page error, check page|||
|Home button redirection|On click the button redirects the user to the home page|Invoke a 404 page error, click the home button|||

405 page
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail/Potential improvements |
|---------|-------------------|-------------------|--------|-----------|
|405 page|Nav and footer appears in the page|Invoke a 405 page error, check page|||
|405 page|405 error displays|Invoke a 405 page error, check page|||
|Home button|Home button appears in the page|Invoke a 405 page error, check page|||
|Home button redirection|On click the button redirects the user to the home page|Invoke a 405 page error, click the home button|||


500 page
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail/Potential improvements |
|---------|-------------------|-------------------|--------|-----------|
|500 page|Nav and footer appears in the page|Invoke a 500 page error, check page|||
|500 page|500 error displays|Invoke a 500 page error, check page|||
|Home button|Home button appears in the page|Invoke a 500 page error, check page|||
|Home button redirection|On click the button redirects the user to the home page|Invoke a 500 page error, click the home button|||
