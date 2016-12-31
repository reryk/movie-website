from django.template.defaultfilters import slugify
from django.db.models import F
# models are imported within functions to prevent circular dependencies


def alter_title_in_watchlist(user, title, watchlist_instance, watch=None, unwatch=None):
    from ..models import Watchlist
    if watch:
        if watchlist_instance and watchlist_instance.imdb:
            # this is when you delete title imdb=True and then you add it again
            watchlist_instance.deleted = False
            watchlist_instance.save(update_fields=['deleted'])
        else:
            Watchlist.objects.create(user=user, title=title)
    elif unwatch:
        if watchlist_instance.imdb:
            watchlist_instance.deleted = True
            watchlist_instance.save(update_fields=['deleted'])
        else:
            watchlist_instance.delete()


def alter_title_in_favourites(user, title, fav=None, unfav=None):
    from ..models import Favourite
    user_favourites = Favourite.objects.filter(user=user)
    if fav:
        Favourite.objects.create(user=user, title=title, order=user_favourites.count() + 1)
    elif unfav:
        favourite_instance = user_favourites.filter(title=title).first()
        user_favourites.filter(order__gt=favourite_instance.order).update(order=F('order') - 1)
        favourite_instance.delete()


def average_rating_of_title(title):
    from ..models import Rating
    current_ratings = Rating.objects.filter(title=title).order_by('user', '-rate_date').distinct('user')\
        .values_list('rate', flat=True)
    if current_ratings.exists():
        # avg_rate = 1
        avg_rate = sum(rate for rate in current_ratings) / current_ratings.count()
        return round(avg_rate, 1), current_ratings.count()
    return None, None


def create_slug(title, new_slug=None):
    from ..models import Title
    # recursive function to get unique slug (in case of 2 titles with the same name/year)
    slug = slugify('{} {}'.format(title.name, title.year))[:70] if new_slug is None else new_slug
    if Title.objects.filter(slug=slug).exists():
        slug += 'i'
        create_slug(title, slug)
    return slug

