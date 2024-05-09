var l1=document.getElementById("l1");
var l2=document.getElementById("l2");
var l3=document.getElementById("l3");
var burger=document.getElementById("burger");
var cross=document.getElementById("cross");
var plane=document.getElementById("plane");
var body = document.getElementById("body");

function show(){
    l2.style.opacity=0;
    l1.style.transform="rotate(-45deg)";
    l3.style.transform="rotate(45deg)";
    burger.style.display="none";
    cross.style.display="block";
    plane.style.width="calc(100vw - 60px)";
    body.style.overflowY = "hidden";
}
function hide(){
    l2.style.opacity=1;
    l1.style.transform="rotate(0deg)";
    l3.style.transform="rotate(0deg)";
    burger.style.display="block";
    cross.style.display="none";
    plane.style.width="0";
    body.style.overflowY = "scroll";
}