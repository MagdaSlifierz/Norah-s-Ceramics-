// Control active class in the navbar

function controlActiveClass() {
  let currentLocation = window.location.href;
  let menuItems = document.querySelectorAll("#menu-list li a");
  let menuLength = menuItems.length;

  for (let i = 0; i < menuLength; i++) {
    if (menuItems[i].href === currentLocation) {
      menuItems[i].classList.add("active");
      console.log(currentLocation);
    } else {
      menuItems[i].classList.remove("active");
    }
  }
}

controlActiveClass();

// Code from https://codepen.io/JoseRosario/pen/BWqMwK*
function toggleHamburgerIcon() {
  let wrapperMenu = document.querySelector(".wrapper-menu");

  wrapperMenu.addEventListener("click", function () {
    wrapperMenu.classList.toggle("open");
  });
}

toggleHamburgerIcon();

/* My code starts here
        Open and close sidebar for small devices*/
const hamburgerIcon = document.querySelector(".wrapper-menu");
const closeButtons = document.querySelectorAll(".close-sidebar");

function openMenu() {
  document.getElementById("my-sidebar").classList.toggle("open-menu");
}

hamburgerIcon.addEventListener("click", function (e) {
  openMenu();
});

// show/hide password
function showPassword(elemendId) {
  let passwordInput = document.getElementById(elemendId);
  if (passwordInput.type === "password") {
    passwordInput.type = "text";
  } else {
    passwordInput.type = "password";
  }
}

const box_one = document.getElementById("show_password_one");
if (box_one) {
  box_one.addEventListener("click", function () {
    showPassword("id_password1");
  });
}

const box_two = document.getElementById("show_password_two");
if (box_two) {
  box_two.addEventListener("click", function () {
    showPassword("id_password2");
  });
}

const box_three = document.getElementById("show_password_login");
if (box_three) {
  box_three.addEventListener("click", function () {
    showPassword("id_password");
  });
}

/* After pressing sidebar links and scrolling to a given section,
      the sidebar closes automatically*/
for (const button of closeButtons) {
  let wrapperMenu = document.querySelector(".wrapper-menu");
  button.addEventListener("click", function (e) {
    if (window.innerWidth < 1150) {
      wrapperMenu.classList.toggle("open");
      openMenu();
    }
  });
}

// Scroll to top after click 'back to top button'
const backToTopButton = document.querySelector("#back-to-top-button");

window.addEventListener("scroll", (e) => {
  // Get the current scroll value
  let currentPosition = window.scrollY;

  if (currentPosition > 200) {
    backToTopButton.className = "go-up-btn show-btn";
  } else {
    backToTopButton.className = "go-up-btn hide-btn";
  }
});

/* The function moves the page up with animate scrolling
 with using window.requestAnimationFrame() */
const backToTop = () => {
  // Set a variable for the number of pixels we are from the top of the document
  const pxNumber =
    document.documentElement.scrollTop || document.body.scrollTop;

  if (pxNumber > 0) {
    window.requestAnimationFrame(backToTop);
    window.scrollTo(0, pxNumber - pxNumber / 20);
  }
};

// Add onclick event listener to 'back to top button'
backToTopButton.onclick = function (e) {
  e.preventDefault();
  backToTop();
};

// show sub menu
const ceramicsBtn = document.querySelector("#ceramics");
const glassBtn = document.querySelector("#glass");
const zeroWasteBtn = document.querySelector("#zero-waste");
const profile = document.querySelector("#profile");
const ceramicsContent = document.querySelectorAll(".ceramics-content");
const glassContent = document.querySelectorAll(".glass-content");
const zeroWasteContent = document.querySelectorAll(".zero-waste-content");
const profileContent = document.querySelectorAll(".profile-content");
let showDropdown = false;

if (ceramicsBtn) {
  ceramicsBtn.addEventListener("click", toggleCeramics);
}

if (glassBtn) {
  glassBtn.addEventListener("click", toggleGlass);
}

if (zeroWasteBtn) {
  zeroWasteBtn.addEventListener("click", toggleWaste);
}

if (profile) {
  profile.addEventListener("click", toggleProfile);
}

function toggleCeramics() {
  if (!showDropdown) {
    ceramicsContent.forEach((item) => item.classList.add("show-sub-menu"));
    showDropdown = true;
  } else {
    ceramicsContent.forEach((item) => item.classList.remove("show-sub-menu"));
    showDropdown = false;
  }
}

function toggleGlass() {
  if (!showDropdown) {
    glassContent.forEach((item) => item.classList.add("show-sub-menu"));
    showDropdown = true;
  } else {
    glassContent.forEach((item) => item.classList.remove("show-sub-menu"));
    showDropdown = false;
  }
}

function toggleWaste() {
  if (!showDropdown) {
    zeroWasteContent.forEach((item) => item.classList.add("show-sub-menu"));
    showDropdown = true;
  } else {
    zeroWasteContent.forEach((item) => item.classList.remove("show-sub-menu"));
    showDropdown = false;
  }
}

function toggleProfile() {
  if (!showDropdown) {
    profileContent.forEach((item) => item.classList.add("show-sub-menu"));
    showDropdown = true;
  } else {
    profileContent.forEach((item) => item.classList.remove("show-sub-menu"));
    showDropdown = false;
  }
}
