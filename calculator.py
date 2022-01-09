class Math:
    def add(first, second):
        if not isinstance(first, int) and not isinstance(second, int):
            return "Invalid input"
        return first + second

    def subtract(first, second):
        if not isinstance(first, int) and not isinstance(second, int):
            return "Invalid input"
        return first - second
