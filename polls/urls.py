from django.urls import path

from .views import (PollListGeneric,
                    PollDetailGeneric,
                    CreateVote,
                    ChoiceList,
                    PollMainListGeneric,
                    VoteDetailGeneric,
                    )

urlpatterns = [
    # Получения списка всех опросов
    path('list', PollMainListGeneric.as_view(), name="list"),
    # Получения списка всех вопросов в опросах
    path('polls', PollListGeneric.as_view(), name="polls_list"),
    # Информация о конкретном вопросе, где <int:pk> - ID вопроса
    path('polls/<int:pk>', PollDetailGeneric.as_view(), name="polls_detail"),
    # Голосование
    path("vote", CreateVote.as_view(), name="vote"),
    # Инфорамция по голосам пользователся, где <str:pk> - session_key клиента
    path("vote/<str:pk>", VoteDetailGeneric.as_view(), name='vote_detail'),
    # Получения списка всех возможных выборов
    path("choices", ChoiceList.as_view(), name="choices"),
]
