front.on("device-list", function (msg) {
	$('#deviceSelect').empty();

	for (const key in msg) {
		$('#deviceSelect').append(`<option value=${key}>${msg[key]}</option>`);
	}

	$('#devices-modal').modal('toggle')
});

$('#connectBtn').click(() => {
	let uuid = $('select').val()
	$('modal-status').html(`Connecting...`);
	$('#modal-status').html(`Connecting <div class="spinner-border" role="status">
		<span class="visually-hidden">Loading...</span>
	</div>`)

	front.send('connect-device', uuid);
})


$("#btnConnected").click(() => {
	front.send('scan-devices');
})

front.on('connected', function (data) {
	if (data.isConnected) {
		$('#devices-modal').modal('toggle');
		$("#btnConnected").text('Connected');

		if ($("#btnConnected").hasClass('btn-danger')) {
			$("#btnConnected").removeClass('btn-danger')
			$("#btnConnected").addClass('btn-success')
		}

		$('#card').removeClass('visually-hidden')

	} else {
		$('modal-status').html(`<span class="text-danger">Unable to Connect</span>`);
		$('#card').addClass('visually-hidden')
	}
})


$('#sendBtn').click(function () {
	let shots = $('#shotsInput').val()
	let delay = $('#delayInput').val()
	let wait = $('#waitInput').val()
	let status = $('#program-select').val()

	$('#remaining-shots').text(shots)

	await _delay.writeValue(Buffer.from(delay.toString()))
	await _shots.writeValue(Buffer.from(shots.toString()))
	await _wait.writeValue(Buffer.from(wait.toString()))
	await _status.writeValue(Buffer.from(status.toString()))
})


$('#stopBtn').click(function (){
	front.send('send-payload', {
		shots: 0,
		delay: 0,
		wait: 0,
		status: 0
	})
})

window.onbeforeunload = function () {
	front.send('disconnect')
};

front.on('shots-remaining', function (data) {
	$('#remaining-shots').text(data)
})
