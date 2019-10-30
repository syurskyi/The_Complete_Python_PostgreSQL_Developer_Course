# INSERT INTO public.users(id, name)
# VALUES (1, 'marysmith');
# 
# SELECT * FROM public.users;
# 
# INSERT INTO public.users()
# VALUES (2, 'rolfsmith');
# 
# SELECT * FROM public.users;
# 
# SELECT * FROM public.videos;
# 
# INSERT INTO public.videos
# VALUES (1, 10, 'Test Video');  # ERROR
# 
# INSERT INTO public.videos
# VALUES (1, 2, 'Test Video');
# 
# SELECT * FROM public.videos;
# 
# SELECT * FROM public.videos INNER JOIN public.users ON public.users.id = public.videos.user_id;

