/* 
SELECT * FROM movie WHERE title LIKE "%STAR WARS%"; 
SELECT * FROM movie,actor WHERE movie.title LIKE "%STAR WARS%" AND actor.name LIKE "%Ford, Harrison%";
SELECT * FROM movie,actor WHERE movie.title LIKE "%STAR WARS%" AND actor.name LIKE "%Fisher, Carrie%";
*/
SELECT * 	FROM movie,actor 
		WHERE movie.title LIKE "%STAR WARS%" AND
		actor.name LIKE "%Ford, Harrison%" ORDER BY movie.year;
