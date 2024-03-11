from django.core.exceptions import ValidationError


def validate_zero_to_ten(value, error_class=ValidationError):
    """Проверяет, входит ли переданное число в промежуток [1, 10]."""
    if not (0 <= value <= 10):
        raise error_class('Оценка может быть только от 0 до 10 включительно')
