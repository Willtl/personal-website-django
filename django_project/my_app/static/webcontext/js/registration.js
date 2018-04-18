var page_id = $('#page_id').val();

$(document).ready(function() {
	// $('html, body').animate({
	// scrollTop : 0
	// }, 0, 'swing');
});

$(document).on('submit', '#register_form', function(e) {
	e.preventDefault();
	var form = $(this);
	if (form.data('submitted') === true) {
		// Previously submitted - don't submit again
		console.log('already submitted');
		e.preventDefault();
		show_info('You already submited a comment.');
	} else {
		$.ajax({
			type : 'POST',
			url : page_id,
			data : {
				atrb_username : $('#id_atrb_username').val(),
				atrb_email : $('#id_atrb_email').val(),
				atrb_password : $('#id_atrb_password').val(),
				csrfmiddlewaretoken : $('#id_csrf_token').val()
			},
			success : function() {
				console.log('success');
				// Mark it so that the next submit can be ignored
				form.data('submitted', true);
				// Disable button
				disable_element('#button_register');
				// Clean form values
				clean_form_values();
				// Hide error messages
				//hide_error();
				// Update comment section values
				//$('#content_section').load(page_id + ' #content_section > *').fadeIn('slow');
				// Smoth scroll to the top
				//$('html, body').animate({
				//	scrollTop : $("#comments_header").offset().top - $("#comments_header").height()
				//}, 1000);
				// Enable button
				//enable_element('#button_register');
			}
		});
	}
});

function show_error(message) {
	$('#comment_form_error').css('display', 'block');
	$('#error_message').text(message);
}

function hide_error() {
	$('#comment_form_error').css('display', 'none');
	$('#error_message').text('');
}

function show_info(message) {
	$('#comment_form_info').css('display', 'block');
	$('#info_message').text(message);
}

function hide_info() {
	$('#comment_form_info').css('display', 'none');
	$('#info_message').text('');
}

function disable_element(element) {
	$(element).attr('disabled', 'true');
}

function enable_element(element) {
	$(element).removeAttr("disabled");
}

function clean_form_values() {
	$('#id_atrb_username').val('');
	$('#id_atrb_email').val('');
	$('#id_atrb_password').val('');
}

function isEmail(email) {
	var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
	return regex.test(email);
}