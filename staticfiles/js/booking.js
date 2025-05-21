// GLOBAL VARIABLES

// CONSTANTS
// Booking delete variables
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("delete-btn");
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of deleteButtons) {
    button.addEventListener("click", deleteBooking)
}

// FUNCTIONS
/* This function deletes the selected booking, using the event handler it takes the
id of the selected booking and deletes the data connected with the id.
Before deletion a confirmation modal
is displayed for the user to confirm booking deletion and warns the user this 
cannot be undone

*@param {Click} e - This is information of the event that triggers the
 function, using this we get the data-booking_id attribute to delete the 
 selected modal 

*/
function deleteBooking(e) {
    let parent = e.target.closest(".booking-buttons-container")
    let bookingId = parent.getAttribute("data-booking_id")
    deleteConfirm.href = `/booking/delete_booking/${bookingId}`;
    deleteModal.show();
}
