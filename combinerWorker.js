self.addEventListener('message', (e) => {
	const data = e.data;
	const ingredients = data.ingredients;
	let res = [];
	ingredients.forEach((ingredient) => res.push({ingredient, id: Date.now()}));
	let cnt = 0;
	const start = Date.now();
	while (cnt !== 300000000) {
		cnt++;
		continue;
	}
	combinationComplete(res);
	console.log(Date.now() - start);
});

function combinationComplete(res) {
	console.log('combination complete');
	self.postMessage({event: 'combinationComplete', result: res});
}
