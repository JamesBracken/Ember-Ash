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
function editMenuItem(e) {
    let parent = e.editMenuItem.target.closest("menu-item-buttons-container")
    let menuItemId = parent.dataset.id
    let itemTitle = parent.dataset.title
    let itemDescription = parent.dataset.description
    let itemImg = parent.dataset.img
    let itemPrice = parent.dataset.price
    let itemMealCategory = parent.dataset.meal_category
    itemTitleInput.value = itemTitle
    itemDescriptionInput.value = itemDescription
    itemImgInput.value = itemImg
    itemPriceInput.value = itemPrice
    itemMealCategoryInput.value = itemMealCategory

    let action = addMenuItemForm.setAttribute("action", `edit_menu_item/${menuItemId}`)
}

function deleteMenuItem(e) {

}
// NAKED CODE which doesn't fit into other categories

