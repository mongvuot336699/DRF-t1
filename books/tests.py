from django.test import TestCase
from django.urls import reverse

# Create your tests here.
from .models import Book

class BookTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title ="A good title",
            subtitle = "Hello world",
            author = "Tom Crui",
            isbn = '123123',
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, "A good title")
        self.assertEqual(self.book.subtitle, "Hello world")
        self.assertEqual(self.book.author, "Tom Crui")
        self.assertEqual(self.book.isbn, "123123")

    def test_book_listview(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "excellent subtitle")
        self.assertTemplateUsed(response, 'books/book_list.html')
