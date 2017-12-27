from datetime import datetime

from django.contrib.auth import get_user_model
from django.db.models import F, Q

from accounts.models import UserFollow
from recommend.models import Recommendation
from titles.models import Rating, CurrentlyWatchingTV
from lists.models import Watchlist, Favourite

User = get_user_model()


def toggle_title_in_watchlist(user=None, title=None, watch=None):
    """
    adds or deletes title from user's watchlist. if title comes from IMDb's watchlist, it is only marked as 'deleted',
    because it would be added again with another watchlist update anyway
    """
    unwatch = not watch
    watchlist_instance = Watchlist.objects.filter(user=user, title=title).first()

    if watchlist_instance and watchlist_instance.imdb:
        watchlist_instance.deleted = False if watch else True
        watchlist_instance.save(update_fields=['deleted'])
        return 'Removed from watchlist'
    else:
        if watch:
            Watchlist.objects.create(user=user, title=title)
            return 'Added to watchlist'
        elif unwatch and watchlist_instance:
            watchlist_instance.delete()
            return 'Removed from watchlist'


def toggle_title_in_favourites(user, title, fav=True):
    """deletes or adds title to user's favourites"""
    user_favourites = Favourite.objects.filter(user=user)
    try:
        instance = user_favourites.get(title=title)
    except Favourite.DoesNotExist:
        Favourite.objects.create(user=user, title=title)
        return 'Added to favourites'
    else:
        instance.delete()
        return 'Removed from favourites'


def recommend_title(title, sender, user_ids):
    """sender recommends the title to user_ids"""
    pks_of_followed_users = UserFollow.objects.filter(follower=sender).exclude(
        Q(followed__rating__title=title) | Q(followed__recommendation__title=title)
    ).values_list('followed__pk', flat=True)

    users = User.objects.filter(Q(pk__in=pks_of_followed_users) & Q(pk__in=user_ids))
    for user in users:
        Recommendation.objects.create(user=user, sender=sender, title=title)

    if users:
        return f'Recommended to {users.count()} users'

    return 'Already recommended'


def follow_user(follower, followed, add):
    if add:
        UserFollow.objects.get_or_create(follower=follower, followed=followed)
        return f'Followed {followed.username}'
    else:
        UserFollow.objects.filter(follower=follower, followed=followed).delete()
        return f'Unfollowed {followed.username}'


def toggle_currently_watched_title(title, user, add):
    if add:
        CurrentlyWatchingTV.objects.get_or_create(title=title, user=user)
        return f'Watching {title.name}'
    else:
        CurrentlyWatchingTV.objects.filter(title=title, user=user).delete()
        return f'Not watching {title.name}'
