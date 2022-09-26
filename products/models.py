from django.db import models
from django.utils.translation import gettext as _

FLAG_OPTION = (
    ('New','New'),
    ('Feature','Feature'),
    ('Sale','Sale'),
)
# Create your models here.
class Product(mpdels.model):
    name = models.CharField(max_length=100 , verbose_name=_("Name"))
    subtitle = models.CharField(_("Subtitle") , max_length=500)
    sku = models.IntegerField(_("SKU"))
    desc = models.TextField(_("Description") , max_length=10000)
    price = models.FloatField(_("Price"))
    flag = models.CharField(_("Flag") ,max_length=10 , choices=FLAG_OPTION)
    quantity = models.IntegerField(_("Quantity"))
    brand = ''
    category = ''

class ProductImages(mpdels.model):
    pass

class Brand(mpdels.model):
    pass

class Category(mpdels.model):
    pass

class ProductReview(mpdels.model):
    pass
