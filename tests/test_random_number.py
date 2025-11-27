from src.random_number import generate_random_number

TEST_1 = 50
TEST_2 = 100


def test_generate_random_number() -> None:
    assert generate_random_number(TEST_1) < TEST_1
    assert (generate_random_number(TEST_2) > TEST_2) is False
