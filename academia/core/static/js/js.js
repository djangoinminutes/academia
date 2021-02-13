// // Function to add event listener to t
// document.addEventListener("DOMContentLoaded", load, false);

// function load() {
// 	alert('hola');
//   var el = document.getElementById("link_busqueda");
//   el.addEventListener("click", modifyText, false);
// };

// function modifyText() {
//   var enlace = document.getElementById("link_busqueda");
//   var texto = document.getElementById("tx_busqueda");
//   // alert(texto.val);
//   // alert('texto' + texto.val());
//   enlace.attr('href','http://www.microsoft.com');
//   // link.attr('href',"{% url 'core:lista_cursos' %}" + '?criterio=' + texto.val());
// };

$(function(){
	var enlace = $('#link_busqueda');
	enlace.on('click',function(){
		var texto = $('#tx_busqueda');
		enlace.attr('href','http://127.0.0.1:8000/visitante/lista_cursos/?criterio=' + texto.val());
	});
}())

var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
    coll[i].innerHTML = '(Ver Descripcion ..)';
  	coll[i].addEventListener("click", function() {
    var content = this.nextElementSibling;
    if (content.style.display === "block") {
    	this.innerHTML = '(Ver Descripcion ..)'
      content.style.display = "none";
    } else {
      content.style.display = "block";
    	this.innerHTML = '(Ocultar Descripcion ..)'
    }
  });
}