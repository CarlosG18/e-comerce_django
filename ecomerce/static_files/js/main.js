var modals = document.querySelectorAll("#modal");
var btns = document.querySelectorAll("#button");
var span = document.getElementsByClassName("close")[0];

for (var i = 0; i < btns.length; i++) {
  console.log(btns[i])
  btns[i].onclick = function() {
  modals[i].style.display = "block";
  }
}