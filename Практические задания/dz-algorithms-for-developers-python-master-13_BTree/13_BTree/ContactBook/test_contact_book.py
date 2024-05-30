from unittest import TestCase

from contact_book import ContactBook
from contact import Contact


class TestContactBook(TestCase):
    def setUp(self):
        self.contacts = (
            Contact("Adam Black", "79121231419"),
            Contact("Amanda Waller", "79126131419"),
            Contact("Jake Paul", "79121271719"),
            Contact("Ilia 1", "79121231412"),
            Contact("Ilya 2", "79121231477"),
            Contact("Ilija 3", "79121232346"),
            Contact("Jeff Dean", "79121267188"),
            Contact("Jeff King", "79121293782"),
            Contact("Jofrie King", "79123233126"),
            Contact("Liam", "79161231256"),
            Contact("Nilson", "79612131512"),
            Contact("Abaca", "79167134212"),
            Contact("Abada", "79179675480"),
            Contact("Abba", "79119123871"),
            Contact("Mother", "79128382190"),
            Contact("Monk", "79167810293"),
            Contact("Motel", "79101299291")
        )


    def test_exists(self):
        book = ContactBook()
        for c in self.contacts:
            book.add(c)

        names = ["Vladimir", "Monks", "Mo", "Nilfather", "abba", "Jeff"]
        for name in names:
            self.assertNotIn(name, book, "Name <" + name + "> found!")

        names = ["Mother", "Jeff Dean", "Jofrie King", "Liam", "Adam Black"]
        for name in names:
            self.assertIn(name, book, "Name <" + name + "> NOT found!")

    def test_count(self):
        book = ContactBook()
        for c in self.contacts:
            book.add(c)

        self.assertEqual(book.count_starts_with("Jefy"), 0)
        self.assertEqual(book.count_starts_with("Jeff"), 2)
        self.assertEqual(book.count_starts_with("I"), 3)
        self.assertEqual(book.count_starts_with("Il"), 3)
        self.assertEqual(book.count_starts_with("Ili"), 2)
        self.assertEqual(book.count_starts_with("Ilia"), 1)
        self.assertEqual(book.count_starts_with(""), self.contacts.length)
        self.assertEqual(book.count_starts_with("M"), 3)
        self.assertEqual(book.count_starts_with("Mo"), 3)
        self.assertEqual(book.count_starts_with("Mot"), 2)
        self.assertEqual(book.count_starts_with("Moth"), 1)

    def test_starts_with(self):
        book = ContactBook()
        for c in self.contacts:
            book.add(c)

        self.assertEqual(book.starts_with("Moth")[0].name, "Mother")
        self.assertEqual(book.starts_with("Jeff D")[0].name, "Jeff Dean")
