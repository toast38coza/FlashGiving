
// Set by specific date/time
function set_by_date(id, options) {
	$('#countdown_1').stopCountDown();
	$('#countdown_1').setCountDown({
		targetDate: {
			'day': 		options.day || 0,
			'month': 	options.month || 0,
			'year': 	options.year || 0,
			'hour': 	options.hour || 0 ,
			'min': 		options.min || 0,
			'sec': 		options.sec || 0
		}
	});
	$('#countdown_1').startCountDown();
}

// set_by_date();

// Set by date/time offset
function set_by_offset(id, options) {
	$('#countdown_'+id).stopCountDown();
	$('#countdown_'+id).setCountDown({
		targetOffset: {
			'day': 		options.day || 0,
			'month': 	options.month || 0,
			'year': 	options.year || 0,
			'hour': 	options.hour || 0,
			'min': 		options.min || 0,
			'sec': 		options.sec || 0
		}
	});
	$('#countdown_'+id).startCountDown();
}
