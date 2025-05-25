import pytest
class TestBooksCollector:

    def test_books_genre_defolt(self, collector):
        assert collector.books_genre == {}

    def test_favorites_defolt(self, collector):
        assert collector.favorites == []

    def test_genre_defolt(self, collector):
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    def test_genre_age_rating_defolt(self, collector):
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    # Проверка устновки книге жанра
    def test_set_book_genre(self, collector):
        collector.add_new_book('Книга для избранных')
        collector.set_book_genre('Книга для избранных', 'Фантастика')
        collector.get_book_genre('Книга для избранных')
        assert collector.get_book_genre('Книга для избранных') == 'Фантастика'
    
    # Получение списка Изрбанных книг
    def test_get_list_of_favorites_books(self,collector):
        collector.add_new_book('Книга для избранных')
        collector.add_book_in_favorites('Книга для избранных')
        favorites = collector.get_list_of_favorites_books()
        assert ('Книга для избранных') in favorites

    # Удаление книги из избранного без жанра
    def test_delete_book_from_favorites(self,collector):
        collector.add_new_book('Книга для избранных',)
        collector.add_book_in_favorites('Книга для избранных')
        favorites = collector.delete_book_from_favorites
        assert "Книга для избранных" is not favorites

    # Выводим список книг с определённым жанром
    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book('Книга для избранных')
        collector.set_book_genre('Книга для избранных', 'Фантастика')
        result = collector.get_books_with_specific_genre('Фантастика')
        assert result == ['Книга для избранных']


    @pytest.mark.parametrize(
        "books_data, expected_result",
        [
            (
                [
                    ('Книга для избранных', 'Фантастика'),
                    ('Оно', 'Ужасы'),
                    ('Том и Джерри', 'Мультфильмы')
                ],
                ['Книга для избранных', 'Том и Джерри']
            )
        ]
    )
    def test_get_books_for_children(self, collector, books_data, expected_result):
        for name, genre in books_data:
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)
        assert collector.get_books_for_children() == expected_result

    




