import hypothesis.strategies as st
from hypothesis import given

def calc_mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# decorator from Hypothesis to generate a series of test cases
@given(numbers = st.lists(st.integers(min_value=-100, max_value=100), min_size=1))
def test_calc_mean(numbers):
    print("calculated mean = ", calc_mean(numbers))
    assert calc_mean(numbers) == sum(numbers) / len(numbers)

if __name__ == "__main__":
    test_calc_mean()