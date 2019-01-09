from django.db import models

# Create your models here.

class Index_LinkerImage(models.Model):
    image = models.ImageField()
    text = models.TextField()
    link = models.TextField()
    alt = models.TextField()

    def __str__(self):
        return self.text


class Florarium_LinkerImage(models.Model):
    image = models.ImageField()
    text = models.TextField()
    link = models.TextField()
    alt = models.TextField()

    def __str__(self):
        return self.text


class Gift_LinkerImage(models.Model):
    image = models.ImageField()
    text = models.TextField()
    link = models.TextField()
    alt = models.TextField()

    def __str__(self):
        return self.text


class Goods_Florarium_EmptyForm(models.Model):
    id0 = models.IntegerField()
    image = models.ImageField()
    image_2 = models.ImageField(blank=True)
    image_3 = models.ImageField(blank=True)
    use_images = models.BooleanField()
    caption = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    old_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    alt = models.TextField(blank=True)

    def __str__(self):
        return self.caption


class Goods_Florarium_FullForm(models.Model):
    id0 = models.IntegerField()
    image = models.ImageField()
    image_2 = models.ImageField(blank=True)
    image_3 = models.ImageField(blank=True)
    use_images = models.BooleanField()
    caption = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    old_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    alt = models.TextField(blank=True)

    def __str__(self):
        return self.caption


class Goods_Gifts_ChristmasGift(models.Model):
    id0 = models.IntegerField()
    image = models.ImageField()
    image_2 = models.ImageField(blank=True)
    image_3 = models.ImageField(blank=True)
    use_images = models.BooleanField()
    caption = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    old_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    alt = models.TextField(blank=True)

    def __str__(self):
        return self.caption


class Goods_Gifts_VitrazhPicture(models.Model):
    id0 = models.IntegerField()
    image = models.ImageField()
    image_2 = models.ImageField(blank=True)
    image_3 = models.ImageField(blank=True)
    use_images = models.BooleanField()
    caption = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    old_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    alt = models.TextField(blank=True)

    def __str__(self):
        return self.caption


class Goods_Gifts_Souvenir(models.Model):
    id0 = models.IntegerField()
    image = models.ImageField()
    image_2 = models.ImageField(blank=True)
    image_3 = models.ImageField(blank=True)
    use_images = models.BooleanField()
    caption = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    old_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    alt = models.TextField(blank=True)

    def __str__(self):
        return self.caption


class Goods_Gifts_Lamp(models.Model):
    id0 = models.IntegerField()
    image = models.ImageField()
    image_2 = models.ImageField(blank=True)
    image_3 = models.ImageField(blank=True)
    use_images = models.BooleanField()
    caption = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    old_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    alt = models.TextField(blank=True)

    def __str__(self):
        return self.caption


class MasterClass(models.Model):
    id0 = models.IntegerField()
    image = models.ImageField()
    image_2 = models.ImageField(blank=True)
    image_3 = models.ImageField(blank=True)
    use_images = models.BooleanField()
    text = models.TextField()

    def __str__(self):
        return self.text
        
        