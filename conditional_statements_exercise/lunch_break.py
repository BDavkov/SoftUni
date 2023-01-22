from math import ceil

movie_name = input()
movie_duration = int(input())
rest_time = int(input())

lunch = rest_time / 8
break_time = rest_time / 4
time_left = rest_time - lunch - break_time

if time_left >= movie_duration:
    print(f"You have enough time to watch {movie_name} and left with {ceil(time_left - movie_duration)} minutes free time.")
else:
    print(f"You don't have enough time to watch {movie_name}, you need {ceil(movie_duration - time_left)} more minutes.")
