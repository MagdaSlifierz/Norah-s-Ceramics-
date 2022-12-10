// https://www.howtocodeschool.com/2021/12/price-range-slider-with-html-css-javascript.html

const one = document.getElementById("id_stars_0");
const two = document.getElementById("id_stars_1");
const three = document.getElementById("id_stars_2");
const four = document.getElementById("id_stars_3");
const five = document.getElementById("id_stars_4");
const stars = document.querySelector("#id_stars");

// Change stars color on click
const handleStarSelect = (size) => {
  const children = stars.children;

  for (let i = 0; i < children.length; i++) {
    if (i <= size) {
      children[i].classList.add("checked");
    } else {
      children[i].classList.remove("checked");
    }
  }
};

// Handle qty of selected stars
const handleSelect = (selection) => {
  switch (selection) {
    case "id_stars_0": {
      handleStarSelect(0);
      return;
    }
    case "id_stars_1": {
      handleStarSelect(1);
      return;
    }
    case "id_stars_2": {
      handleStarSelect(2);
      return;
    }
    case "id_stars_3": {
      handleStarSelect(3);
      return;
    }
    case "id_stars_4": {
      handleStarSelect(4);
      return;
    }
  }
};

const arr = [one, two, three, four, five];

arr.forEach((item) => {
  if (item) {
    item.addEventListener("click", (event) => {
      handleSelect(event.target.id);
    });
  }
});

const openModalButton = document.querySelector("#open-modal");
const closeModal = document.querySelector(".popup__close");

// / Function opens modal
function openModal() {
  let showDeleteModal = document.querySelector(".popup");
  showDeleteModal.classList.toggle("show-modal");
}

if (openModalButton) {
  openModalButton.addEventListener("click", openModal);
  closeModal.addEventListener("click", openModal);
}
// ================================================================
const openModalBtn = document.querySelector("#see-rev");
const closeModalBtn = document.querySelector(".popup__close_btn");

// / Function opens reviews modal
function openRevModal() {
  let showDeleteModal = document.querySelector(".rev-popup");
  showDeleteModal.classList.toggle("show-rev-modal");
}

if (openModalBtn) {
  openModalBtn.addEventListener("click", openRevModal);
  closeModalBtn.addEventListener("click", openRevModal);
}
