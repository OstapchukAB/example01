from extended_stack import ExtendedStack

def test_extended_stack_operations():
    ex_stack = ExtendedStack([1, 2, 3, 4, -3, 3, 5, 10])
    
    # Тест деления
    ex_stack.div()
    assert ex_stack.pop() == 2
    
    # Тест вычитания
    ex_stack.sub()
    assert ex_stack.pop() == 6
    
    # Тест сложения
    ex_stack.sum()
    assert ex_stack.pop() == 7
    
    # Тест умножения
    ex_stack.mul()
    assert ex_stack.pop() == 2
    
    # Проверка пустого стека
    assert len(ex_stack) == 0

def test_empty_stack():
    stack = ExtendedStack()
    stack.sum()  # не должно быть ошибки
    assert len(stack) == 0

def test_division_by_zero():
    stack = ExtendedStack([0, 1])
    stack.div()  # не должен выполниться из-за нуля
    assert stack == [0, 1]