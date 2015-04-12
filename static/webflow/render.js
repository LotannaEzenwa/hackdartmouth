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
	console.log(result)
	$('#main_arg_title').text(result.title);
	$('#main_arg_body').text(result.text);
	$('#author_link').text('Posted by ' + result.author);
	var disagree_count = 0; var agree_count = 0; var neutral_count = 0;
	for (var i = 0; i < result.votes.length; i++) {
		if (result.votes[i][1] == 'disagree') disagree_count++;
		if (result.votes[i][1] == 'agree') agree_count++;
		if (result.votes[i][1] == 'neutral') neutral_count++;
	};
	$('#disagree_count').text(disagree_count.toString() + ' Disagree')
	$('#agree_count').text(agree_count.toString() + ' Agree')
	$('#neutral_count').text(neutral_count.toString() + ' Unsure/Neutral')
	if (result.pro_sons.length == 0) {
		$('#prolist').text('No one has expressed any detailed support for this argument. Would you like to?')
	} else {
		for (var i = 0; i < result.pro_sons.length; i++) {
			son_ID = result.pro_sons[i]
			$.ajax({
				url :'/get_argument', 
				type : 'GET',
				data : {id : result.pro_sons[i]},
				dataType: "json",
				success : function(son, status) {
					var rgba = 'rgba('+(Math.floor(Math.random()*256))+','+(Math.floor(Math.random()*256))+','+(Math.floor(Math.random()*256))+',.3)'
					$('#prolist').append($('<li class="list-item" style="background-color:'+rgba+'"> <a href="/'+son.id+'">  <strong>' + son.title + '</strong> </a> <br>' + son.text + '</li>'))
				}
			});
		};
	}

	if (result.con_sons.length == 0) {
		$('#conlist').text('No one has expressed any detailed opposition to this argument. Would you like to?')
	} else {
		for (var i = 0; i < result.con_sons.length; i++) {
			son_ID = result.con_sons[i]
			$.ajax({
				url :'/get_argument',
				type: 'GET',
				data: {id: result.con_sons[i]},
				dataType: "json",
				success: function (son, status) {
					var rgba = 'rgba('+(Math.floor(Math.random()*256))+','+(Math.floor(Math.random()*256))+','+(Math.floor(Math.random()*256))+',.3)'
					$('#conlist').append($('<li class="list-item" style="background-color:'+rgba+'"> <a href="/'+son.id+'">  <strong>' + son.title + '</strong> </a> <br>' + son.text + '</li>'))
				}
			});
		}
	}
}

function submit_arg(ID, pro) {
	if (pro) {
		var this_text = $("#newpro").val()
		var this_title = $("#newpro_title").val()
	} else {
		var this_text = $('#newcon').val()
		var this_title = $("#newcon_title").val()
	}

	$.ajax({
		url: '/add_argument',
		type: 'POST',
		data: {title: this_title, text: this_text, mom: ID, pro: pro},
		dataType: "json",
		success: function() {
			window.location.reload()
		}
	});
}

function vote(type, ID) {
	$.ajax({
		url: '/vote',
		type: 'POST',
		data: {ID: ID, type: type},
		dataType: "json",
		success: function() {
			window.location.reload()
		}
	});
}