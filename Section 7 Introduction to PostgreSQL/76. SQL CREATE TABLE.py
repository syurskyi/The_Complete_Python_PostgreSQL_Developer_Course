# CREATE TABLE public.users(
# id INTEGER PRIMARY KEY,
# name CHARACTER VARYING(100) NOT NULL,
# )
#
# CREATE TABLE public.users(
# id INTEGER,
# name CHARACTER VARYING(100) NOT NULL,
# CONSTAINT users_id_pkey PRIMARY KEY (id)
# )
#
# SELECT * FROM public.users;
#
# CREATE TABLE public.videos(
# id INTEGER PRIMARY KEY,
# user_id INTEGER REFERENCES public.users,
# name CHARACTER VARYING(255) NOT NULL
# )
