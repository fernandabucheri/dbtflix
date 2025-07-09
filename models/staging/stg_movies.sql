SELECT
    id              AS movie_id
    , title         AS movie_title
    , genre         AS movie_genre
    , release_year  AS movie_release_year
    , rating        AS movie_rating  
FROM 
    read_csv_auto('data/movies.csv')
