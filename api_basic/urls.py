from django.urls import path
from .views import article_list, article_detail, ArticleAPIView, ArticleDetailAPIView

urlpatterns = [
    # Function based view path for article list
    # path('article/', article_list),

    # Class based view path for article list
    path('article/', ArticleAPIView.as_view()),

    # Function based view path for article detail
    # path('article/<int:pk>/', article_detail),

    # Class based view path for article detail
    path('article/<int:pk>/', ArticleDetailAPIView.as_view())
]