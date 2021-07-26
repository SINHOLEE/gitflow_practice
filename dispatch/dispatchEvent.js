function preventDef(event) {
	event.preventDefault();
	console.log(123);
}

function addHandler() {
	document.getElementById('checkbox').addEventListener('c', preventDef, false);
}

function removeHandler() {
	document.getElementById('checkbox').removeEventListener('c', preventDef, false);
}

function simulateClick() {
	var evt = document.createEvent('MouseEvents');
	const clickEvent = new CustomEvent('c');
	console.log(evt);
	console.log(clickEvent);
	evt.initMouseEvent('c', true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
	var cb = document.getElementById('checkbox');
	var canceled = !cb.dispatchEvent(clickEvent);
	if (canceled) {
		// A handler called preventDefault
		alert('canceled');
	} else {
		// None of the handlers called preventDefault
		alert('not canceled');
	}
}
