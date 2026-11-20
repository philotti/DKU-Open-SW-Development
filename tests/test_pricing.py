import pytest

from orderlab.pricing import final_total, subtotal


def test_subtotal_normal():
    # Arrange: 입력 준비
    price = 10_000
    quantity = 2
    # Act: 테스트 대상 실행
    result = subtotal(price, quantity)
    # Assert: 기대 결과 검증
    assert result == 20_000


def test_subtotal_zero_price():
    # Arrange
    price = 0
    quantity = 3
    # Act
    result = subtotal(price, quantity)
    # Assert
    assert result == 0


def test_subtotal_negative_price():
    # Arrange
    price = -100
    quantity = 2
    # Act & Assert: 음수 입력에서 ValueError가 발생하는지 확인
    with pytest.raises(ValueError):
        subtotal(price, quantity)


def test_discount_below_zero():
    with pytest.raises(ValueError):
        final_total(10_000, 2, -1)


def test_discount_over_100():
    with pytest.raises(ValueError, match="invalid discount"):
        final_total(10_000, 2, 101)


@pytest.mark.parametrize(
    "price, qty, discount, expected",
    [
        (10_000, 2, 0, 23_000),
        (49_999, 1, 0, 52_999),
        (50_000, 1, 0, 50_000),
        (50_001, 1, 0, 50_001),
        (10_000, 2, 10, 21_000),
    ],
)
def test_final_total(price, qty, discount, expected):
    assert final_total(price, qty, discount) == expected
