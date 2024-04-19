var l1 = document.getElementById("l1");
var l2 = document.getElementById("l2");
var l3 = document.getElementById("l3");
var hide_btn = document.getElementById("hide");
var show_btn = document.getElementById("show");
var tabs = document.getElementById("tabs");
var cover = document.getElementById("cover");
var glow = document.getElementById("glow");
var sun = document.getElementById("sun");
var navbar = document.getElementById("navbar");
var logo = document.getElementById("logo");
var theme=document.getElementById("theme");
var buttons=document.getElementById("buttons");

var sq=document.getElementById("square");
var fixed=document.getElementById("fixed");
function changeCss() {
    this.scrollY > 10 ? square.style.opacity = 0 : square.style.opacity = 1;
    this.scrollY > 140 ? fixed.style.opacity="0" : fixed.style.opacity=1;
    this.scrollY > 140 ? document.getElementById("c1").style.height="53vh" : document.getElementById("c1").style.height="0vh";
    this.scrollY > 300 ? document.getElementById("c2").style.width="27vw" : document.getElementById("c2").style.width="0vw";
    this.scrollY > 300 ? document.getElementById("info").style.opacity="1" : document.getElementById("info").style.opacity="0";
    this.scrollY > 300 ? document.getElementById("info").style.marginLeft="5vw" : document.getElementById("info").style.marginLeft="3vw";
}

window.addEventListener("scroll", changeCss, false);


const targetCount = 7;
const counterElement = document.getElementById('users');
function updateCounter(count) {
    counterElement.textContent = count;
}
function startCounter() {
    let count = 0;
    const intervalId = setInterval(function () {
        if (count < targetCount) {
            count++;
            updateCounter(count);
        } else {
            clearInterval(intervalId);
        }
    }, 200);
}
window.onload = startCounter;

function show() {
    l1.style.transform = "rotate(45deg)";
    l2.style.opacity = 0;
    l3.style.transform = "rotate(-45deg)";
    hide_btn.style.display = "flex";
    tabs.style.marginLeft = "70vw";
    cover.style.width = "calc(100vw - 20px - 6vh)";
    document.getElementById("top").style.opacity = 0;
    navbar.style.height="100vh";
    document.getElementById("body").style.overflowY="hidden";
    buttons.style.opacity=1;
    buttons.style.left="20px";
}
function hide() {
    l1.style.transform = "rotate(0deg)";
    l2.style.opacity = 1;
    l3.style.transform = "rotate(0deg)";
    hide_btn.style.display = "none";
    tabs.style.marginLeft = "150vw";
    cover.style.width = "0vw";
    document.getElementById("top").style.opacity = 1;
    navbar.style.height="calc(5vh + 20px)";
    document.getElementById("body").style.overflowY="scroll";
    buttons.style.opacity=0;
    buttons.style.left="-30px";
}
var light = function theme() {
    glow.style.border = "2px dotted white";
    glow.style.padding = "2px";
    sun.style.height = "2vh";
    sun.style.width = "2vh";
    sun.style.opacity = 1;
    glow.style.boxShadow = "0px 0px 10px #00000000";
    document.getElementById("body").style.backgroundColor = "rgba(0,0,0, 0.2)";
    document.getElementById("body").style.filter = "invert(1)";
    document.getElementById("theme").setAttribute("onClick", "javascript: dark();");
    navbar.style.backgroundColor = "rgba(149, 149, 149, 0.738)";
    logo.style.filter = "invert(1)";
    cover.style.backgroundColor = "rgba(149, 149, 149, 0.738)";
    buttons.style.pointerEvents="fixed";
}

var dark = function theme2() {
    glow.style.border = "1px solid white";
    glow.style.padding = 0;
    sun.style.height = "2.6vh";
    sun.style.width = "2.6vh";
    sun.style.opacity = 0;
    glow.style.boxShadow = "0px 0px 10px white";
    document.getElementById("body").style.backgroundColor = "black";
    document.getElementById("body").style.filter = "invert(0)";
    document.getElementById("theme").setAttribute("onClick", "javascript: light();");
    navbar.style.backgroundColor = "rgba(149, 149, 149, 0.138)";
    logo.style.filter = "invert(0)";
    cover.style.backgroundColor = "rgba(149, 149, 149, 0.138)";
}

function topFunction() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

window.onscroll = function () {
    scrollFunction()
};

function scrollFunction() {
    if (document.body.scrollTop > 10 ||
        document.documentElement.scrollTop > 10) {
        navbar.style.backgroundColor="rgba(149, 149, 149, 0.138)";
        document.getElementById("top").style.opacity = 1;
    }
    else{
        navbar.style.backgroundColor="rgba(149, 149, 149, 0)";
        document.getElementById("top").style.opacity = 0;
    }
}
