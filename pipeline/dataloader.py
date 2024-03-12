"""Module for loading data from the dataset."""

import re
import xmltodict
import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


# class that will be used to load the dataset
class AbstractNarrationDataset:
    def __init__(
        self, dataset_folder: str, clean: bool = False, lemmatize: bool = False
    ):
        self.dataset_folder = dataset_folder
        # get the list of files in the dataset folder that ends with .xml
        self.files = [f for f in os.listdir(dataset_folder) if f.endswith(".xml")]
        self.clean = clean
        self.lemmatize = lemmatize
        if self.clean:
            # Initialize NLTK resources
            nltk.download("punkt")
            nltk.download("stopwords")
            if self.lemmatize:
                self.lemmatize = lemmatize
                # Initialize NLTK resources
                nltk.download("wordnet")

    def __len__(self):
        return len(self.files)

    def __getitem__(self, idx):
        file_name = self.files[idx]
        file_path = os.path.join(self.dataset_folder, file_name)
        file_dict = self.get_xml_as_dict(file_path)
        award_info = self.get_award_info_from_dict(file_dict)
        abstract = award_info["AbstractNarration"]
        if self.clean:
            abstract = self.clean_abstract(abstract, self.lemmatize)
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

    # clean the abstract
    @staticmethod
    def clean_abstract(abstract: str, lemmatize: bool = False) -> str:
        """
        Clean the abstract by:
        - lowercase
        - removing the characters that generate &lt;br/&gt;
        - removing the URLs
        - removing the punctuation
        - removing the stop words
        - lemmatizing the words if lemmatize is True

        Arguments:
            abstract:
                The abstract to clean.
            lemmatize:
                If True, the words will be lemmatized.

        Returns:
            A string with the abstract cleaned.
        """

        abstract = abstract.lower()
        abstract = abstract.replace("&lt;br/&gt;", "")
        abstract = re.sub(r"http\S+", "", abstract)
        # drop the punctuation except the - character
        abstract = re.sub(r"[^\w\s-]", "", abstract)

        words = word_tokenize(abstract)
        stop_words = set(stopwords.words("english"))
        if lemmatize:
            lemmatizer = WordNetLemmatizer()
            cleaned_abstract = [
                lemmatizer.lemmatize(word)
                for word in words
                if word.isalnum() and word not in stop_words
            ]
        else:
            cleaned_abstract = [word for word in words if word not in stop_words]
        return " ".join(cleaned_abstract)
