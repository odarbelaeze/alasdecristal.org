from django.contrib import admin

from .models import Contact
from .models import Hint
from .models import HintGroup
from .models import NewsletterSubscription
from .models import Product
from .models import ProductImage
from .models import Quote
from .models import QuoteLine
from .models import Team
from .models import TeamMember


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


class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    model = NewsletterSubscription


class ContactAdmin(admin.ModelAdmin):
    model = Contact


class QuoteAdmin(admin.ModelAdmin):
    model = Quote
    inlines = [QuoteLineInline]


admin.site.register(Team, TeamAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(HintGroup, HintGroupAdmin)
admin.site.register(NewsletterSubscription, NewsletterSubscriptionAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Quote, QuoteAdmin)
