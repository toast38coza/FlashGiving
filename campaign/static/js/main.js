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

	test : function () {
		console.log('test');
	}
};

var AjaxLink = {

	init : function () {
		$("[data-link]").on('click', function (el) {
			el.preventDefault();

		});
	}
};

$(document).ready(function (){
	AjaxForm.init();
});