from django.urls import path
from .views import ListAds, DetailAds, DeleteAds, CreateAds, UpdateAds, StatisticView, AdsSearch

urlpatterns: list = [
    path("", ListAds.as_view(), name="list-ads"),
    path("<int:pk>/", DetailAds.as_view(), name="detail-ads"),
    path("<int:pk>/delete/", DeleteAds.as_view(), name="delete-ads"),
    path("<int:pk>/edit/", UpdateAds.as_view(), name="update-ads"),
    path("new/", CreateAds.as_view(), name="create-ads"),
    path("statistic", StatisticView.as_view(), name="statistic"),
    path("search/", AdsSearch.as_view(), name="search-ads"),
]
