var btnContainer = document.getElementById("side_nav");
console.log(btnContainer);
var btns = btnContainer.getElementsByClassName("nav_list");

for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function() {
    var current = document.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.className += " active";
  });
}
