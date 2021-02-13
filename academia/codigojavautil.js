//Convertimos en array las variables en el GET
function getVariableGetByName() {
   var variables = {};
   var arreglos = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(m,key,value) {
      variables[key] = value;
   });
   return variables;
}

if (getVariableGetByName()['vuelve'] == '1'){
	if (getVariableGetByName()['detalle'] != '0'){
		tema_id = getVariableGetByName()['tema'];
		tema = document.getElementById('tema_' + tema_id);
		tema.parentElement.querySelector(".nested").classList.toggle("active");
    	tema.classList.toggle("check-box");
		capitulo_id = getVariableGetByName()['capitulo'];
		capitulo = document.getElementById('capitulo_' + capitulo_id);
		capitulo.parentElement.querySelector(".nested").classList.toggle("active");
    	capitulo.classList.toggle("check-box");
    	detalle = document.getElementById("detalle_" + getVariableGetByName()['detalle']);
    	detalle.style.background = "#ffaadd";
	} else {
			if (getVariableGetByName()['tema'] != '0'){
				capitulo_id = getVariableGetByName()['capitulo'];
				capitulo = document.getElementById('capitulo_' + capitulo_id);
				capitulo.parentElement.querySelector(".nested").classList.toggle("active");
		    	capitulo.classList.toggle("check-box");
		    	tema = document.getElementById("tema_" + getVariableGetByName()['tema']);
		    	tema.style.background = "#ffaadd";
			}
			else {
	    		capitulo = document.getElementById("capitulo_" + getVariableGetByName()['capitulo']);
	    		capitulo.style.background = "#ffaadd";

			}		
	} 
}
if alert(getVariableGetByName()['vuelve']) != 1
{
	if alert(getVariableGetByName()['detalle']) != '0'	{
		alert('detalle');
		// this.parentElement.querySelector(".nested").classList.toggle("active");
  //   	this.classList.toggle("check-box");
    }
}

