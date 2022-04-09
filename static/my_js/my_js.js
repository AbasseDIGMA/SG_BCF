
     var ecole= document.getElementById("ecole");
     var classe= document.getElementById("classe");
     var annee= document.getElementById("annee");

     var L=screen.height()
     var l=screen.width();
     ecole.addEventListener("click", addecole);
     function addecole(){
          var position= elementPosition(ecole) 
          window.open("{% url 'login_url' %}", "-parent", "width=300, height=50, left=position.clientX, top=position.clientY, toolbar=no, titlebars=no, scrollbar=no");
          }
