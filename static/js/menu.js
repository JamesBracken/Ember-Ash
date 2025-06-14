// GLOBAL VARIABLES
// CONSTANTS
const deleteButtons = document.getElementsByClassName("menu-delete-item-button");
const deleteConfirm = document.getElementById("deleteConfirm");

// EVENT LISTENERS
for (let button of deleteButtons) {
    button.addEventListener("click", deleteMenuItem);
}

// FUNCTIONS
/* This function opens the delete confirmation modal, it takes the
id of the selected menu item and it updates the href for the delete_menu_item
 view to delete the correct data. 

*@param {Click} e - This is information of the event that triggers the
 function, using this we get the data-booking_id attribute to delete the 
 selected modal 

*/
function deleteMenuItem(e) {
    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    let itemId = e.target.getAttribute("data-id");
    deleteConfirm.href = `delete_booking/${itemId}`;
    deleteModal.show();
}