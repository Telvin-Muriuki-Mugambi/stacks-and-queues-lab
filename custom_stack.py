def is_valid_parentheses(s: str) -> bool:
    """
    Return True if the string contains valid, balanced parentheses.
    Only (), {}, and [] are considered valid.
    """
    opening_to_closing = {"(": ")", "{": "}", "[": "]"}
    closing_brackets = set(opening_to_closing.values())
    stack = []

    for character in s:
        if character in opening_to_closing:
            stack.append(character)
        elif character in closing_brackets:
            if not stack or opening_to_closing[stack.pop()] != character:
                return False

    return not stack
