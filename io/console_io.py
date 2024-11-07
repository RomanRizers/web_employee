class ConsoleIO:
    def input(self, field, defvalue=None):
        return input(f"{field}: ")
    
    def output(self, title, field):
        print(f"{title}: {field}")
