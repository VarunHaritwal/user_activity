from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, ActivityPeriodCreateView

urlpatterns = {
	url(r'^usertask/$', CreateView.as_view(), name="create"),
	url(r'^useractivity/$', ActivityPeriodCreateView.as_view(), name="activity"),
}

urlpatterns = format_suffix_patterns(urlpatterns)