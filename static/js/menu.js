// GLOBAL VARIABLES
// CONSTANTS
const deleteButtons = document.getElementsByClassName("menu-delete-item-button")
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"))
const deleteConfirm = document.getElementById("deleteConfirm")
// LET AND VAR VARIABLES

// EVENT LISTENERS
for (let button of deleteButtons) {
    button.addEventListener("click", deleteMenuItem)
}

// FUNCTIONS
/* This function deletes the selected menu item, using the event handler, it takes the
id of the selected booking and deletes the data connected with this id. 
Before deletion a confirmation modal
is displayed for the user to confirm menu item deletion and warns the user this 
cannot be undone

*@param {Click} e - This is information of the event that triggers the
 function, using this we get the data-booking_id attribute to delete the 
 selected modal 

*/
function deleteMenuItem(e) {
    // console.log(e)
    let itemId = e.target.getAttribute("data-id")
    deleteConfirm.href = `delete_booking/${itemId}`;
    deleteModal.show();
}
// NAKED CODE which doesn't fit into other categories

