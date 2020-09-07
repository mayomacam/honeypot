$(function(){
	$(".signup").hide();
	$("#flipToSignUp").on("click", function(evt){
		$(".login").slideUp(600);
		$(".signup").slideDown(600);
	});
	$("#flipToSignIn").on("click", function(evt){
		$(".signup").slideUp(600);
		$(".login").slideDown(600);
	});	
});
$(function(){
	$("#passtry2").on("keyup keydown focusout", function(){
		var pass1 = frmsignout.newpass.value;
		var pass2 = frmsignout.confirmpass.value;
		if(pass1 == pass2 && pass1!='')
			$(this).css('border','2px solid lime');
		else{
				$(this).css('border','2px solid red');
			}
	});
})