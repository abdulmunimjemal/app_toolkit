import unittest
import app_toolkit


class TestStopWordsRemover(unittest.TestCase):

    def test_stopwords_remover(self):
        input_list = [
            "አበባ እና ከበደ ጓደኛሞች ናቸው",
            ["ይህ", "ማን", "አንዳች", "ለማይችሉ", "እንዴት"]
        ]
        expected_output = [
            ['አበባ', 'ከበደ', 'ጓደኛሞች'],
            ["ማን", "ለማይችሉ"]
        ]
        for i in range(len(TEST_CASES)):
            self.assertEqual(remove_stopwords(
                input_list=[i]), expected_output[i])

    def test_empty_input(self):
        input_list = []
        expected_output = []
        self.assertEqual(remove_stopwords(input_list), expected_output)

    def test_all_stopwords(self):
        input_list = ["እና", "ናቸው"]
        expected_output = []
        self.assertEqual(remove_stopwords(input_list), expected_output)

    def test_non_amharic_input(self):
        input_list = ["እና", "ናቸው", "hello"]
        expected_output = ["hello"]
        self.assertEqual(remove_stopwords(input_list), expected_output)


if __name__ == "__main__":
    unittest.main()
