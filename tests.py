import pytest
from main import BooksCollector



class TestBooksCollector:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.collector = BooksCollector()

    def test_add_new_book_add_two_books(self):
        self.collector.add_new_book('Гордость и предубеждение и зомби')
        self.collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(self.collector.get_books_genre()) == 2

    def test_add_new_book_added_book_without_genre(self):
        self.collector.add_new_book('Евгений Онегин')
        assert self.collector.books_genre['Евгений Онегин'] == ''

    def test_set_book_genre_add_genre(self):
        self.collector.add_new_book('Мгла')
        self.collector.set_book_genre('Мгла','Ужасы')
        assert self.collector.books_genre['Мгла'] == 'Ужасы'

    def test_set_book_genre_wrong_genre_not_added(self):
        self.collector.add_new_book('Гроза')
        self.collector.set_book_genre('Гроза', 'Драма')
        assert self.collector.books_genre['Гроза'] == ''

    @pytest.mark.parametrize("book_name, genre", [
        ["К", "Фантастика"],
        ["Книга 2", "Комедии"],
        ["КнигаКнигаКнигаКнигаКнигаКнигаКнигаКнига", "Ужасы"]
    ])
    def test_get_book_genre_shows_correct_genre(self, book_name, genre):
        self.collector.add_new_book(book_name)
        self.collector.set_book_genre(book_name, genre)
        assert self.collector.get_book_genre(book_name) == genre

    def test_get_books_with_specific_genre_books_added(self):
        self.collector.add_new_book('Дубровский')
        self.collector.set_book_genre('Дубровский', 'Детективы')
        self.collector.add_new_book('Капитанская дочка')
        self.collector.set_book_genre('Капитанская дочка', 'Детективы')
        assert self.collector.get_books_with_specific_genre('Детективы') == ['Дубровский', 'Капитанская дочка']

    def test_get_books_genre_dict_success_shows(self):
        self.collector.add_new_book('Книга 1')
        self.collector.set_book_genre('Книга 1', 'Детективы')
        self.collector.add_new_book('Книга 2')
        self.collector.set_book_genre('Книга 2', 'Фантастика')
        assert self.collector.get_books_genre() == {'Книга 1': 'Детективы', 'Книга 2': 'Фантастика'}

    @pytest.mark.parametrize("book_name, genre", [
        ["Книга 1", "Фантастика"],
        ["Книга 2", "Комедии"],
        ["Книга 3", "Мультфильмы"]
    ])
    def test_get_books_for_children_shows_books(self, book_name, genre):
        self.collector.add_new_book(book_name)
        self.collector.set_book_genre(book_name, genre)
        books = self.collector.get_books_for_children()
        assert book_name in books

    @pytest.mark.parametrize("book_name, genre", [
        ["Книга 1", "Ужасы"],
        ["Книга 2", "Детективы"],
    ])
    def test_get_books_for_children_not_show_added_books(self, book_name, genre):
        self.collector.add_new_book(book_name)
        self.collector.set_book_genre(book_name, genre)
        books = self.collector.get_books_for_children()
        assert book_name not in books

    @pytest.mark.parametrize("book_name, genre", [
        ["Книга 1", "Ужасы"],
        ["Книга 2", "Детективы"]
    ])
    def test_book_in_favorites_shows_books(self, book_name, genre):
        self.collector.add_new_book(book_name)
        self.collector.set_book_genre(book_name, genre)
        self.collector.add_book_in_favorites(book_name)
        assert book_name in self.collector.favorites

    def test_delete_book_from_favorites_book_deleted(self):
        self.collector.add_new_book("Властелин колец")
        self.collector.add_book_in_favorites("Властелин колец")
        self.collector.delete_book_from_favorites("Властелин колец")
        assert self.collector.favorites == []

    def test_get_list_of_favorites_books_show_book_in_list(self):
        self.collector.add_new_book("Властелин колец")
        self.collector.add_book_in_favorites("Властелин колец")
        assert self.collector.get_list_of_favorites_books() == ["Властелин колец"]
