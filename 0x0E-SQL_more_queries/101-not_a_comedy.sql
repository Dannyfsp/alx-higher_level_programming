-- list all shows without the genre comedy in the database hbtn_0d_tvshows
-- The tv_shows table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_genres.title
-- Results must be sorted in ascending order by the genre name
-- We can use a maximum of two SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT tv_genres.title
FROM tv_genres
WHERE title NOT IN (
	SELECT tv_genres.title
	FROM tv_shows
	INNER JOIN tv_show_genres
	ON tv_shows.id = tv_show_genres.show_id
		INNER JOIN tv_genres
		ON tv_show_genres.genre_id = tv_genres.id
	WHERE tv_shows.name = 'Comedy'
)
ORDER BY tv_genres.title;