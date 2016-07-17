var AjaxForm = {

	init : function () {
		$("[data-form]").on('submit', function(e){
			e.preventDefault();

			var frm = $(this);
			var btn = $("[type='submit']", frm);
			var url = frm.attr('action');

			btn.attr('disabled', 'disabled')

			btn.button('loading');

			$.post(url, frm.serializeArray(), function (data){	
				console.log(data);			
				btn.removeAttr('disabled')
				btn.button('reset');
				window[frm.data('onsuccess')](data);
			});
		});
	},
};

var DonateBtn = {

	init: function () {
		$(".donate-form").on('click', DonateBtn.saveTransaction);
	},

	saveTransaction: function (e) {

		e.preventDefault();
		var frm = $(this);
		var btn = $("button[type='submit']");
		var amount = $('[name="amount"]', frm).val()
		
		btn.button('loading');
		var data = {
			'campaign': frm.data('campaign')
		};
		
		$.post('/api/transactions/', data, function (data){

			var returnUrl = $('[name="return_url"]', frm);
			var url = returnUrl.val() + data.id + '&amt=' + amount
			returnUrl.val(url);
			frm.submit();

		});

	}

};

$(document).ready(function (){
	AjaxForm.init();
	DonateBtn.init();
});