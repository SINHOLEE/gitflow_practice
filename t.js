// 3:15
// 3: 52
// 4:41
function solution(n) {
	function rec(s, o, e, n, answer) {
		if (n === 1) {
			answer.push([s, e]);
			return [...answer];
		}
		answer.concat(rec(s, e, o, n - 1, answer));
		answer.push([s, e]);
		answer.concat(rec(o, s, e, n - 1, answer));

		return answer;
	}

	return rec(1, 2, 3, n, []);
}
console.log(solution(4));
