
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^home/$', views.home),
    url(r'^id/(?P<id>\d+)/', views.detail, name='id'),
    url(r'^note/new/$', views.note_new, name='note_new'),
    url(r'^ajax/edit_post/$', views.edit_post, name='note_edit'),
    url(r'^ajax/delete_post/$', views.delete_post, name='note_delete'),
    url(r'^patient/share/(?P<id>\d+)/$', views.share_patient, name='patient_share'),
    url(r'^patient/share/submit/(?P<id>\d+)/', views.submit_patient, name='patient_submit'),


]
