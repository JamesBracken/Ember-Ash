# Testing

## Difficult to solve bugs

When implementing my login modal I experienced problems with my modal. It was appearing behind the modal backdrop. In the documentation Bootstrap stipulates modals tend to act differently when placed into fixed components hence the issues.
![alt text](./static/images/testing/modal_z_index.PNG)

I fixed this problem by taking the modal code out of the header and placing it at the bottom of the body. I also set a z-index for both the modal and modal backdrop as an extra defensive measure.
![alt text](./static/images/testing/modal_z_index_solved.PNG)


## Validators

### Lighthouse
[]()
[]()
[]()
[]()
[]()
[]()
[]()
[]()
[]()
[]()
### HTML validator
[]()
[]()
[]()
[]()

### CSS validator
[]()
[]()
[]()
[]()
[]()
[]()
[]()
[]()
### ESLint validator
[]()
[]()
[]()
[]()
[]()
[]()
[]()
### WAVE(Optional)
###
###




## Manual testing

Responsiveness
|Screen Size|Device Type|Viewport Width|Pass/Fail|
|-----------|-----------|--------------|---------|
|Mobile|Smartphone|375px||
|Tablet|Tablet |768px||
|Laptop|Small Laptop/Desktop|1024px||

Browser testing
|Browser|Not Functioning|Partial Functioning|Full Functioning|
|-------|---------------|-------------------|----------------|
|<i class="fab fa-chrome"></i>Google Chrome| | ||
|<i class="fab fa-firefox-browser"></i>Mozilla Firefox| | ||
|<i class="fab fa-edge"></i>Microsoft Edge| | ||
|<i class="fab fa-opera"></i>Opera| | ||

Header & Navbar
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
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
|Regular nav links|Have no underline |Visual check|||
|Regular nav links|Transition underline on hover|Hover mouse over|||
|Regular nav links|Transition remove underline on mouse exit|Hover mouse over then mouse exit|||
|My profile icon|On login the my profile icon is found on the left of the navbar||||
|My profile icon|If not logged in the my profile icon is not present|Log out and check if the my profile icon is present|||
|My profile icon|If logged in clicking the my profile icon leads the user to the my profile page|Login and click the my profile icon|||
|Button, anchor links, logo and my profile icon|On hover over any of these links the mouse become a pointer|Hover over links, buttons and icon|||
|Responsive|The navbar looks good and functions on many screen sizes|Window resize||||||||
|Spelling check|There are no spelling errors in any of the links or the company logo within the nav|Read through links and company logo|||


Footer
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|---------|-------------------|-------------------|--------|-----------|
|Responsive|Information displays well on multiple devices|Window resize|||
|Social media links |Each link opens the right page|Click links|||
|Social media links|Each links open the page on a new tab|Click links|||
|Footer availability|Footer is displayed on every page|Check the bottom of each page|||

Home page
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|---------|-------------------|-------------------|--------|-----------|
|Hero img responsiveness|The hero image looks good on multiple screen sizes|Window resize|||
|Images alt|Images contain alt tags|Check alt tags in console|||
|Navigation cards|Cards are responsive and display well on multiple screen sizes|Window resize|||
|Navigation cards links|On click of the navigation cards these link to the correct website page|Click navigation cards|||
|Review Navigation card |Opens googleon another tab|Click review navigation card|||
|Navigation cards(Menu and booking)|Redirect the current page|Click navigation cards|||

My profile page
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
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
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|---------|-------------------|-------------------|--------|-----------|
|Meal cards|Meal cards are displayed|Visual check|||
|Meal cards|When clicking anywhere on the card, navigate to their respective page|Click cards|||
|Meal cards responsiveness|Each card remains the same size on multiple screen sizes|Screen resize|||
|Add menu icon|Clicking the add menu icon navigates the user to the add menu item form|Click the + icon|||
|Add menu icon|Admins can see an add menu icon|Login to an admin account and check|||
|Add menu icon|Regular users cannot see an add menu icon|Login to a normal user account and check|||

Add item page 
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|---------|-------------------|-------------------|--------|-----------|
||||||
Dinner menu delete item modal



Dinner menu page
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|---------|-------------------|-------------------|--------|-----------|
||||||


Login modal
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|---------|-------------------|-------------------|--------|-----------|
||||||

Signup modal
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|---------|-------------------|-------------------|--------|-----------|
||||||








Success page
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|---------|-------------------|-------------------|--------|-----------|
||||||


404 page

500 page

405 page

403 page