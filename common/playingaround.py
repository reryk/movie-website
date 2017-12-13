import django
import os
from django.contrib.auth import get_user_model
from django.db.models import Q

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()
import pytz
from accounts.models import *
import sys
user = User.objects.all().first()

from mysite.settings import MEDIA_ROOT

User = get_user_model()
collection_id = 119

from tmdb.api import TmdbWrapper, PopularMovies, TitleUpdater, MovieTmdb, TmdbResponseMixin, PopularPeople, \
    NowPlayingMovies, UpcomingMovies
from titles.models import Title, Person, Collection

# c = Collection.objects.get(id=119)
# print(c)
# print(c.titles.all())
# t = c.titles.all()[0]
# print(t.collection.all())

title_in_collection = 'tt0120737'
xfiles = 'tt0106179'
# Title.objects.filter(imdb_id=title_in_collection).delete()
# TmdbWrapper().get(title_in_collection, call_updater=True)
# person, created = Person.objects.update_or_create(pk=1000,
#     defaults={'name': 'testo tsetst', 'image_path': ''}
# )
# person2, created2 = Person.objects.update_or_create(pk=1001,
#     defaults={'name': 'testo tsetst', 'image_path': ''}
# )
# Title.objects.filter(imdb_id=xfiles).delete()
# TmdbWrapper().get(xfiles, call_updater=True)

def database_is_clean():
    title_in_collection = 'tt0120737'
    TmdbWrapper().get(title_in_collection, call_updater=True)
    PopularMovies().get()
    User.objects.create_user(username='test', password='123')
# database_is_clean()

# print(Person.objects.get(pk=17051).name)
# print(Person.objects.get(pk=17051).slug)
# for p in Person.objects.all():
#     if not p.slug:
#         print(p.name)
#         print(p.slug)

def get_daily():
    # PopularPeople().get()
    # PopularMovies().get()
    # NowPlayingMovies().get()
    UpcomingMovies().get()

# get_daily()

def get_person(value):
    person, created = Person.objects.update_or_create(
        pk=value['id'], defaults={'name': value['name'], 'image_path': value['profile_path'] or ''}
    )
    return person


# for t in Title.objects.all():
#     print(t.overview)

# def random_date():
#     start = datetime(2010, 1, 1, tzinfo=pytz.utc)
#     end = datetime.now(tz=pytz.utc)
#     return start + timedelta(seconds=random.randint(0, int((end - start).total_seconds())))
#
#
# def get_random_title():
#     idtitle = random.randint(1, Title.objects.count())
#     return Title.objects.filter(id=idtitle).first()
#
#
# def get_random_rated_title(user):
#     titles = Title.objects.filter(rating__user=user).values_list('const', flat=True).distinct()
#     return Title.objects.get(const=random.choice(titles))
#
#
# def get_random_recommended_title(user):
#     titles = Title.objects.filter(watchlist__user=user).values_list('const', flat=True).distinct()
#     return Title.objects.get(const=random.choice(titles))
#
# def get_random_user(user):
#     us = User.objects.exclude(username=user.username).values_list('id', flat=True)
#     return User.objects.get(id=random.choice(us))


# for i in range(15):
#     # better nicknames?
#     username = 'dummy' + str(i)
#     password = '123123'
#     user, created = User.objects.get_or_create(username=username)
#     user.set_password(password)
#     user.save()
#
#     if not Rating.objects.filter(user=user).exists():
#         r = random.randint(0, random.randint(1, 1000))
#         r2 = random.randint(0, random.randint(1, 120))
#         r3 = random.randint(0, random.randint(1, 200))
#         r4 = random.randint(0, random.randint(1, 200))
#         r5 = random.randint(0, random.randint(1, 10))
#
#         for j in range(r):
#             rate = random.randint(1, 10)
#             title = get_random_title()
#             if title:
#                 d = random_date()
#                 if not Rating.objects.filter(user=user, title=title, rate_date=d).exists():
#                     Rating.objects.get_or_create(user=user, title=title, rate=rate, rate_date=d)
#
#         for j in range(r2):
#             title = get_random_title()
#             if title:
#                 d = random_date()
#                 if not Favourite.objects.filter(user=user, title=title).exists():
#                     Favourite.objects.get_or_create(user=user, title=title, added_date=d)
#
#         for j in range(r3):
#             title = get_random_title()
#             if title:
#                 d = random_date()
#                 if not Watchlist.objects.filter(user=user, title=title).exists():
#                     Watchlist.objects.get_or_create(user=user, title=title, added_date=d)
#
#         for j in range(r4):
#             title = get_random_rated_title(user)
#             if title:
#                 d = random_date()
#                 rate = random.randint(1, 10)
#                 if not Rating.objects.filter(user=user, title=title, rate_date=d).exists():
#                     Rating.objects.get_or_create(user=user, title=title, rate=rate, rate_date=d)
#
#         for j in range(r5):
#             u = get_random_user(user)
#             UserFollow.objects.get_or_create(user_follower=user, user_followed=u)
#         # recommend titles to followed (they should not be unrecommended when the user is deleted)
#
#     # else:
#     #     Rating.objects.filter(user=user).delete()
