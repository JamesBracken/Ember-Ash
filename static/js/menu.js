// GLOBAL VARIABLES

// CONSTANTS
// Add & edit item page and link to page
const addButton = document.getElementById("add-menu-item-button")
const addMenuItemForm = document.getElementById("add-menu-item-form")
const submitMenuItem = document.getElementById("add-menu-item-submit")
const editButtons = document.getElementsByClassName("menu-edit-item-button")
 
//  Add inputs
const itemTitleInput = document.getElementById("id_title")
const itemDescriptionInput = document.getElementById("id_description")
const itemImgInput = document.getElementById("id_img")
const itemPriceInput = document.getElementById("id_price")
const itemMealCategoryInput = document.getElementById("id_meal_category")


const deleteButtons = document.getElementsByClassName("menu-delete-item-button")
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"))
const deleteConfirm = document.getElementById("deleteConfirm")
// LET AND VAR VARIABLES

// EVENT LISTENERS
for (let button of editButtons) {
    button.addEventListener("click", editMenuItem)
}

for (let button of deleteButtons) {
    button.addEventListener("click", deleteMenuItem)
}

// FUNCTIONS

// NAKED CODE which doesn't fit into other categories

