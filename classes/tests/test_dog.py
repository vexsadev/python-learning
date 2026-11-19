from learning_classes.dog import Dog


def test_instance_attributes():
    dog = Dog("Rex", 3)
    assert dog.name == "Rex"
    assert dog.age == 3
    assert dog.tricks == []


def test_class_attribute_is_shared():
    assert Dog("A", 1).species == Dog("B", 2).species == Dog.species


def test_tricks_are_not_shared_between_instances():
    a, b = Dog("A", 1), Dog("B", 2)
    a.learn("sit")
    assert a.tricks == ["sit"]
    assert b.tricks == []


def test_methods():
    dog = Dog("Rex", 3)
    assert dog.bark() == "Rex says woof!"
    assert dog.birthday() == 4


def test_repr_and_str():
    dog = Dog("Rex", 3)
    assert repr(dog) == "Dog(name='Rex', age=3)"
    assert str(dog) == "Rex (3 years old)"
