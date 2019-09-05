import lemon

from .models import (
    City, MapMarkCoords, Partner, Number,
    AssetImage, Location, Concept, Plan,
    VologdaMart, VologdaBrend, VologdaCity, 
    PhotoReport, Photo, Camera, FranchCity,
    FranchVologda, CityMart, MartBrend, FranchMart,
    CityRecipientEmail, VologdaRecipientEmail,
    VologdaMartRecipientEmail, CityMartRecipientEmail,
    CityReward, VologdaMartImage, CityMartImage
)


class ParthnerInline(lemon.StackedInline):

    model = Partner
    extra = 1


class NumberInline(lemon.StackedInline):

    model = Number
    extra = 1


class AssetImageInline(lemon.StackedInline):

    model = AssetImage
    extra = 1


class LocationInline(lemon.StackedInline):

    model = Location
    extra = 1


class ConceptInline(lemon.StackedInline):

    model = Concept
    extra = 1


class PlanInline(lemon.StackedInline):

    model = Plan
    extra = 1


class MapMarkCoordsInline(lemon.StackedInline):

    model = MapMarkCoords
    extra = 1


class CameraInline(lemon.StackedInline):

    model = Camera
    extra = 1


class FranchCityInline(lemon.StackedInline):

    model = FranchCity
    extra = 5
    markup_fields = ['description']


class CityRecipientEmailInline(lemon.StackedInline):

    model = CityRecipientEmail


class CityRewardInline(lemon.StackedInline):

    model = CityReward
    markup_fields = ['text']


class CityAdmin(lemon.ModelAdmin):

    list_display = ['city', 'slug', 'weight', 'is_active']
    list_editable = ['weight', 'is_active']
    inlines = [
        ParthnerInline, NumberInline, AssetImageInline, LocationInline,
        ConceptInline, PlanInline, MapMarkCoordsInline, CameraInline,
        FranchCityInline, CityRecipientEmailInline, CityRewardInline
    ]
    tabs = True
    prepopulated_fields = {"slug": ("city",)}
    markup_fields = [
        'peview', 'text', 'text2', 'text3', 'text4', 'text5',
        'video_text', 'franch_text', 'list_text', 'peview_2'
    ]


class VologdaBrendInline(lemon.StackedInline):

    model = VologdaBrend
    extra = 1


class FranchVologdaInline(lemon.StackedInline):

    model = FranchVologda
    extra = 5
    markup_fields = ['description']


class VologdaMartRecipientEmailInline(lemon.StackedInline):

    model = VologdaMartRecipientEmail


class VologdaMartImageInline(lemon.StackedInline):

    model = VologdaMartImage


class VologdaMartAdmin(lemon.ModelAdmin):

    list_display = ['title', 'weight']
    list_editable = ['weight']
    markup_fields = ['text', 'franch_text']
    inlines = [VologdaMartImageInline, VologdaBrendInline, FranchVologdaInline, VologdaMartRecipientEmailInline]
    tabs = True


class VologdaRecipientEmailInline(lemon.StackedInline):

    model = VologdaRecipientEmail


class VologdaCityAdmin(lemon.ModelAdmin):

    markup_fields = ['text', 'preview']
    inlines = [VologdaRecipientEmailInline]
    tabs = True


class PhotoInline(lemon.StackedInline):

    model = Photo
    extra = 3


class PhotoReportAdmin(lemon.ModelAdmin):

    list_display = ['title', 'city', 'publication_date']
    list_filter = ['city']
    inlines = [PhotoInline]


class MartBrendInline(lemon.StackedInline):

    model = MartBrend
    extra = 3


class FranchMartInline(lemon.StackedInline):

    model = FranchMart
    extra = 3
    markup_fields = ['description']


class CityMartRecipientEmailInline(lemon.StackedInline):

    model = CityMartRecipientEmail


class CityMartImageInline(lemon.StackedInline):

    model = CityMartImage


class CityMartAdmin(lemon.ModelAdmin):

    list_display = ['title', 'city', 'weight']
    list_filter = ['city']
    list_editable = ['weight']
    markup_fields = ['text', 'franch_text']
    inlines = [CityMartImageInline, MartBrendInline, FranchMartInline, CityMartRecipientEmailInline]
    tabs = True


lemon.site.register(City, CityAdmin)
lemon.site.register(VologdaMart, VologdaMartAdmin)
lemon.site.register(VologdaCity, VologdaCityAdmin)
lemon.site.register(PhotoReport, PhotoReportAdmin)
lemon.site.register(CityMart, CityMartAdmin)
