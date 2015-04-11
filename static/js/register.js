$(function() {
    $('.error').hide();
    $(".button").click(function() {
      // validate and process form here
      
    //   $('.error').hide();
  	 //  var email = $("input#email").val();
  		// if (email == "" || email.length() < 4) {
    //     $("label#email_error").show();
    //     $("input#email").focus();
    //     return false;
    //   }
  		// var username = $("input#username").val();
  		// if (username == "" || username.length() < 3) {
    //     $("label#username_error").show();
    //     $("input#username").focus();
    //     return false;
    //   }
  		// var password = $("input#password").val();
  		// if (password == "" || password.length() < 6) {
    //     $("label#password_error").show();
    //     $("input#password").focus();
    //     return false;
    //   }
      var dataString = 'email='+ email + '&username=' + username + '&password=' + password;
	  //alert (dataString);return false;
	  $.ajax({
	    type: "POST",
	    url: "/register",
	    data: dataString,
	    success: function() {
	      $('#register_form').html("<div id='message'></div>");
	      $('#message').html("<h2>Registration Submitted!</h2>")
	      .append("<p>Please <a href="login">login</a> now.</p>")
	      .hide()
	      // .fadeIn(1500, function() {
	      //   $('#message').append("<img id='checkmark' src='images/check.png' />");
	      // });
	    }
	  });
	  return false;
    });
  });