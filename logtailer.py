class Tail:
    def __init__(self, file_name='', pattern_list=['.*']):
        self.file_name = file_name
        self.pattern_list = pattern_list

    def initialize(self, file_name, pattern_list):
        self.file_name = file_name
        self.pattern_list = pattern_list

    def add_pattern(self, pattern):
        self.pattern_list.append(pattern)

    def remove_pattern(self, index):
        try:
            del self.pattern_list[index]
        except IndexError:
            return False
        return True

    def start(self, callback_func):
        self.callback_func = callback_func

        return True

if __name__ == "__main__":
    print('Hello World')
