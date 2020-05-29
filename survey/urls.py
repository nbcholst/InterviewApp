from django.urls import path
from . import views
from .views import (
    SurveyListView,
    SurveyDetailView,
    UserSurveyListView,
    SurveyCreateView,
    SurveyUpdateView,
    SurveyDeleteView,
    SurveyShareView,
    QuestionCreateView,
    QuestionDeleteView,
    QuestionRecordView,
    QuestionRecordSubmitView
                    )

urlpatterns = [
    path('', SurveyListView.as_view(), name='survey-home'),
    path('survey/<int:pk>', SurveyDetailView.as_view(), name='survey-detail'),
    path('user/<str:username>', UserSurveyListView.as_view(), name='user-surveys'),
    path('survey/new/', SurveyCreateView.as_view(), name='survey-create'),
    path('survey/<int:pk>/update/', SurveyUpdateView.as_view(), name='survey-update'),
    path('survey/<int:pk>/delete/', SurveyDeleteView.as_view(), name='survey-delete'),
    path('survey/<int:pk>/share/', SurveyShareView.as_view(), name='survey-share'),
    path('survey/<int:pk>/new_question/', QuestionCreateView.as_view(), name='survey-question-add'),
    path('survey/<int:pk>/delete_question/', QuestionDeleteView.as_view(), name='survey-question-delete'),
    path('survey/<int:pk>/record_question/', QuestionRecordView.as_view(), name='survey-question-record'),
    path('survey/<int:pk>/record_submit_question/', views.QuestionRecordSubmitView, name='survey-question-submit-record')
]
