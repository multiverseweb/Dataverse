var l1=document.getElementById("l1");
var l2=document.getElementById("l2");
var l3=document.getElementById("l3");
var hide_btn=document.getElementById("hide");
var show_btn=document.getElementById("show");
var tabs=document.getElementById("tabs");
var cover=document.getElementById("cover");
function show(){
    l1.style.transform="rotate(45deg)";
    l2.style.opacity=0;
    l3.style.transform="rotate(-45deg)";
    hide_btn.style.display="flex";
    tabs.style.marginLeft="70vw";
    cover.style.width="calc(100vw - 20px - 6vh)";
}
function hide(){
    l1.style.transform="rotate(0deg)";
    l2.style.opacity=1;
    l3.style.transform="rotate(0deg)";
    hide_btn.style.display="none";
    tabs.style.marginLeft="110vw";
    cover.style.width="0vw";
}