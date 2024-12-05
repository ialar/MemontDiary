from django.test import TestCase
from django.urls import reverse

from diary.models import Entry
from users.models import User


class EntryTestCase(TestCase):
    def setUp(self):
        # Создаем пользователя и устанавливаем пароль
        self.user = User.objects.create(email="test@test.com")
        self.user.set_password("testpassword")
        self.user.is_active = True
        self.user.save()

        # Аутентификация пользователя
        self.client.login(email="test@test.com", password="testpassword")

        # Создаем тестовую запись, принадлежащую пользователю
        self.entry = Entry.objects.create(title='Test Entry 1', text='This is a test entry.', owner=self.user)

    def test_user_authentication(self):
        # Проверяем логин
        logged_in = self.client.login(email="test@test.com", password="testpassword")
        self.assertTrue(logged_in)

    def test_index_view(self):
        # Проверяем главную страницу
        response = self.client.get(reverse('diary:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'diary/index.html')

    def test_entry_list_view(self):
        # Выполняем запрос к представлению
        response = self.client.get(reverse('diary:entry_list'))

        # Проверяем код ответа
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'diary/entry_list.html')
        self.assertContains(response, 'Test Entry 1')  # Проверяем, что запись отображается

    def test_entry_list_view_empty(self):
        # Логинимся с новым пользователем, у которого нет записей
        self.client.logout()  # Выход из системы
        new_user = User.objects.create(email="newuser@test.com")
        new_user.set_password("newpassword")
        new_user.is_active = True
        new_user.save()
        self.client.login(email="newuser@test.com", password="newpassword")

        # Выполняем запрос к представлению
        response = self.client.get(reverse('diary:entry_list'))

        # Проверяем код ответа
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'diary/entry_list.html')
        self.assertContains(response, "No entries yet")  # Проверяем, что отображается сообщение о пустом списке

    def test_entry_create_view(self):
        # Создаем запись
        response = self.client.post(reverse('diary:entry_create'), {
            'title': 'New Entry',
            'text': 'This is a new entry.',
            'is_public': True
        })

        # Проверяем, что перенаправляет на страницу списка записей
        self.assertRedirects(response, reverse('diary:entry_list'))

        # Проверяем, что запись была создана
        self.assertTrue(Entry.objects.filter(title='New Entry').exists())

    def test_entry_detail_view(self):
        # Смотрим запись
        response = self.client.get(reverse('diary:entry_detail', args=[self.entry.pk]))

        # Проверяем, что код ответа 200
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'diary/entry_detail.html')
        self.assertContains(response, self.entry.title)  # Проверяем, что заголовок записи отображается

    def test_entry_update_view(self):
        # Изменяем запись
        response = self.client.post(reverse('diary:entry_update', args=[self.entry.pk]), {
            'title': 'Updated Entry',
            'text': 'This is an updated entry.',
            'is_public': True
        })

        # Проверяем, что перенаправляет на страницу списка записей
        self.assertRedirects(response, reverse('diary:entry_list'))

        # Проверяем, что запись была обновлена
        self.entry.refresh_from_db()  # Обновляем объект записи из базы данных
        self.assertEqual(self.entry.title, 'Updated Entry')

    def test_entry_delete_view(self):
        # Удаляем запись
        response = self.client.post(reverse('diary:entry_delete', args=[self.entry.pk]))

        # Проверяем, что перенаправляет на страницу списка записей
        self.assertRedirects(response, reverse('diary:entry_list'))

        # Проверяем, что запись была удалена
        self.assertFalse(Entry.objects.filter(pk=self.entry.pk).exists())

    def test_entry_search_view(self):
        # Создаем дополнительную запись для поиска
        Entry.objects.create(title='Searchable Entry', text='This entry is searchable.', owner=self.user)

        response = self.client.get(reverse('diary:entry_search'), {'query': 'Searchable'})

        # Проверяем, что код ответа 200
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'diary/search_entries_list.html')
        self.assertContains(response, 'Searchable')  # Проверяем, что запись отображается в результатах поиска
