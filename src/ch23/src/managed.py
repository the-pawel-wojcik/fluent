def clsname(obj_or_cls):
    cls = type(obj_or_cls)
    if cls is type:
        cls = obj_or_cls
    return cls.__name__.split('.')[-1]


def display(obj):
    cls = type(obj)
    if cls is type:
        return f'<class {obj.__name__}>'
    elif cls in [type(None), int]:
        return repr(obj)
    else:
        return f'<{clsname(cls)} object>'


def print_args(name, *args):
    args_str = ', '.join(display(arg) for arg in args)
    print(f'-> {clsname(args[0])}.__{name}__({args_str})')


class Overriding:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print_args('set', self, instance, value)
        instance.__dict__[self.name] = value


class NonOver:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        print_args('set', self, instance, value)
        instance.__dict__[self.name] = value


class NonSet:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)
        return instance.__dict__[self.name]


class Managed:
    over = Overriding()
    nover = NonOver()
    noset = NonSet()

    def spam(self):
        print('-> Managed.')
