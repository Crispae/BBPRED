$(document).ready(function() 
{

	$('form').on('submit', function(event)
	{

		$.ajax({
			data : {
				name : $('#smiles').val(),
				email : $('#algo').val()
			},
			type : 'POST',
			url : '/predict'
		})
		.done(function(data) {

			if (data.error) {
				$('#errorAlert').text(data.error).show();
				$('#successAlert').hide();
			}
			else {
				$('#successAlert').text(data.name).show();
				$('#errorAlert').hide();
			}

		});

		event.preventDefault();

	});

});