from django.contrib import admin

from .models import (
    Activity,
    Ambassador,
    AmbassadorActivity,
    AmbassadorGoal,
    AmbassadorStatus,
    AmbassadorStatusHistory,
    Goal,
)

admin.site.register(Ambassador)
admin.site.register(AmbassadorGoal)
admin.site.register(AmbassadorStatus)
admin.site.register(AmbassadorStatusHistory)
admin.site.register(AmbassadorActivity)
admin.site.register(Goal)
admin.site.register(Activity)
