class Combiner {
	constructor() {
		this.watingForChunks = 0;
	}
	combine = (ingredients) => {
		console.log('-----start combining');
		ingredients
			.filter((_, index) => index % 2 === 0)
			.forEach((ingredient, idx) => {
				this.watingForChunks++;
				const worker = new Worker('combinerWorker.js');
				worker.addEventListener('message', this.complete);
				worker.postMessage({ingredients: ingredients.slice(idx * 2, idx * 2 + 2)});
			});
		test();
		for (const temp of Object.keys(this)) {
			console.log(`key: ${temp}, value: ${this[temp]}, this: ${this} `);
		}
		console.log(`combine this: ${this}`);
		function test() {
			console.log(`test ${this}`);
		}
	};
	complete = (message) => {
		this.watingForChunks--;
		console.log(`outstanding chunks cont at: ${this.watingForChunks}`);
		console.log(message.data.result);
		if (this.watingForChunks === 0) {
			console.log('---------all Done-----');
		}
	};
}

const combiner = new Combiner();

const ingredients = [
	1, 2, 3, 4, 5, 6, 7, 8, 9, 90, 1, 2, 3, 1, 3, 4, 2, 1, 3, 4, 2, 3, 1, 2, 3, 4, 2, 1, 2, 3, 4, 2,
	2, 3, 1, 2, 3, 1, 2, 3, 2, 1, 2, 3, 2,
];
combiner.combine(ingredients);
