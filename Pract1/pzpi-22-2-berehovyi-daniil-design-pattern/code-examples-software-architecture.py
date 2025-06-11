from abc import ABC, abstractmethod

# Абстрактні продукти
class Button(ABC):
    @abstractmethod
    def render(self): pass

class Checkbox(ABC):
    @abstractmethod
    def render(self): pass

# Конкретні продукти
class WinButton(Button):
    def render(self): print("Rendering Windows Button")

class MacButton(Button):
    def render(self): print("Rendering Mac Button")

class WinCheckbox(Checkbox):
    def render(self): print("Rendering Windows Checkbox")

class MacCheckbox(Checkbox):
    def render(self): print("Rendering Mac Checkbox")

# Абстрактна фабрика
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self): pass

    @abstractmethod
    def create_checkbox(self): pass

# Конкретні фабрики
class WinFactory(GUIFactory):
    def create_button(self): return WinButton()
    def create_checkbox(self): return WinCheckbox()

class MacFactory(GUIFactory):
    def create_button(self): return MacButton()
    def create_checkbox(self): return MacCheckbox()

# Клієнтський код
def create_ui(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    button.render()
    checkbox.render()

class OldPrinter:
    def specific_request(self):
        return "OLD PRINTER"

class NewPrinter:
    def print(self):
        return "NEW PRINTER"

class PrinterAdapter:
    def __init__(self, old_printer):
        self.old_printer = old_printer

    def print(self):
        return self.old_printer.specific_request()

# Використання
def use_printer(printer):
    print(printer.print())

old = PrinterAdapter(OldPrinter())
new = NewPrinter()

use_printer(old)  # OLD PRINTER
use_printer(new)  # NEW PRINTER

class Text:
    def render(self):
        return "Hello"

class TextDecorator:
    def __init__(self, wrapped):
        self._wrapped = wrapped

    def render(self):
        return self._wrapped.render()

class BoldDecorator(TextDecorator):
    def render(self):
        return f"<b>{super().render()}</b>"

class ItalicDecorator(TextDecorator):
    def render(self):
        return f"<i>{super().render()}</i>"

# Використання
simple = Text()
bold = BoldDecorator(simple)
italic_bold = ItalicDecorator(bold)

print(italic_bold.render())  # <i><b>Hello</b></i>

class Subject:
    def __init__(self):
        self._observers = []
        self._state = None

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._state)

    def change_state(self, value):
        self._state = value
        self.notify()

class Observer:
    def update(self, state):
        print(f"Updated with new state: {state}")

# Використання
subject = Subject()
obs1 = Observer()
obs2 = Observer()
subject.attach(obs1)
subject.attach(obs2)
subject.change_state("data loaded")

def main():
    print("=== Abstract Factory ===")
    create_ui(WinFactory())
    create_ui(MacFactory())

    print("\n=== Adapter ===")
    old = PrinterAdapter(OldPrinter())
    new = NewPrinter()
    use_printer(old)
    use_printer(new)

    print("\n=== Decorator ===")
    text = Text()
    decorated = ItalicDecorator(BoldDecorator(text))
    print(decorated.render())

    print("\n=== Observer ===")
    subject = Subject()
    observer1 = Observer()
    observer2 = Observer()
    subject.attach(observer1)
    subject.attach(observer2)
    subject.change_state("New Event")

if __name__ == "__main__":
    main()
