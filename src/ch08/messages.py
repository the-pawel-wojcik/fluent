# version 0: No type hints
# def show_count(count, word):
# version 1: incomplete type hints
# def show_count(count, word) -> str:
# version 2: all hinted
def show_count(count: int, word: str, plural: str = "") -> str:
    if count == 1:
        return f'1 {word}'
    if not plural:
        plural = word + 's'
    count_str = str(count) if count else 'no'
    return f'{count_str} {plural}'
