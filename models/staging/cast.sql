
SELECT
	rank,
	id,
	awards,
	REPLACE(runtime, ' min','')::INTEGER,
	released::DATE,
	metascore,
	country,
	director,
	genre,
	imdbrating,
	imdbvotes,
	language,
	title,
	type,
	year,
	poster,
	actors
FROM src."SOURCE_IMDB"

