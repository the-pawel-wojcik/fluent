import abc


class Validated(abc.ABC):
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        valid_value = self.validate(self.name, value)
        instance.__dict__[self.name] = valid_value

    @abc.abstractmethod
    def validate(self, name, value):
        """ Returns a validated value or raises error """


class Quantity(Validated):
    """ A positive value. """
    def validate(self, name, value):
        if value > 0:
            return value
        raise ValueError(f'{name} must be positive.')


class NonBlank(Validated):
    """ A non-blank string. """
    def validate(self, name, value):
        if isinstance(value, str):
            if value.strip():
                return value
        raise ValueError(f'{name} cannot be blank.')
