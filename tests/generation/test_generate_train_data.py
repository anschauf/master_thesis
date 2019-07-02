import unittest
from src.generation.generator import generate_train_data_by_lines, generate_train_data


class TestGenerateTrainData(unittest.TestCase):

    def test_not_string_param(self):
        """
        Raise an Exception, if one of the parameter is not a string
        :return:
        """
        self.assertRaises(Exception, generate_train_data, 'test string', 3)
        self.assertRaises(Exception, generate_train_data, 3, 'test string')

    def test_generation_of_train_data(self):
        """
        Checks if the returning values have all the length as expected.
        :return:
        """
        sources_en, sources_de, targets_de, base_de = generate_train_data(
            'Record file and application usage',
            'Die Nutzung von Dateien und Anwendungen aufzeichnen')

        self.assertEqual(len(sources_en), 7, '"sources_en" has lenght of 7.')
        self.assertEqual(len(sources_de), 7, '"sources_de" has lenght of 7.')
        self.assertEqual(len(targets_de), 7, '"targets_de" has lenght of 7.')
        self.assertEqual(len(base_de), 7, '"base_de" has lenght of 7.')
    # def test_empty_parameters(self):
    #     """
    #     Empty parameter entries should return empty lists back
    #     :return:
    #     """
    #     sources_en, sources_de, targets_de = generate_train_data_by_lines([], [])
    #     self.assertEqual(len(sources_en), 0)
    #     self.assertEqual(len(sources_de), 0)
    #     self.assertEqual(len(targets_de), 0)
    #
    # def test_not_same_length(self):
    #     """
    #     Not the same length of the two lists raises an exception.
    #     """
    #     list_en = [
    #         'Includes Gmail, Google Docs, Google +, YouTube and Picasa',
    #         'Change your own user data'
    #     ]
    #     list_de = [
    #         'Umfasst Gmail, Google Docs, Google+, YouTube und Picasa',
    #         'Ändern Ihrer eigenen Benutzerdaten',
    #         'Zur Änderung Ihrer eigenen Benutzerdaten ist eine Legitimierung erforderlich']
    #     self.assertRaises(Exception, generate_train_data_by_lines, list_en, list_de)
    #
    # def test_proper_setup_length(self):
    #     """
    #     Check if all tree list return the same length of 22.
    #     """
    #     list_en = [
    #         'View or change ACL and User Extended Attributes on files and directories',
    #         'Uncover pairs of stones while navigating obstacles using a marble'
    #
    #     ]
    #     list_de = [
    #         'Betrachten oder ändern Sie ACL- und erweiterte Eigenschaften von Dateien und Verzeichnissen',
    #         'Decken Sie Steinpaare auf, während Sie mit einer Murmel um Hindernisse herumnavigieren'
    #     ]
    #     sources_en, sources_de, targets_de = generate_train_data_by_lines(list_en, list_de)
    #
    #     self.assertEqual(len(sources_en), 25)
    #     self.assertEqual(len(sources_de), 25)
    #     self.assertEqual(len(targets_de), 25)
    #
    # def test_proper_setup_lemmatization(self):
    #     """
    #     Checks if the word at same position in sources_de
    #      is the lemmatized word of the word in targets_de
    #     """
    #     list_en = [
    #         'View or change ACL and User Extended Attributes on files and directories',
    #         'Uncover pairs of stones while navigating obstacles using a marble'
    #     ]
    #     list_de = [
    #         'Betrachten oder ändern Sie ACL- und erweiterte Eigenschaften von Dateien und Verzeichnissen',
    #         'Decken Sie Steinpaare auf, während Sie mit einer Murmel um Hindernisse herumnavigieren'
    #     ]
    #     sources_en, sources_de, targets_de = generate_train_data_by_lines(list_en, list_de)
    #
    #     self.assertEqual(sources_de[11],
    #                      'Verzeichnis\n', 'sources_de lemmatizes the word "Verzeichnissen" to "Verzeichnis"')
    #     self.assertEqual(sources_de[23],
    #                      'Hindernis\n', 'sources_de lemmatizes the word "Hindernisse" to "Hindernis"')
    #
    # def test_proper_setup_targets(self):
    #     """
    #     Checks whether entries in targets_de are single tokens from the input sentence.
    #     """
    #     list_en = [
    #         'View or change ACL and User Extended Attributes on files and directories',
    #         'Uncover pairs of stones while navigating obstacles using a marble'
    #     ]
    #     list_de = [
    #         'Betrachten oder ändern Sie ACL- und erweiterte Eigenschaften von Dateien und Verzeichnissen',
    #         'Decken Sie Steinpaare auf, während Sie mit einer Murmel um Hindernisse herumnavigieren'
    #     ]
    #     sources_en, sources_de, targets_de = generate_train_data_by_lines(list_en, list_de)
    #
    #     self.assertEqual(targets_de[0], 'Betrachten\n')
    #     self.assertEqual(targets_de[11], 'Verzeichnissen\n')
    #     self.assertEqual(targets_de[23], 'Hindernisse\n')