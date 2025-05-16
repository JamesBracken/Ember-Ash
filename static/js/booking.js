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
function deleteBooking(e) {
    let parent = e.target.closest(".booking-buttons-container")
    let bookingId = parent.getAttribute("data-booking_id")
    deleteConfirm.href = `/booking/delete_booking/${bookingId}`;
    deleteModal.show();
}
// NAKED CODE which doesn't fit into other categories
