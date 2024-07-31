import pytest
from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_added_book_without_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Евгений Онегин')
        assert collector.books_genre['Евгений Онегин'] == ''

    def test_set_book_genre_add_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Мгла')
        collector.set_book_genre('Мгла','Ужасы')
        assert collector.books_genre['Мгла'] == 'Ужасы'

    def test_set_book_genre_wrong_genre_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Гроза')
        collector.set_book_genre('Гроза', 'Драма')
        assert collector.books_genre['Гроза'] == ''

    @pytest.mark.parametrize("book_name, genre", [["Книга 1", "Фантастика"], ["Книга 2", "Комедии"]])
    def test_get_book_genre_shows_correct_genre(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    def test_get_books_with_specific_genre_books_added(self):
        collector = BooksCollector()
        collector.add_new_book('Дубровский')
        collector.set_book_genre('Дубровский', 'Детективы')
        collector.add_new_book('Капитанская дочка')
        collector.set_book_genre('Капитанская дочка', 'Детективы')
        assert collector.get_books_with_specific_genre('Детективы') == ['Дубровский', 'Капитанская дочка']

    def test_get_books_genre_dict_success_shows(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.set_book_genre('Книга 1', 'Детективы')
        collector.add_new_book('Книга 2')
        collector.set_book_genre('Книга 2', 'Фантастика')
        assert collector.get_books_genre() == {'Книга 1': 'Детективы', 'Книга 2': 'Фантастика'}

    @pytest.mark.parametrize("book_name, genre", ([
        ["Книга 1", "Фантастика"],
        ["Книга 2", "Комедии"],
        ["Книга 3", "Мультфильмы"]
    ]))
    def test_get_books_for_children_shows_books(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        books = collector.get_books_for_children()
        assert book_name in books

    @pytest.mark.parametrize("book_name, genre", [
        ["Книга 1", "Ужасы"],
        ["Книга 2", "Детективы"],
    ])
    def test_get_books_for_children_not_show_added_books(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        books = collector.get_books_for_children()
        assert book_name not in books

    @pytest.mark.parametrize("book_name, genre", [
        ["Книга 1", "Ужасы"],
        ["Книга 2", "Детективы"]
    ])
    def test_book_in_favorites_shows_books(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.favorites

    def test_delete_book_from_favorites_book_deleted(self):
        collector = BooksCollector()
        collector.add_new_book("Властелин колец")
        collector.add_book_in_favorites("Властелин колец")
        collector.delete_book_from_favorites("Властелин колец")
        assert collector.favorites == []

    def test_get_list_of_favorites_books_show_book_in_list(self):
        collector = BooksCollector()
        collector.add_new_book("Властелин колец")
        collector.add_book_in_favorites("Властелин колец")
        assert collector.get_list_of_favorites_books() == ["Властелин колец"]
