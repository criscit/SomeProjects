from unittest import TestCase
from functools import cmp_to_key  # see https://docs.python.org/3/howto/sorting.html#the-old-way-using-the-cmp-parameter

from book_comparator import compare_books_by_price, compare_books_by_author_and_title_and_year
from book import Book


class TestBookComparator(TestCase):
    def setUp(self):
        self.algo_books = [
            Book("Грокаем алгоритмы", "Адитья Бхаргава", 2017, 500.0),
            Book("Совершенный алгоритм. Основы", "Тим Рафгарден", 2019, 1500.0),
            Book("Совершенный алгоритм. Графовые алгоритмы и структуры данных", "Рафгарден Тим", 2019, 999.0),
            Book("Алгоритмы для начинающих", "Луридас Панос", 2018, 499.0),
            Book("Грокаем алгоритмы", "Адитья Бхаргава", 2021, 700.0),
            Book("Введение в анализ алгоритмов", "Майкл Солтис", 2019, 500.0),
            Book("Алгоритмы: разработка и применение", "Джон Клейнберг", 2016, 100.0)
        ]

    def test_sort_books_by_price(self):
        expected_list = [
            Book("Алгоритмы: разработка и применение", "Джон Клейнберг", 2016, 100.0),
            Book("Алгоритмы для начинающих", "Луридас Панос", 2018, 499.0),
            Book("Грокаем алгоритмы", "Адитья Бхаргава", 2017, 500.0),
            Book("Введение в анализ алгоритмов", "Майкл Солтис", 2019, 500.0),
            Book("Грокаем алгоритмы", "Адитья Бхаргава", 2021, 700.0),
            Book("Совершенный алгоритм. Графовые алгоритмы и структуры данных", "Рафгарден Тим", 2019, 999.0),
            Book("Совершенный алгоритм. Основы", "Тим Рафгарден", 2019, 1500.0),
        ]

        sorted_books = sorted(self.algo_books, key=cmp_to_key(compare_books_by_price))

        self.assertListEqual(sorted_books, expected_list, sorted_books)

    def test_sort_books_by_author_title_year(self):
        expected_list = [
            Book("Грокаем алгоритмы", "Адитья Бхаргава", 2017, 500.0),
            Book("Грокаем алгоритмы", "Адитья Бхаргава", 2021, 700.0),
            Book("Алгоритмы: разработка и применение", "Джон Клейнберг", 2016, 100.0),
            Book("Алгоритмы для начинающих", "Луридас Панос", 2018, 499.0),
            Book("Введение в анализ алгоритмов", "Майкл Солтис", 2019, 500.0),
            Book("Совершенный алгоритм. Графовые алгоритмы и структуры данных", "Рафгарден Тим", 2019, 999.0),
            Book("Совершенный алгоритм. Основы", "Тим Рафгарден", 2019, 1500.0),
        ]

        sorted_books = sorted(self.algo_books, key=cmp_to_key(compare_books_by_author_and_title_and_year))

        self.assertListEqual(sorted_books, expected_list, sorted_books)
