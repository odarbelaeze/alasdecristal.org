from django.utils.translation import ugettext as _

from django.db import models


class Team(models.Model):
    class Meta:
        verbose_name = _('Team')
        verbose_name_plural = _('Teams')

    def __str__(self):
        return '%s' % self.name

    name = models.CharField(max_length=250, verbose_name='Nombre')


class TeamMember(models.Model):
    class Meta:
        verbose_name = _('Miembro del Equipo')
        verbose_name_plural = _('Miembros del Equipo')

    def __str__(self):
        return '%s' % self.name

    team = models.ForeignKey(Team)
    name = models.CharField(max_length=250, verbose_name='Nombre')
    bio = models.TextField()
    image = models.ImageField(upload_to='team/images')


class Product(models.Model):

    class Meta:
        verbose_name = _('Producto')
        verbose_name_plural = _('Productos')

    def __str__(self):
        return '%s' % self.name

    id = models.SlugField(unique=True, primary_key=True)
    name = models.CharField(max_length=250, verbose_name='Nombre')
    short_description = models.TextField(verbose_name='Descirpción')
    thumbnail = models.ImageField(
        upload_to='products/thumbnails',
        verbose_name='Icono'
    )
    featured = models.BooleanField(
        verbose_name='En promoción, el que lleve, el que escoja'
    )


class ProductImage(models.Model):

    class Meta:
        verbose_name = _('ProductImage')
        verbose_name_plural = _('ProductImages')

    def __str__(self):
        return '%s' % self.title

    product = models.ForeignKey(Product)
    image = models.ImageField(
        upload_to='products/images',
        verbose_name='Imagen'
    )
    title = models.CharField(max_length=250, verbose_name='Título')
    description = models.TextField(verbose_name='Descirpción')
    caption_on = models.BooleanField(verbose_name='Activar caption')


class HintGroup(models.Model):

    class Meta:
        verbose_name = _('Grupo de recomendaciones')
        verbose_name_plural = _('Grupos de recomendaciones')

    def __str__(self):
        return self.title

    title = models.CharField(max_length=250)


class Hint(models.Model):
    class Meta:
        verbose_name = _('Recomendación')
        verbose_name_plural = _('Recomendacións')

    def __str__(self):
        return self.text

    hint_group = models.ForeignKey(HintGroup)
    text = models.TextField()


class NewsletterSuscription(models.Model):
    class Meta:
        verbose_name = _('Suscripción al Newsletter')
        verbose_name_plural = _('Suscripciónes al Newsletter')

    def __str__(self):
        return '%s' % self.email

    date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha')
    name = models.CharField(max_length=250, verbose_name='Nombre')
    email = models.EmailField(
        verbose_name='Email',
        unique=True)


class Contact(models.Model):
    class Meta:
        verbose_name = _('Contacto')
        verbose_name_plural = _('Contactos')

    def __str__(self):
        return '%s' % self.subject

    date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha')
    name = models.CharField(max_length=250, verbose_name='Nombre')
    subject = models.CharField(max_length=250, verbose_name='Asunto')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(blank=True, null=True,
                             max_length=250, verbose_name='Teléfono')
    city = models.CharField(blank=True, null=True,
                            max_length=250, verbose_name='Ciudad')
    message = models.TextField(verbose_name='Mensaje')


class Quote(models.Model):
    class Meta:
        verbose_name = _('Cotización')
        verbose_name_plural = _('Cotizaciónes')

    def __str__(self):
        return '%s' % self.name

    date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha')
    name = models.CharField(max_length=250, verbose_name='Nombre')
    subject = models.CharField(max_length=250, verbose_name='Asunto')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(blank=True, null=True,
                             max_length=250, verbose_name='Teléfono')
    city = models.CharField(blank=True, null=True,
                            max_length=250, verbose_name='Ciudad')


class QuoteLine(models.Model):

    class Meta:
        verbose_name = _('QuoteLine')
        verbose_name_plural = _('QuoteLines')

    def __str__(self):
        return '%s' % self.product

    quote = models.ForeignKey(Quote)
    product = models.CharField(max_length=250, verbose_name='Producto')
    quantity = models.IntegerField(verbose_name='Cantidad')
