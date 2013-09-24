# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from ecommerce.models import Team 
from ecommerce.models import TeamMember 
from ecommerce.models import Product 
from ecommerce.models import ProductImage 
from ecommerce.models import HintGroup 
from ecommerce.models import Hint 
from ecommerce.models import NewsletterSuscription 
from ecommerce.models import Contact 
from ecommerce.models import Quote 
from ecommerce.models import QuoteLine 

class TeamMemberInline(admin.TabularInline):
    model = TeamMember
    extra = 2

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 2

class HintInline(admin.TabularInline):
    model = Hint
    extra = 2

class QuoteLineInline(admin.TabularInline):
    model = QuoteLine
    extra = 2


class TeamAdmin(admin.ModelAdmin):
    model = Team
    inlines = [TeamMemberInline]

class ProductAdmin(admin.ModelAdmin):
    model = Product
    inlines = [ProductImageInline]

class HintGroupAdmin(admin.ModelAdmin):
    model = HintGroup
    inlines = [HintInline]

class NewsletterSuscriptionAdmin(admin.ModelAdmin):
    model = NewsletterSuscription

class ContactAdmin(admin.ModelAdmin):
    model = Contact

class QuoteAdmin(admin.ModelAdmin):
    model = Quote
    inlines = [QuoteLineInline]


admin.site.register(Team, TeamAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(HintGroup, HintGroupAdmin)
admin.site.register(NewsletterSuscription, NewsletterSuscriptionAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Quote, QuoteAdmin)
