// Array of city names
var cities = ["Pune", "Moradabad", "Dehradun", "Rampur", "Delhi", "Coimbatore"];

// Preloader JS styling
window.addEventListener('DOMContentLoaded', () => {
    // Hide the loader after 3 seconds
    setTimeout(() => {
        const loader = document.getElementById('video-loader');
        loader.style.display = 'none';

        displayCopyright();
    }, 3000);
});

function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}

function changeCss() {
    var top = document.getElementById("top");
    var scroll_icon = document.getElementById("scroll_icon");
    this.scrollY > 30 ? top.style.opacity = 1 : top.style.opacity = 0;
    this.scrollY > 0 ? scroll_icon.style.opacity = 0 : scroll_icon.style.opacity = 1;
}

window.addEventListener("scroll", changeCss, false);

var map = L.map('map', {
    center: [23.7937, 80.9629],
    zoom: 5,
    zoomControl: false
});

// Add OpenStreetMap tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

var redIcon = L.icon({
    iconUrl: 'https://img1.picmix.com/output/stamp/normal/2/5/4/3/873452_376bb.png',
    iconSize: [25, 25],
    iconAnchor: [12, 12],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
});

// Function to get coordinates for a city and add a marker
async function addMarker(city) {
    var url = `https://nominatim.openstreetmap.org/search?format=json&q=${city}`;

    try {
        const response = await fetch(url, {
            headers: {
                'User-Agent': 'YourAppName/1.0'
            }
        });
        const data = await response.json();

        if (data.length > 0) {
            var lat = data[0].lat;
            var lon = data[0].lon;
            L.marker([lat, lon], { icon: redIcon }).addTo(map)
                .bindPopup(city);
        } else {
            console.log("No results found for " + city);
        }
    } catch (error) {
        console.error("Error fetching coordinates for " + city + ": " + error);
    }
}

// Add markers for each city
cities.forEach(city => addMarker(city));

console.log("Tejas' Codes :)");

// Element selectors
var l1 = document.getElementById("l1");
var l2 = document.getElementById("l2");
var l3 = document.getElementById("l3");
var burger = document.getElementById("burger");
var lines = document.getElementById("lines");
var cross = document.getElementById("cross");
var plane = document.getElementById("plane");
var body = document.getElementById("body");
var buttons = document.getElementById("buttons");
var examples = document.getElementById("examples");
var examples2 = document.getElementById("examples2");
var tags = document.getElementById("tags");
var contribute = document.getElementById("contribute");
var github = document.getElementById("github");
var last_link = document.getElementById("last_link");
var indicator = document.getElementById("indicator");
var shadow = document.getElementById("shadow");
var download = document.getElementById("download_btn");
const lightButton = document.getElementById("lightButton");
const darkButton = document.getElementById("darkButton");
const technologies = document.getElementById("technologies");

let lastScrollTop = 0;
const navbar = document.getElementById("navbar");

window.addEventListener('scroll', () => {
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

    if (scrollTop > lastScrollTop) {
        // Scroll down
        navbar.style.top = '-60px';
        burger.style.top = '-60px';
        lines.style.top = '-60px';
        cross.style.top = '-60px';
    } else {
        // Scroll up
        navbar.style.top = '0';
        burger.style.top = '10px';
        lines.style.top = '10px';
        cross.style.top = '10px';
    }

    lastScrollTop = scrollTop;
});

function progress() {
    var scroll = this.scrollY;
    var scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    var percent = Math.round((scroll / scrollHeight) * 100);
    document.getElementById("progress_bar").style.width = percent + 'vw';
};

window.addEventListener("scroll", progress);

function show() {
    l2.style.opacity = 0;
    l1.style.transform = "rotate(-45deg)";
    l3.style.transform = "rotate(45deg)";
    burger.style.display = "none";
    cross.style.display = "block";
    plane.style.right = 0;
    body.style.overflowY = "hidden";
    buttons.style.marginLeft = 0;
}

function hide() {
    l2.style.opacity = 1;
    l1.style.transform = "rotate(0deg)";
    l3.style.transform = "rotate(0deg)";
    burger.style.display = "block";
    cross.style.display = "none";
    plane.style.right = "-100vw";
    body.style.overflowY = "scroll";
    buttons.style.marginLeft = "-60px";
}

function updateIndicator(button) {
    const adjustment = (button.offsetHeight - indicator.offsetHeight) / 2;
    indicator.style.top = `${button.offsetTop + adjustment}px`;

    const currentTheme = localStorage.getItem('theme');
    indicator.style.backgroundImage = currentTheme === 'light'
        ? "radial-gradient(circle, rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0))"
        : "radial-gradient(circle, rgba(255, 255, 255, 0.7), rgba(0, 0, 0, 0))";
}

function light() {
    localStorage.setItem('theme', 'light');
    body.classList.remove('dark-mode');
    body.classList.add('light-mode');
    document.getElementById("map").style.filter = "none";
    document.getElementById("map").style.zIndex = 0;
    tags.style.borderColor = "black";
    tags.style.backgroundColor = "#171717";
    indicator.style.backgroundImage = "radial-gradient(rgba(0,0,0, 0.608),#00000000,#00000000)";
    shadow.style.backgroundImage = "linear-gradient(115deg, #00000000,#f9f9f9,#00000000)";
    contribute.style.filter = "invert(1)";
    technologies.style.border = "1px solid #00000044";
    updateIndicator(lightButton);
}

function dark() {
    localStorage.setItem('theme', 'dark');
    document.getElementById("map").style.filter = "invert(1) hue-rotate(180deg) brightness(1.5)";
    tags.style.borderColor = "rgba(255, 255, 255, 0.323)";
    tags.style.backgroundColor = "#00000000";
    indicator.style.backgroundImage = "radial-gradient(rgba(255,255,255, 0.608),#00000000,#00000000)";
    shadow.style.backgroundImage = "linear-gradient(115deg, #00000000,#000000d4,#00000000)";
    body.classList.remove('light-mode');
    body.classList.add('dark-mode');
    contribute.style.filter = "invert(0)";
    technologies.style.border = "1px solid #ffffff044";
    updateIndicator(darkButton);
}

function systemDefault() {
    const theme = localStorage.getItem('theme');
    if (theme === 'light') {
        light();
    } else if (theme === 'dark') {
        dark();
    } else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        dark();
    } else {
        light();
    }
    updateIndicator(document.getElementById("defaultButton"));
}

systemDefault();

document.getElementById("lightButton").addEventListener("click", () => {
    light();
    updateIndicator(document.getElementById("lightButton"));
});
document.getElementById("darkButton").addEventListener("click", () => {
    dark();
    updateIndicator(document.getElementById("darkButton"));
});
document.getElementById("defaultButton").addEventListener("click", () => {
    systemDefault();
    updateIndicator(document.getElementById("defaultButton"));
});

function animate() {
    var reveal = document.querySelectorAll(".section");

    for (var i = 1; i < reveal.length; i++) {
        var windowHeight = window.innerHeight;
        var elementTop = reveal[i].getBoundingClientRect().top;
        var e = 90;

        if (elementTop < windowHeight - e) {
            reveal[i].classList.add("big_container");
        } else {
            reveal[i].classList.remove("big_container");
        }
    }
}

window.addEventListener("scroll", animate);

function validateForm() {
    var name = document.querySelector('input[name="Name"]').value.trim();
    var email = document.querySelector('input[name="Email"]').value.trim();
    var message = document.querySelector('textarea[name="Message"]').value.trim();

    if (name === "" || email === "" || message === "") {
        alert("Please fill out all fields.");
        return false;
    }

    if (!isValidEmail(email)) {
        alert("Please enter a valid email address.");
        return false;
    }

    // Save form data to localStorage
    localStorage.setItem('reviewData', JSON.stringify({
        Name: name,
        Email: email,
        Message: message
    }));

    alert("Your feedback has been submitted");

    return true;
}

function isValidEmail(email) {
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

function displayCopyright() {
    const year = new Date().getFullYear();
    document.getElementById("copyright").innerText = year;
}