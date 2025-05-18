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
||||||


Menu page
| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
|---------|-------------------|-------------------|--------|-----------|
||||||

Lunch Menu page 
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

