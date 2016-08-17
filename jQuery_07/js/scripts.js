$(document).ready(function () {
    console.log("jQuery on tap");
    $("#sortable").sortable();
    $("#sortable").disableSelection();
    var cache = $("#sortable").html();

    $("#reset").click(function(){
        $("#sortable").html(cache).sortable("refresh");
        $("body").css("background", "#7abcff").hide().fadeIn("slow");
    });

    $("#check").click(function(){

    var order = $("#sortable").sortable("toArray");
    var counter = 0;

        for(var i = 0; i < order.length; i++){

           if( parseInt(order[i]) < parseInt(order[i+1]) ) {
               counter ++
          }
        }

        if(counter == 4){

            alert("Well done, the image is in order!")
            $("body").css("background", "#66cdaa").hide().fadeIn("slow");
        }else{
            alert("Keep going, not there yet!")
        }
    });
});
