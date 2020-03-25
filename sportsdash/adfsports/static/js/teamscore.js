var $DOM = $(document);

$DOM.on('click', '#teamsscorev', function() {

	
    data = {}
    data["TeamMatch"] = $("#TeamMatch").val();
    data["Sports"] = $("#Sports").val();
    data["Point"] = $("#Point").val();
    data["Wonby"] = $("#Wonby").val();
data["Lossby"] = $("#Lossby").val();
	
    $.ajax({
		type: 'post',
        data: JSON.stringify(data),
        async: false,
		url: 'teamsscoreapi/',
		success: function(result) {
            
                // alertify.set('notifier', 'position', 'top-right');
                 alert(result.message);
           
		}
	});
});


