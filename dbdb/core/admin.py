# django imports
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# local imports
from .models import *


# inlines

class FeatureOptionsInlines(admin.StackedInline):
    model = FeatureOption
    extra = 0

class SystemACLInlines(admin.StackedInline):
    model = SystemACL
    extra = 0
    exclude=('created', 'modified')

# model admins

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff', 'date_joined', 'last_login')
    readonly_fields=('date_joined', 'last_login')
    inlines = [SystemACLInlines]

class FeatureAdmin(admin.ModelAdmin):
    inlines = [FeatureOptionsInlines]

class FeatureOptionAdmin(admin.ModelAdmin):
    list_filter = ['feature']
    list_display = ('value', 'feature')
    search_fields = ('value', )

class SystemAdmin(admin.ModelAdmin):
    empty_value_display = 'unknown'
    list_display = ('name', 'created', 'modified', 'ver', 'view_count')
    list_filter = ['created', 'modified' ]
    search_fields = ('name', )
    readonly_fields=('view_count', 'created', 'modified' )

class SystemVersionAdmin(admin.ModelAdmin):
    empty_value_display = 'unknown'
    list_display = ('system', 'ver', 'creator', 'created')
    list_filter = ['created', 'system']
    readonly_fields=('ver', 'system')
    ordering = ('-created',)
    exclude = ('system', )

class SystemACLAdmin(admin.ModelAdmin):
    list_display = ('system', 'user', 'created', 'modified')
    list_filter = ['created']
    readonly_fields=('created', 'modified')

class SystemRecommendationAdmin(admin.ModelAdmin):
    list_display = ('system', 'recommendation', 'score', 'created')
    list_filter = ['created', 'system']
    readonly_fields=('created', )
    ordering = ('-created',)

class SystemSearchTextAdmin(admin.ModelAdmin):
    list_display = ('system', 'search_text', 'created')
    readonly_fields = ('created',)
    ordering = ('-created',)

class SystemVisitAdmin(admin.ModelAdmin):
    list_display = ('system', 'ip_address', 'created')
    list_filter = ['created', 'system']
    readonly_fields=('created',)
    ordering = ('-created',)
    
class LicenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'url')
    ordering = ('name',)
    
class OperatingSystemAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'url')
    ordering = ('name',)
    
class ProgrammingLanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'url')
    ordering = ('name',)


# registrations
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.register(Feature, FeatureAdmin)
admin.site.register(FeatureOption, FeatureOptionAdmin)
admin.site.register(License, LicenseAdmin)
admin.site.register(OperatingSystem, OperatingSystemAdmin)
admin.site.register(ProgrammingLanguage, ProgrammingLanguageAdmin)
admin.site.register(Tag)
admin.site.register(ProjectType)
admin.site.register(Publication)
#admin.site.register(SuggestedSystem)
admin.site.register(System, SystemAdmin)
admin.site.register(SystemFeature)
admin.site.register(SystemVisit, SystemVisitAdmin)
admin.site.register(SystemRecommendation, SystemRecommendationAdmin)
admin.site.register(SystemSearchText, SystemSearchTextAdmin)
admin.site.register(SystemACL, SystemACLAdmin)
admin.site.register(SystemVersion, SystemVersionAdmin)
admin.site.register(SystemVersionMetadata)
