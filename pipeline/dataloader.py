"""Module for loading data from the dataset."""

import re
import xmltodict
import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


# class that clean the abstract
class CleanAbstract:
    def __init__(self, lemmatize: bool = False):
        self.lemmatize = lemmatize
        # Initialize NLTK resources
        nltk.download("punkt")
        nltk.download("stopwords")
        if self.lemmatize:
            # Initialize NLTK resources
            nltk.download("wordnet")

    def clean_abstract(self, abstract: str) -> str:
        """
        Clean the abstract by:
        - lowercase
        - removing the characters that generate &lt;br/&gt;
        - removing the URLs and websites
        - removing the punctuation
        - transform the strings like 'covid-19' into 'covid19'
        - removing the stop words
        - lemmatizing the words if lemmatize is True

        Arguments:
            abstract:
                The abstract to clean.

        Returns:
            A string with the abstract cleaned.
        """

        abstract = abstract.lower()
        abstract = abstract.replace("&lt;br/&gt;", "")
        abstract = re.sub(r"http\S+", "", abstract)
        # removing the websites
        abstract = re.sub(r"www\S+", "", abstract)
        # drop the punctuation except the - character when appears between two words
        abstract = re.sub(r"[^\w\s-]", "", abstract)
        # reduce -- to -
        abstract = re.sub(r"-+", "-", abstract)

        # clean the hyphen words
        words = word_tokenize(abstract)
        words = [self.clean_hyphen_words(word) for word in words]
        abstract = " ".join(words)

        words = word_tokenize(abstract)
        words = [word for word in words if word.isalnum()]
        stop_words = set(stopwords.words("english"))
        if self.lemmatize:
            lemmatizer = WordNetLemmatizer()
            cleaned_abstract = [
                lemmatizer.lemmatize(word)
                for word in words
                if word.isalnum() and word not in stop_words
            ]
        else:
            cleaned_abstract = [word for word in words if word not in stop_words]
        return " ".join(cleaned_abstract)

    @staticmethod
    def clean_hyphen_words(word: str) -> str:
        """
        Transform a string like 'covid-19' into 'covid19', and 'state-of-the-art' into
        'state of the art'

        Arguments:
            word:
                The word to clean.

        Returns:
            A string with the hyphen words cleaned.
        """
        if len(word) <= 2:
            return word
        if word[0] == "-":
            word = word[1:]
        if word[-1] == "-":
            word = word[:-1]
        # split string by '-'
        word_split = word.split("-")
        connector_list = []
        for i in range(len(word_split) - 1):
            if word_split[i][-1].isalpha() and word_split[i + 1][0].isalpha():
                connector_list.append(" ")
            else:
                connector_list.append("")
        word = word_split[0] + "".join(
            [f"{connector_list[i-1]}{word_split[i]}" for i in range(1, len(word_split))]
        )
        return word


# class that will be used to load the dataset
class AbstractNarrationDataset:
    def __init__(self, dataset_folder: str, clean: CleanAbstract = CleanAbstract()):
        self.dataset_folder = dataset_folder
        # get the list of files in the dataset folder that ends with .xml
        self.files = [f for f in os.listdir(dataset_folder) if f.endswith(".xml")]
        # exclude from the dataset the files that do not have the AbstractNarration
        self.__exclude_files_without_abstract_narration()
        self.clean = clean

    def __len__(self):
        return len(self.files)

    def __getitem__(self, idx):
        file_name = self.files[idx]
        file_path = os.path.join(self.dataset_folder, file_name)
        file_dict = self.get_xml_as_dict(file_path)
        award_info = self.get_award_info_from_dict(file_dict)
        abstract = award_info["AbstractNarration"]
        if self.clean:
            abstract = self.clean.clean_abstract(abstract)
        return abstract

    # function that reads the XML file and returns a dictionary
    @staticmethod
    def get_xml_as_dict(file_path: str) -> dict:
        """
        Read an XML file and return a dictionary with the data

        Arguments:
            file_path:
                The path to the XML file to read.

        Returns:
            A dictionary with the data from the XML file. If the file is not found, it
            returns FileNotFoundError
        """
        try:
            # open the file
            with open(file_path, "r") as file:
                # read the file
                data = file.read()
                # convert the XML to a dictionary
                return xmltodict.parse(data)
        # manage error in case the file is not found
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            return None

    @staticmethod
    def get_award_info_from_dict(xml_dict: dict) -> dict:
        """
        Get the information about the awards from the XML dictionary

        Arguments:
            xml_dict:
                The dictionary with the data from the XML file.

        Returns:
            A dictionary with the information about the awards. If the awards are not found, it
            returns an empty dictionary.
        """
        if "rootTag" in xml_dict:
            if "Award" in xml_dict["rootTag"]:
                return xml_dict["rootTag"]["Award"]
            else:
                print("Award not found")
                return {}
        else:
            print("rootTag not found")
            return {}

    ################################
    #       PRIVATE METHODS        #
    ################################

    # exclude from the dataset the files that do not have the AbstractNarration
    def __exclude_files_without_abstract_narration(self):
        self.files = [
            f
            for f in self.files
            if self.get_award_info_from_dict(
                self.get_xml_as_dict(os.path.join(self.dataset_folder, f))
            )["AbstractNarration"]
            is not None
        ]

    # # clean the abstract
    # @staticmethod
    # def clean_abstract(abstract: str, lemmatize: bool = False) -> str:
    #     """
    #     Clean the abstract by:
    #     - lowercase
    #     - removing the characters that generate &lt;br/&gt;
    #     - removing the URLs
    #     - removing the punctuation
    #     - removing the stop words
    #     - lemmatizing the words if lemmatize is True

    #     Arguments:
    #         abstract:
    #             The abstract to clean.
    #         lemmatize:
    #             If True, the words will be lemmatized.

    #     Returns:
    #         A string with the abstract cleaned.
    #     """

    #     abstract = abstract.lower()
    #     abstract = abstract.replace("&lt;br/&gt;", "")
    #     abstract = re.sub(r"http\S+", "", abstract)
    #     # drop the punctuation except the - character
    #     abstract = re.sub(r"[^\w\s-]", "", abstract)

    #     words = word_tokenize(abstract)
    #     stop_words = set(stopwords.words("english"))
    #     if lemmatize:
    #         lemmatizer = WordNetLemmatizer()
    #         cleaned_abstract = [
    #             lemmatizer.lemmatize(word)
    #             for word in words
    #             if word.isalnum() and word not in stop_words
    #         ]
    #     else:
    #         cleaned_abstract = [word for word in words if word not in stop_words]
    #     return " ".join(cleaned_abstract)
