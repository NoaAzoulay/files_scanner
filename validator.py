import os
import re
# Noa Azoulay


class Validator:

    # scan all files and check if any special option appears
    def scan_files(self, files_list):
        for file in files_list:
            if file:
                with open(file, 'r', encoding="utf-8") as inF:
                    for num, line in enumerate(inF, 1):
                        words = line.split()
                        self._check_validators(num, line, words)

    # check if any special option appears
    def _check_validators(self, num, line, words):
        self._is_word(words, "token", num, line)
        self._is_word(words, "password", num, line)
        self._is_more_than_80_chars(words, num, line)
        self._is_user_then_pass(words, num, line)
        self._is_uuid(words, num, line)
        self._find_string_of_variable(line, num)

    # print generic method
    @staticmethod
    def _print_word(num, line, word):
        print(f"line {str(num)} has the word/s {str(word)} in it: \n{line}\n")

    # check if any special word appear (token/password)
    def _is_word(self, words, word, num, line):
        if word in words:
            self._print_word(num, line, word)

    # check if a word contains more than 80 chars
    def _is_more_than_80_chars(self, words, num, line):
        for word in words:
            if len(word) > 80:
                self._print_word(num, line, word + " with more than 80 chars")

    # check if the words user , pass appears, in this order
    def _is_user_then_pass(self, words, num, line):
        flag = 0
        for word in words:
            if word == "user":
                flag = 1
            if word == "pass":
                if flag:
                    self._print_word(num, line, "user, pass")

    # check if the environment variable is set
    @staticmethod
    def _get_environment_variable():
        key = "BC_SPECIAL_WORD"
        env = os.environ.get(key)
        if env is not None:
            return env
        else:
            return None

    # check if the string set from environment variable exists in line
    def _find_string_of_variable(self, line, num):
        s = self._get_environment_variable()
        if s:
            if s in line:
                self._print_word(num, line, s + " of environment variable")

    # check if there is a word in uuid v4 standard in line
    def _is_uuid(self, words, num, line):
        standard = "[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}"
        for word in words:
            if re.match(standard, word):
                self._print_word(num, line, word)