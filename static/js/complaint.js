//$(document).ready(function() {
//    $("button.py").each(function(){
//        $(this).bind('click', function(){
//            $("form.p-3").each(function(){
//                $(this).toggle();
//            });
//        });
//    });
//});

$(document).ready(function() {
    $("div.pyy").html('<button class="py" type="button" onclick="Openform()";><ion-icon size="large" name="create"></ion-icon></button>');
    $(document).on("click", "button.py", function() {
        alert("Button was clicked"+this.id);
        $("form.p-3").each( function() {
            $(this).toggle();
        });
    });
});

//function Openform()
//{
//    alert(this.length);
//    var x = document.getElementById('py1');
//    //var x = document.getElementsByClassName("form.p-3");
//    var i;
//    for (i = -1; i < x.length; i++) {
//        x[i].style.display = '';
//       // alert("Hi");
//    }
//}
