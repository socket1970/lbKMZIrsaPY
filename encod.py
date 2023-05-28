from json import load


class Encod:
    def decoding(self, decode_word, encod="64_lw") \
            -> list[str]:
        """
        Decoding words by using tabel.

        :param decode_word: Integer, word to decoding.
        :param encod: String, encoding table(64_lw, 64_up, 32_lw, 32_up).

        :return: list[String] with decoding word.
        """
        if encod == "64_up" or encod == "64_lw":
            count = 6
        elif encod == "32_up" or encod == "32_lw":
            count = 5
        else:
            raise UnicodeError

        alphabet = self.__read_json(encod)

        decoding_worlds = []

        for i in decode_word:
            word = str(bin(int(i)))
            word = word[1:]
            word = word[1:]

            if len(word) % count != 0:
                word = ("0" * (count - len(word) % count)) + word

            dec_word = ""

            chunks = [word[j:j + count] for j in range(0, len(word), count)]
            for chunk in chunks:
                for k in alphabet:
                    if chunk == k:
                        dec_word += alphabet[k]
            decoding_worlds.append(dec_word)
        return decoding_worlds

    def encoding(self, string, n, encod="64_lw") \
            -> list[str]:
        """
        Encoding word by use table(alphabet.json).

        :param string: String, word to be encoded.
        :param n: Integer, number of word splits.
        :param encod: String, encoding table(64_lw, 64_up, 32_lw, 32_up).

        :return: list[String](binary) with encoding word.
        """
        alphabet = self.__read_json(encod)
        encode_words = []

        string = [string[i:i+n] for i in range(0, len(string), n)]
        if len(string[-1]) < n:
            string[-1] += "а" * (n - len(string[-1]))

        for i in string:
            encode_word = ""
            for j in i:
                for k in alphabet:
                    if j == alphabet[k]:
                        encode_word += k

            encode_words.append(str(int(encode_word, 2)))
        return encode_words

    def __read_json(self, encod):
        """

        :param encod:
        :return:
        """
        try:
            with open("alphabet.json", "r", encoding="utf-8") as file:
                temp = load(file)
        except IOError:
            print("file not accessible")
        for key, value in temp.items():
            if key == encod:
                return value
