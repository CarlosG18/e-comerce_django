document.addEventListener('DOMContentLoaded', function() {
  var btn_remove = document.getElementById("btn_remove");
  var btn_add = document.getElementById("btn_add");
  var quantidade = document.getElementById("qtd_falta");

  btn_add.addEventListener('click', function(){
    quantidade.value = parseInt(quantidade.value) + 1;
  });

  btn_remove.addEventListener('click', function(){
    quantidade.value = parseInt(quantidade.value) - 1;
  });
});
