// 7:28
// 7:39
class Node {
	constructor(x, y, index) {
		this.level = y;
		this.value = x;
		this.key = index + 1;
		this.left = null;
		this.right = null;
	}
	willGoLeft(targetNode) {
		return this.value > targetNode.value;
	}
	insertAtLeft(targetNode) {
		this.left = targetNode;
	}
	insertAtRight(targetNode) {
		this.right = targetNode;
	}
}
class BinTree {
	constructor() {
		this.root = null;
		this.preOrder = [];
		this.postOrder = [];
	}

	insertNode(targetNode) {
		if (this.root === null) {
			this.root = targetNode;
			return;
		}
		this._insertNode(this.root, targetNode);
	}
	_insertNode(currNode, targetNode) {
		if (currNode.willGoLeft(targetNode)) {
			if (currNode.left === null) {
				currNode.insertAtLeft(targetNode);
			} else {
				this._insertNode(currNode.left, targetNode);
			}
		} else {
			if (currNode.right === null) {
				currNode.insertAtRight(targetNode);
			} else {
				this._insertNode(currNode.right, targetNode);
			}
		}
	}
	preOrderTravarse() {
		this.preOrder = [];

		this._preOrderTraverse(this.root);
		return this.preOrder;
	}
	_preOrderTraverse(currNode) {
		if (currNode === null) {
			return;
		}
		this.preOrder.push(currNode.key);
		this._preOrderTraverse(currNode.left);
		this._preOrderTraverse(currNode.right);
	}
	postOrderTravarse() {
		this.postOrder = [];

		this._postOrderTraverse(this.root);
		return this.postOrder;
	}
	_postOrderTraverse(currNode) {
		if (currNode === null) {
			return;
		}
		this._postOrderTraverse(currNode.left);
		this._postOrderTraverse(currNode.right);
		this.postOrder.push(currNode.key);
	}
}

function solution(nodeinfo) {
	function comaparator(a, b) {
		if (a[1] === b[1]) {
			return a[0] - b[0];
		}
		return b[1] - a[1];
	}

	const newNodeinfo = nodeinfo.map((node, i) => [node[0], node[1], i]).sort(comaparator);
	const binTree = new BinTree();
	newNodeinfo.forEach((node) => binTree.insertNode(new Node(...node)));

	// console.log(binTree);

	return [binTree.preOrderTravarse(), binTree.postOrderTravarse()];
}
console.log(
	solution([
		[5, 3],
		[11, 5],
		[13, 3],
		[3, 5],
		[6, 1],
		[1, 3],
		[8, 6],
		[7, 2],
		[2, 2],
	]),
);
