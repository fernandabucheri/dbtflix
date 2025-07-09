with movies as (
    select * from {{ ref("stg_movies") }}
)

select
    movie_genre,
    count(movie_id) as total_movies,
    avg(movie_rating) as avg_rating
from movies
group by 1
order by 3 desc

