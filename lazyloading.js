const Bread = (() => {
	function Bread(breadType) {
		this.breadType = breadType;
		console.log('=======');
		console.log('복잡한 시간 많이 걸리는 작업 -> 빵만들기');
		console.log(breadType);
		console.log('=======');
		console.log();
	}
	return Bread;
})();

const Bakery = (() => {
	function Bakery() {
		this.requiredBreads = [];
	}
	Bakery.prototype.orderBreadType = function (breadType) {
		this.requiredBreads.push(breadType);
	};
	Bakery.prototype.pickUpBread = function (breadType) {
		console.log(`${breadType} 픽업하기요청!!`);
		if (!this.breads) {
			this.createBreads();
		}
		for (let i = 0; i < this.breads.length; i++) {
			debugger;
			if (this.breads[i].breadType === breadType) return this.breads[i];
		}
	};
	Bakery.prototype.createBreads = function () {
		this.breads = [];
		this.requiredBreads.forEach((breadType) => this.breads.push(new Bread(breadType)));
	};

	return Bakery;
})();
const bakery = new Bakery();
bakery.orderBreadType('우유식빵');
bakery.orderBreadType('몽블랑');
bakery.orderBreadType('딸기케이크');
bakery.orderBreadType('바게트');
console.log(bakery.pickUpBread('바게트'));
console.log(bakery.pickUpBread('몽블랑'));
