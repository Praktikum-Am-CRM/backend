from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()


class UserTestCase(TestCase):
    def setUp(self) -> None:
        self.user_last_name = "Mask"
        self.user_first_name = "Ilon"
        self.user_middle_name = "Ivanovich"
        self.user_full_name = "Mask Ilon Ivanovich"
        self.username = "IlonMask"
        self.user = User.objects.create_user(
            username="IlonMask",
            email="IlonMask@example.com",
            first_name="Ilon",
            last_name="Mask",
            middle_name="Ivanovich",
            profession="Web Designer",
        )
        self.user2 = "Tim Cook Apple"
        self.user2 = User.objects.create_user(
            username="TimCook",
            email="tim@apple.com",
            first_name="Tim",
            last_name="Cook",
            middle_name="Sergeevich",
            profession="Developer",
        )
        self.amount_of_users = 2

    def test_get_full_name(self):
        self.assertEqual(
            self.user.get_full_name(),
            self.user_full_name,
            "Метод get_full_name выдал неверный результат",
        )

    def test_str(self):
        self.assertEqual(
            self.user.__str__(),
            self.user_full_name,
            "Метод __str__ выдал неверный результат",
        )

    def test_user_creation(self):
        """Проверка корректности созданных пользовательских данных.."""
        user_from_db = User.objects.get(username=self.username)

        self.assertEqual(user_from_db.email, f"{self.username}@example.com")
        self.assertEqual(
            user_from_db.last_name, self.user_last_name, "Неверная Фамилия"
        )
        self.assertEqual(
            user_from_db.first_name, self.user_first_name, "Неверное имя"
        )
        self.assertEqual(
            user_from_db.middle_name,
            self.user_middle_name,
            "Неверное отчество",
        )
