$(document).ready(function(){
    
  $("#blanks form").submit(function(event){

    var button1 = parseInt($("input:radio[name=button1]:checked").val());
    var button2 = parseInt($("input:radio[name=button2]:checked").val());
    var button3 = parseInt($("input:radio[name=button3]:checked").val());

   
    var result= 0;
   
    if (button1===10){
      
      result+=10;
    }
    if (button2===10){
      
      result+=10;
    } 
    if (button3===10){
      
      result+=10;
    }
    
    $(".final").show();
    $("#display").text("Your score is: " + result+"/30 Marks");
   
    event.preventDefault();
    }) 
    

  });
 
   
  

   