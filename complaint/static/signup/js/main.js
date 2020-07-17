(function($) {

    $(".toggle-password").click(function() {

        $(this).toggleClass("zmdi-eye zmdi-eye");
        var input = $($(this).attr("toggle"));
        if (input.attr("type") == "password") {
          input.attr("type", "text");
        } else {
          input.attr("type", "password");
        }
      });
     $("#re_password").click( function() {

        $(this).toggleClass("glyphicon glyphicon-eye-open");
        //var input = $($(this).attr("toggle"));
        if ($(this).attr("type") == "password") {
          this.attr("type", "text");
        } else {
          this.attr("type", "password");
        }
      });


   })(jQuery);

