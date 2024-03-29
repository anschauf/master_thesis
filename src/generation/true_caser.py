"""
 Simple True-caser & Top-Most validator

    For simplicity reasons it only compares the count of
    lowercase against capitalized version of a token.
    This method assumes that all punctuations are removed beforehand.

    Also used as an Top-Most validator, as it holds the counts for all the tokens.
    The frequency of token appearances can be written into a file and then also read out of this file.
"""
import string
from collections import Counter


class TrueCaser():

    def __init__(self):
        self.true_case_counter = Counter()
        self.has_training_finished = False

    def train(self, line):
        """
        Add all the token from the param line into the True-Case-Counter.
        The counter is used to evaluate the true-casing afterwards
        :param line:
        :return:
        """
        if self.has_training_finished:
            raise Exception('The training of the TruceCaser model has already finished before this call.')
        line = self.__remove_punctuation(line)
        for token in line.split():
            self.true_case_counter[token] += 1

    def close_training(self):
        """
        Close the training, after all tokens have been read in by add_into_model Method.
        Assures that the model will not be changed afterwards.
        The model returns always lower form if the count is even (incl. also 0).
        :return:
        """
        self.has_training_finished = True

    def true_case(self, token):
        """
        Returns the true case of the param token based on the pre-trained model
        :param token:
        :raises Exception if training has not finished yet
        :return:
        """
        if not self.has_training_finished:
            raise Exception('Training of the true-caser has not finished yet.'
                            ' Close it by calling "close_training"-function.')
        cap_count = self.true_case_counter[token.capitalize()]
        lower_count = self.true_case_counter[token.lower()]

        # keep form if both number are same, also when 0:0
        if cap_count == lower_count:
            return token
        elif cap_count > lower_count:
            return token.capitalize()
        else:
            return token.lower()

    def is_true_case_most_common(self, token, n):
        """
        Is the true-case form of the given token
        one of the n-th common token in the model
        :param token:
        :param n:
        :raises Exception if training has not finished yet.
        :return:
        """
        if not self.has_training_finished:
            raise Exception('Training of the true-caser has not finished yet.'
                            ' Close it by calling "close_training"-function.')
        most_common = self.true_case_counter.most_common(n)
        true_case = self.true_case(token)
        token_count = self.true_case_counter[true_case]
        return most_common.__contains__((true_case, token_count))

    def export_counter(self, path):
        """
        Exports the counter into the provided path location.
        Export is done by writing every token with its corresponding number into the file
        Creates a file if not existing.
        :param path: file path
        :return:
        """
        with open(path, 'w+') as f:
            for k, v in self.true_case_counter.items():
                f.write(k + ';' + str(v) + '\n')

    def import_counter(self, path):
        """
        Imports the counter by the provided path location.
        File must have format 'key;value' on each line
        :param path: file path
        :return:
        """
        with open(path, 'r') as f:
            line = f.readline()
            while line:
                content = line.split(";")
                self.true_case_counter[content[0]] = int(content[1])
                line = f.readline()

    # remove symbols like  [!”#$%&’()*+,-./:;<=>?@[\]^_`{|}~]
    def __remove_punctuation(self, line):
        return line.translate(str.maketrans('', '', string.punctuation))


# def true_case_lines(lines):
#     """
#     Takes in multiple lines of text.
#     Creates a true-case model with the private function and the provided lines.
#     Uses this model to true-case all the lines and return them.
#     :return: true cased lines
#     """
#     model = _build_model(lines)
#
#     true_cased_lines = []
#     for line in lines:
#         true_cased_lines.append(_true_case(line, model))
#     return true_cased_lines
