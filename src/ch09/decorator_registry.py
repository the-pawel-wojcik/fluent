registry = set()

def register(active = True):
    def decorator(func):
        print(f'Running register(active={active}) -> decorator({func})')
        if active is True:
            registry.add(func)
        else:
            registry.discard(func)
        return func
    return decorator

@register()
def f1():
    print("Running f1")

@register(active=False)
def f2():
    print("Running f2")

def f3():
    print("Running f3")

print(f'{registry=}')
register()(f3)
print(f'{registry=}')
register(active=False)(f1)
print(f'{registry=}')
