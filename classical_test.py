from classical import Classical_Ciphers
from os.path import join
class Tester():
    def __init__(self):
        self.clear()
    def clear(self):
        self.__plain_texts = []
        self.__cipher_texts = []
    def __get_plain_texts(self, path, file_name):
        file_path = join(path, file_name + '.txt')
        with open(file_path, mode = 'r') as f:
            for line in f:
                self.__plain_texts.append(line.replace('\n', ''))
    def __write_output(self, path, file_name):
        file_path = join(path, file_name + '.txt')
        for i in range(len(self.__cipher_texts) - 1):
            self.__cipher_texts[i] += '\n'
        with open(file_path, mode = 'w') as f:
            f.writelines(self.__cipher_texts)
    def show_plain_texts(self):
        print(self.__plain_texts)
    def test_encryption(self, path, input_file_name, output_file_name, cipher_type, key, vegenere_auto_mode = True):
        self.__get_plain_texts(path, input_file_name)
        cipher = Classical_Ciphers(cipher_type, key, vegenere_auto_mode)
        for plain_text in self.__plain_texts:
            self.__cipher_texts.append(cipher.encrypt(plain_text))
        self.__write_output(path, output_file_name)
        self.clear()

tester = Tester()
tester.test_encryption('../Input Files/Caesar', 'caesar_plain', 'caesar_cipher_3', 'caeser', 3)
tester.test_encryption('../Input Files/Caesar', 'caesar_plain', 'caesar_cipher_6', 'caeser', 6)
tester.test_encryption('../Input Files/Caesar', 'caesar_plain', 'caesar_cipher_12', 'caeser', 12)
tester.test_encryption('../Input Files/Hill', 'hill_plain_2x2', 'hill_cipher_2x2', 'hill', [5, 17, 8, 3])
tester.test_encryption('../Input Files/Hill', 'hill_plain_3x3', 'hill_cipher_3x3', 'hill', [2, 4, 12, 9, 1, 6, 7, 5, 3])
tester.test_encryption('../Input Files/PlayFair', 'playfair_plain', 'playfair_cipher_rats', 'playfair', 'rats')
tester.test_encryption('../Input Files/PlayFair', 'playfair_plain', 'playfair_cipher_archangel', 'playfair', 'archangel')
tester.test_encryption('../Input Files/Vigenere', 'vigenere_plain', 'vigenere_cipher_auto', 'vegenere', 'aether', True)
tester.test_encryption('../Input Files/Vigenere', 'vigenere_plain', 'vigenere_cipher_repeat', 'vegenere', 'pie', False)
tester.test_encryption('../Input Files/Vernam', 'vernam_plain', 'vernam_cipher', 'vernam', 'SPARTANS')