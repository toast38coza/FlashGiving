var AjaxForm = {

	init : function () {
		$("[data-form]").one('submit', function(e){
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
		$(".donate-form").one('submit', DonateBtn.saveTransaction);
	},

	saveTransaction: function (e) {

		e.preventDefault();
		var frm = $(this);
		var btn = $("button[type='submit']", frm);
		var amount = $('[name="amount"]', frm).val()

		btn.button('loading');
		var data = {
			'campaign': frm.data('campaign'),
			'csrfmiddlewaretoken': $("[name='csrfmiddlewaretoken']", frm).val()
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


function calculate67MinSalary (form, id) {
		var salary = form.monthlySalary.value;
		var WORKING_DAYS = 20;
		var HOURS_IN_A_DAY = 8;
		var totalMinutes = (WORKING_DAYS * HOURS_IN_A_DAY * 60) / 67;
		debugger;
		document.getElementById('salary_to_donate_'+id).text = totalMinutes;
}
