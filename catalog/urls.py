from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('book/', views.BookListView.as_view(), name='books'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),

    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path(r'borrowed/', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),  # Added for challenge

    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),

    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete', views.AuthorDelete.as_view(), name='author_delete'),

    path('book/create/', views.BookCreate.as_view(), name='book_create'),
    path('book/<int:pk>/update', views.BookUpdate.as_view(), name='book_update'),
    path('book/<int:pk>/delete', views.BookDelete.as_view(), name='book_delete'),

]

# from django.urls import path
# from . import views
# from django.conf.urls import url
#
# urlpatterns = [
#     url(r'^$', views.index, name='index'),
#     url(r'^books/$', views.BookListView.as_view(), name='books'),
#     url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
# ]