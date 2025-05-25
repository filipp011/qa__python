class TestBooksCollector:

    def test_books_genre_defolt(self, collector):
        assert collector.books_genre == {}

    def test_favorites_defolt(self, collector):
        assert collector.favorites == []

    def test_genre_defolt(self, collector):
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    def test_genre_age_rating_defolt(self, collector):
        assert collector.genre_age_rating == ['Ужасы', 'Детективы']

    # Добавление новой книги
    def test_add_new_book(self, collector):
        collector.add_new_book('Книга для избранных')
        assert 'Книга для избранных' in collector.get_books_genre()

    # Проверка устновки книге жанра
    def test_set_book_genre(self, collector):
        collector.add_new_book('Книга для избранных')
        collector.set_book_genre('Книга для избранных', 'Фантастика')
        genre=collector.get_book_genre('Книга для избранных')
        assert genre == 'Фантастика'
    
    # Добавление новой книги в израбнное без жанра
    def test_add_new_book_in_favorites(self,collector):
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