int ListSum (IntList l) {
	int sum = 0;
	while (l != NULL) {
		sum = sum + 1->val;
		l = l->next;
	}
	return sum;
}
