studies(Peter, maths).
studies(Paul, arts).
studies(Mary, physics).

teaches(Richard, arts).
teaches(Sam, maths).
teaches(Sam, physics).

professor(X, Y) :- 
	teaches(X,S), 
	studies(Y,S).

