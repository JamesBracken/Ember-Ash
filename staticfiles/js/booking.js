// GLOBAL VARIABLES

// CONSTANTS

// Booking edit variables
const editButtons = document.getElementsByClassName("edit-btn")
const bookingForm = document.getElementById("bookingForm")
const updateBookingBtn = document.getElementById("updateBookingBtn")
// Inputs injected into my_profile template from booking forms.py
const bookingDateInput = document.getElementById("id_booking_date")
const bookingTimeInput = document.getElementById("id_booking_time")
const bookingGuestsInput = document.getElementById("id_guests_qty")
const bookingCommentInput = document.getElementById("id_comment")

// Booking delete variables
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("delete-btn");
const deleteConfirm = document.getElementById("deleteConfirm");

// LET AND VAR VARIABLES

// EVENT LISTENERS
for (let button of editButtons) {
    button.addEventListener("click", fillBookingData)
}

for (let button of deleteButtons) {
    button.addEventListener("click", deleteBooking)
}

// FUNCTIONS

// Injects data from a booking which is selected into the form at the top of the page
// Makes the form at the top of the page appear when invoked
// When the form is submitted the edit form is again hidden
function fillBookingData(e){
    let parent = e.target.closest(".booking-buttons-container")
    let bookingId = parent.dataset.booking_id;
    let bookingSlug = parent.dataset.booking_slug;
    let bookingDateContent = parent.dataset.booking_date;
    let bookingTimeContent = parent.dataset.booking_time;
    let bookingGuestsContent = parent.dataset.guests_qty;
    let bookingCommentContent = parent.dataset.comment;
    bookingDateInput.value = bookingDateContent
    bookingTimeInput.value = bookingTimeContent
    bookingGuestsInput.value = bookingGuestsContent
    bookingCommentInput.value = bookingCommentContent

    let action = bookingForm.setAttribute("action", `edit_booking/${bookingSlug}`)
}

function deleteBooking(e) {
    let parent = e.target.closest(".booking-buttons-container")
    // let bookingId = parent.dataset.booking_id;
    let bookingSlug = parent.dataset.booking_slug
    deleteConfirm.href = `delete_booking/${bookingSlug}`;
    deleteModal.show();
}
// NAKED CODE which doesn't fit into other categories

