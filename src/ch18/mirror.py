import sys

class LookingGlass:
    
    def __enter__(self):
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write # type: ignore
        return "Jabberwocky"
    
    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_value, traceback):
        """ 
        `exc_type` is the Exception class
        `exc_value` is the Exception instance
        `traceback` is a `traceback` object
        """
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('Please DO NOT divide by zero!')
            return True


with LookingGlass() as what:
    print('Charles Lutwidge Dodgson')
    print(what)
    print(1/0)

print(what)
