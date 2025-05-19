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
function deleteMenuItem(e) {
    // console.log(e)
    let itemId = e.target.getAttribute("data-id")
    deleteConfirm.href = `delete_booking/${itemId}`;
    deleteModal.show();
}
// NAKED CODE which doesn't fit into other categories

