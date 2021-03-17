from django.urls import path
from . import views

urlpatterns = [
    path('get-articles/<int:count>', views.ArticlesView.as_view()),
    path('get-articles/', views.ArticlesView.as_view()),
    path('get-article/<int:id>', views.ArticleView.as_view()),
    path('get-comments/<int:article_id>', views.CommentsView.as_view()),
    path('post-comment/', views.AddCommentView.as_view()),
    path('get-categories/', views.CategoriesView.as_view()),
    path('get-category/<int:category_id>/<int:page>', views.CategoryView.as_view()),
    path('about-us/', views.AboutUsView.as_view()),
    path('subscribe/', views.SubscribeView.as_view()),
]
