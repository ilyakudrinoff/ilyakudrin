from django.core.paginator import Paginator
from config.settings import INTERVAL_END_NUM


def paginator(request, post_list):
    pag = Paginator(post_list, INTERVAL_END_NUM)
    page_number = request.GET.get('page')
    return pag.get_page(page_number)
