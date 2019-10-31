# SELECT * FROM public.users WHERE name='rolfsmith';
# 
# SELECT * FROM public.users WHERE name='rolfsmith' LIMIT 1;
# 
# CREATE INDEX users_name_index ON public.users(name);
# 
# CREATE UNIQUE INDEX index_name ON table(column);
# 
# SELECT * FROM public.movies WHERE id=1 AND user_id=2;
# 
# CREATE UNIQUE INDEX index_name ON public.movies(id, user_id);
# 
# REINDEX INDEX users_name_index;
# 
# REINDEX TABLE users_name_index;
# 
# REINDEX DATABASE users_name_index;
# 
# REINDEX DATABASE database_name;
