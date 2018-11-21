from django.urls import path
from .views import SnippetList, SnippetDetail, UserList, UserDetail, api_root, SnippetHighlight

urlpatterns = [
    path('snippetlist/',SnippetList.as_view(),name='snippet-list'),
    path('snippetdetail/<int:pk>',SnippetDetail.as_view(),name = 'snippet-detail'),

    path('snippets/<int:pk>/highlight/',
         SnippetHighlight.as_view(), name='snippet-highlight'),

    path('users/',UserList.as_view(), name='user-list'),
    path('users/<int:pk>',UserDetail.as_view(), name = 'user-detail'),
    path('',api_root)
]