class HelloWorld:

    def __init__(self, name):
        self.name = name

    def say_hello(self) -> str:
        return f"Hello {self.name}!"
    
    def say_bye(self, from_who: str) -> str:
        return f"{from_who} said by to {self.name}."

    def is_girl(self, gender):
        if gender == "F":
            return True
        else:
            return False
