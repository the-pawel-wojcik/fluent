from typing import TypeVar, Generic


class Father:
    def say_hi(self):
        print("Hi! I am Father!")


class Son(Father):
    def say_hi(self):
        print("Hi! I am Son!")


class Grandson(Son):
    def say_hi(self):
        print("Hi! I am Grandson!")

T_co = TypeVar('T_co', covariant=True)

class ClassTemplate(Generic[T_co]):
    """ Holder of a type T_co or its decendants. """
    def __init__(self, person: T_co) -> None:
        self.person = person
        
    def produce_a_man(self) -> T_co:
        return self.person


father_holder = ClassTemplate(Father())
son_holder = ClassTemplate(Son())
grandson_holder = ClassTemplate(Grandson())

def the_voice_of_descendants(person_holder: ClassTemplate[Son]) -> None:
    person_holder.produce_a_man().say_hi()

the_voice_of_descendants(father_holder)  # type error
the_voice_of_descendants(son_holder)
the_voice_of_descendants(grandson_holder)  # would be type error, but covariant
