from django import template
from main_pages.models import FavoriteProduct, RatingProduct


register = template.Library()


@register.simple_tag()
def check_favorite(auth, product_id):
    return FavoriteProduct.objects.filter(auth=auth, product_id=product_id).exists()


@register.simple_tag()
def check_rating(auth, product_id):
    # проверяем есть ли рейтинг
    status = RatingProduct.objects.filter(auth=auth, product_id=product_id).exists()
    if status is True:
        # получаем рейтинг пользователя
        rating = RatingProduct.objects.get(auth=auth, product_id=product_id)
        try:
            # получаем все рейтинги продукта
            rating_all = RatingProduct.objects.filter(product_id=product_id)
            # получаем количество оценок продукта
            total_quantity = len(rating_all)
            # получаем сумму оценок продукта
            total_sum = sum([item.number_rating for item in rating_all])
            overall_rating = total_sum / total_quantity
            return {
                'rating': rating,
                'overall_rating': overall_rating
            }
        except:
            return {
                'rating': rating,
                'overall_rating': 0
            }
    else:
        try:
            # получаем все рейтинги продукта
            rating_all = RatingProduct.objects.filter(product_id=product_id)
            # получаем количество оценок продукта
            total_quantity = len(rating_all)
            # получаем сумму оценок продукта
            total_sum = sum([item.number_rating for item in rating_all])
            overall_rating = total_sum / total_quantity
            return {
                'status': 'show_form',
                'overall_rating': overall_rating
            }
        except:
            return {
                'status': 'show_form',
                'overall_rating': 0
            }
