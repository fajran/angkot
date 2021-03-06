from django.conf.urls import patterns, url

urlpatterns = patterns('angkot.route.views',
    url(r'^$', 'index', name='route_index'),
    url(r'^submission-list.json$', 'submission_list', name='route_submission_list'),
    url(r'^province-list.js$', 'province_list_js', name='route_province_list_js'),
    url(r'^province-list.json$', 'province_list', name='route_province_list'),
    url(r'^transportation-list.json$', 'transportation_list', name='route_transportation_list'),
    url(r'^transportation/(?P<tid>\d+)/$',
        'transportation_data_save', name='route_transportation_data_save'),
    url(r'^transportation/(?P<tid>\d+)\.json$',
        'transportation_data', name='route_transportation_data'),
)

