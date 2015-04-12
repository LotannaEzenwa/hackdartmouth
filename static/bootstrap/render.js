function get_data(ID) {
	$.ajax({
		url :'/get_argument', 
		type : 'GET',
		data : {id : ID},
		dataType: "json",
		success : function(result) {render(result)}
	});
// 	$(document).ready(function() {
// 	$.get('/get_argument', {id: ID}, render(data))
// })
}


function render(result) {
	$('#arg_body_p').text(result.text);
	$('#arg_title_h').text(result.title);
	$('#author_link').text(result.author)
	if (result.pro_sons.length == 0) {
		$('#prolist').text('No one has expressed any detailed support for this argument. Would you like to?')
	} else {
		for (var i = 0; i < result.pro_sons.length; i++) {
			$.ajax({
				url :'/get_argument', 
				type : 'GET',
				data : {id : result.pro_sons[i]},
				dataType: "json",
				success : function(son) {
					$('#prolist').append($("<li/>").text(son.text))
				}
			});
		};
	}

	if (result.con_sons.length == 0) {
		$('#conlist').text('No one has expressed any detailed opposition to this argument. Would you like to?')
	} else {
		for (var i = 0; i < result.con_sons.length; i++) {
			$.ajax({
				url :'/get_argument',
				type: 'GET',
				data: {id: result.con_sons[i]},
				dataType: "json",
				success: function (son) {
					$('#conlist').append($("<li/>").text(son.text))
				}
			});
		}
	}
}

function submit_arg(form, ID, pro) {
	if (pro) {
		var this_text = $("#newpro").val()
	} else {
		var this_text = $('#newcon').val()
	}

	$.ajax({
		url: '/add_argument',
		type: 'POST',
		data: {title: null, text: this_text, mom: ID, pro: pro},
		dataType: "json",
		success: function(next_ID, pro) {
			history.go(0)
		}
	});
}