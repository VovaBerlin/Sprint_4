# qa_python
1. Добавляем 2 новых книги в словарь books_genre и проверяем, что длина словаря get_books_genre равняется 2.
2. Добавляем книгу в словарь books_genre и проверяем, что книга добавилась без жанра.
3. Добавляем книгу в словарь books_genre и добавляем жанр, с помощью поиска по ключу в словаре books_genre, проверяем, что значение(жанр) добавилось.
4. Добавляем книгу в словарь books_genre, добавляем жанр к книге, который отсутствует в списке genre. Проверяем, что жанр к книге не добавился.
5. С помощью параметризации добавляем 2 книги и жанр к каждой книге, проверяем, с помощью метода get_book_genre, что книге соответствует корректный жанр.
6. Добавляем 2 книги в словарь books_genre с одинаковыми жанрами, с помощью get_books_with_specific_genre, проверяем, что выводятся список книг у которых одинаковый жанр.
7. Добавляем 2 книги с жанрами в словарь books_genre и проверяем, что при вызове метода get_books_genre выводится словарь, где ключ - книга, значение - жанр.
8. С помощью параметризации добавляем 3 книги с жанрами без возрастного ограничения и проверяем, что книги добавились в список для детей get_books_for_children.
9. С помощью параметризации добавляем 2 книги с жанром с возрастным ограничением и проверяем, что книги не добавились в список для детей get_books_for_children.
10. Добавляем 2 книги в словарь books_genre, затем добавляем эти книги в избранное (в словарь favorites) с помощью метода add_book_in_favorites. Проверяем, что книги успешно добавились в избранное.
11. Добавляем книгу в словарь books_genre, затем добавляем эту книгу в favorites, после чего удаляем книгу из favorites с помощью метода delete_book_from_favorites. Проверяем, что книга удалилась из списка favorites.
12. Добавляем книгу в словарь books_genre, затем добавляем в favorites, после чего вызывае метод get_list_of_favorites_books, и проверяем что выводится список с избранными книгами.