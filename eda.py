# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     custom_cell_magics: kql
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.2
#   kernelspec:
#     display_name: globant
#     language: python
#     name: python3
# ---

# %%
# Allow autoreload modules to always have the latest version
# %load_ext autoreload
# %autoreload 2

# %%
# include libraries to work with XML
import xml.etree.ElementTree as ET
import xmltodict
import os
import sys
import re
import json
import random
from pipeline.dataloader import AbstractNarrationDataset, CleanAbstract

# %%
# look for the dataset folder that is in the previous folder to this file
dataset_folder = os.path.abspath(os.path.join(os.getcwd(), "dataset"))


# %%
# function that reads the XML file and returns a dictionary
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


# %%
get_xml_as_dict(os.path.join(dataset_folder, "2035012.xml"))

# %%
# read the file using the xmltodict library
# get a random file from the dataset folder
random_file = random.choice(os.listdir(dataset_folder))

# define the file_path
file_path = os.path.join(dataset_folder, random_file)
print("Reading file:", file_path)
# read the XML file
file_dict = get_xml_as_dict(file_path)

# %%
# print the dictionary in a pretty format
print(json.dumps(file_dict, indent=2))


# %% [markdown]
# Let's look the json extracted for the XML file `2003434.xml`
# ```json
# {
#   "AwardTitle": "Collaborative research: Patterns, causes, and consequences of synchrony in giant kelp populations",
#   "AGENCY": "NSF",
#   "AwardEffectiveDate": "08/15/2020",
#   "AwardExpirationDate": "07/31/2024",
#   "AwardTotalIntnAmount": "109079.00",
#   "AwardAmount": "109079",
#   "AwardInstrument": {
#     "Value": "Standard Grant"
#   },
#   "Organization": {
#     "Code": "06040300",
#     "Directorate": {
#       "Abbreviation": "GEO",
#       "LongName": "Directorate For Geosciences"
#     },
#     "Division": {
#       "Abbreviation": "OCE",
#       "LongName": "Division Of Ocean Sciences"
#     }
#   },
#   "ProgramOfficer": {
#     "SignBlockName": "Daniel J. Thornhill",
#     "PO_EMAI": "dthornhi@nsf.gov",
#     "PO_PHON": "7032928143"
#   },
#   "AbstractNarration": "Populations of organisms located in different, often far-apart places can change over time in similar ways. This natural phenomenon, known as synchrony, is important to many issues affecting societal well-being, such as those in medicine, public health, conservation, and natural resource management. For instance, synchrony is critical to the persistence, stability, and resilience of plant and animal populations, and can have cascading effects on biodiversity, ecosystem function, and associated benefits to society. However, many aspects of synchrony are poorly resolved. For example, understanding the influence of multiple potential drivers of synchrony\u2014such as climatic events and predators\u2014has been a longstanding challenge in ecology. Moreover, the causes of synchrony may change over space, time, and timescale (e.g., annual vs. decadal synchrony), but this potential is rarely explored, especially in marine ecosystems. The consequences of synchrony for the dynamics of diverse ecological communities, and the potential for synchrony to have cascading effects across ecosystem boundaries (e.g., from sea to land), are also understudied. Addressing these gaps is especially pressing because growing evidence indicates that climate change may alter patterns of synchrony, potentially leading to diminished spatial resilience of ecosystems. This project studies coastal kelp forests and sandy beach ecosystems to address several current gaps in the understanding of synchrony. The project generates knowledge to improve the understanding of these economically-valuable environments and the many organisms that they sustain. Broader impacts extend through the mentorship of researchers across career stages and student training in coastal ecology and data science. To improve educational opportunities for students from groups underrepresented in science, the project creates a Coastal-Heartland Marine Biology Exchange, in which undergraduates from the Midwest travel to California to carry out coastal field research, and undergraduates from Los Angeles interested in marine biology travel to Kansas to learn biostatistics. To benefit the management of kelp forests in California that have suffered dramatic declines in recent years, workshops will be hosted with coastal managers, conservation practitioners, and other stakeholders to identify restoration sites to enhance regional recovery, stability, and resilience. Methods, software, and data that are useable across scientific disciplines are published online following reproducible and transparent standards.&lt;br/&gt;&lt;br/&gt;The objective of this project is to investigate the patterns and causes of synchrony in giant kelp (Macrocystis pyrifera) forests and the consequences for coastal ecosystem structure and function. By integrating and leveraging numerous long-term, large-scale datasets and analyzing them with new statistical techniques, the investigators  assess how oceanographic conditions, propagule dispersal, and sea urchin herbivory interact to structure the synchrony and stability of giant kelp populations over the past 36 years across 10 degrees of latitude in the northeast Pacific Ocean. New wavelet modeling tools and other statistical techniques are used to quantify the drivers of synchrony and how they operate across geography, time, and timescales. Using a 20-year spatial timeseries of reef biodiversity, it will be determined how giant kelp and other factors induce synchrony in a speciose community of understory algae through \u2018cascades of synchrony\u2019. Moreover, the team tests the degree to which giant kelp synchrony propagates across ecosystem boundaries to sandy beaches through the transport and deposition of allochthonous organic matter (kelp wrack), and how such spatial subsidies produce bottom-up cascades of synchrony to beach invertebrates and shorebirds.&lt;br/&gt;&lt;br/&gt;This award reflects NSF's statutory mission and has been deemed worthy of support through evaluation using the Foundation's intellectual merit and broader impacts review criteria.",
#   "MinAmdLetterDate": "08/07/2020",
#   "MaxAmdLetterDate": "08/07/2020",
#   "ARRAAmount": null,
#   "TRAN_TYPE": "Grant",
#   "CFDA_NUM": "47.050",
#   "NSF_PAR_USE_FLAG": "1",
#   "FUND_AGCY_CODE": "4900",
#   "AWDG_AGCY_CODE": "4900",
#   "AwardID": "2023523",
#   "Investigator": {
#     "FirstName": "Kyle",
#     "LastName": "Cavanaugh",
#     "PI_MID_INIT": "C",
#     "PI_SUFX_NAME": null,
#     "PI_FULL_NAME": "Kyle C Cavanaugh",
#     "EmailAddress": "kcavanaugh@geog.ucla.edu",
#     "NSF_ID": "000683861",
#     "StartDate": "08/07/2020",
#     "EndDate": null,
#     "RoleCode": "Principal Investigator"
#   },
#   "Institution": {
#     "Name": "University of California-Los Angeles",
#     "CityName": "LOS ANGELES",
#     "ZipCode": "900244200",
#     "PhoneNumber": "3107940102",
#     "StreetAddress": "10889 WILSHIRE BLVD STE 700",
#     "StreetAddress2": null,
#     "CountryName": "United States",
#     "StateName": "California",
#     "StateCode": "CA",
#     "CONGRESSDISTRICT": "36",
#     "CONGRESS_DISTRICT_ORG": "CA36",
#     "ORG_UEI_NUM": "RN64EPNH8JC6",
#     "ORG_LGL_BUS_NAME": "UNIVERSITY OF CALIFORNIA, LOS ANGELES",
#     "ORG_PRNT_UEI_NUM": null
#   },
#   "Performance_Institution": {
#     "Name": "UCLA Geography",
#     "CityName": "Los Angeles",
#     "StateCode": "CA",
#     "ZipCode": "900951524",
#     "StreetAddress": "BOX 951524, 1255 Bunche Hall",
#     "CountryCode": "US",
#     "CountryName": "United States",
#     "StateName": "California",
#     "CountryFlag": "1",
#     "CONGRESSDISTRICT": "36",
#     "CONGRESS_DISTRICT_PERF": "CA36"
#   },
#   "ProgramElement": {
#     "Code": "1650",
#     "Text": "BIOLOGICAL OCEANOGRAPHY"
#   },
#   "ProgramReference": [
#     {
#       "Code": "1174",
#       "Text": "POPULATION DYNAMICS"
#     },
#     {
#       "Code": "1195",
#       "Text": "LONG TERM ECOLOGICAL RESEARCH"
#     }
#   ],
#   "Appropriation": {
#     "Code": "0120",
#     "Name": "NSF RESEARCH & RELATED ACTIVIT",
#     "APP_SYMB_ID": "040100"
#   },
#   "Fund": {
#     "Code": "01002021DB",
#     "Name": "NSF RESEARCH & RELATED ACTIVIT",
#     "FUND_SYMB_ID": "040100"
#   },
#   "FUND_OBLG": "2020~109079"
# }
# ```
# Our objective is to classify the abstract topic, for this reason we are interested in the key `AbstractNarration`, so we are going to extract that value. Now note that the information contained in the key `ProgramElement` is the main topic of the article. For that reason we are going to extract these two values to solve our task. But before define functions and organize our info, let's review that this value appears in the majority of the files disposed in the dataset.


# %%
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


# %%
# count the amount of dictionaries that have each key
keys_count = {}

# iterate over all the files in the dataset folder
for file_name in os.listdir(dataset_folder):
    # get the file path
    file_path = os.path.join(dataset_folder, file_name)
    # read the XML file
    file_dict = get_xml_as_dict(file_path)
    award_info = get_award_info_from_dict(file_dict)
    # if the award_info is not empty
    if award_info != {}:
        for key in award_info.keys():
            if key not in keys_count:
                keys_count[key] = 0
            # increase the count of the key
            keys_count[key] += 1

# %%
print(
    f"The amount of files disposed in the dataset is {len(os.listdir(dataset_folder))}"
)
print("The amount of dictionaries that have the important keys is:")
print(f'Abstracts: {keys_count.get("AbstractNarration", 0)}')
print(f'Organization: {keys_count.get("Organization", 0)}')
print(f'Program Element: {keys_count.get("ProgramElement", 0)}')

# %% [markdown]
# As you can note almost the 100% of the files have that value that can help us to guide our model. Now we are going to create the pipeline to clean the data. As you can see to calculate the previous values we iterate over all the files, but in fact when we are going to train a model we don't need to charge all the information, so we can create a DataLoader that will load only the information needed and this DataLoader will process the information only when is required to be used.

# %%
# count the amount of dictionaries that have each key
programs_type_count = {}

# iterate over all the files in the dataset folder
for file_name in os.listdir(dataset_folder):
    # get the file path
    file_path = os.path.join(dataset_folder, file_name)
    # read the XML file
    file_dict = get_xml_as_dict(file_path)
    award_info = get_award_info_from_dict(file_dict)
    # if the award_info is not empty
    if award_info != {}:
        try:
            program_element = type(award_info["ProgramElement"])
            if program_element not in programs_type_count:
                programs_type_count[program_element] = 0
            # increase the count of the programs
            programs_type_count[program_element] += 1
        except:
            print("ProgramElement not found")

# %%
programs_type_count

# %% [markdown]
# When the type of the programs count is a list of dictionaries we are going to extract the first one, and let's count the different programs that the dataset have.

# %%
# count the amount of dictionaries that have each key
programs_count = {}

# iterate over all the files in the dataset folder
for file_name in os.listdir(dataset_folder):
    # get the file path
    file_path = os.path.join(dataset_folder, file_name)
    # read the XML file
    file_dict = get_xml_as_dict(file_path)
    award_info = get_award_info_from_dict(file_dict)
    # if the award_info is not empty
    if award_info != {}:
        try:
            program_element_dict = award_info["ProgramElement"]
            # review if the program_element_dict is a list
            if isinstance(program_element_dict, list):
                program_element_dict = program_element_dict[0]
            program_element = program_element_dict["Text"]
            if program_element not in programs_count:
                programs_count[program_element] = 0
            # increase the count of the programs
            programs_count[program_element] += 1
        except:
            print("ProgramElement not found")

# %%
programs_count


# %%
# count the amount of dictionaries that have each key
organization_count = {}

# iterate over all the files in the dataset folder
for file_name in os.listdir(dataset_folder):
    # get the file path
    file_path = os.path.join(dataset_folder, file_name)
    # read the XML file
    file_dict = get_xml_as_dict(file_path)
    award_info = get_award_info_from_dict(file_dict)
    # if the award_info is not empty
    if award_info != {}:
        try:
            organization_dict = award_info["Organization"]
            # review if the organization_dict is a list
            if isinstance(organization_dict, list):
                organization_dict = organization_dict[0]
            organization_directorate = organization_dict["Directorate"]["LongName"]
            if organization_directorate not in organization_count:
                organization_count[organization_directorate] = 0
            # increase the count of the programs
            organization_count[organization_directorate] += 1
        except:
            print("ProgramElement not found")

# %%
organization_count

# %%
# TODO: define which model I will be use

# %% [markdown]
# ### Abstract clean pipeline
# In order to train the model ??? we have to clean all the abstracts strings and then vectorize to utilize the technique. To do that, let's review if there are special characters that we can clean easily. The dataset loader is included as a package and extract the abstract of each file.


# %%
# initialize the dataset
abstract_narration_dataset = AbstractNarrationDataset(dataset_folder, None)

# %%
abstract_narration_dataset[0]

# %%
# Select a random list of abstracts
import textwrap


random_indexes = random.sample(range(len(abstract_narration_dataset)), 3)
for idx in random_indexes:
    print(f"Abstract {idx + 1}")
    # print the abstract but not allow more than 100 characters per line
    print(textwrap.fill(abstract_narration_dataset[idx], 120))
    print()

# %% [markdown]
# The abstracts are paragraphs that are well written, so they don't need so much preprocessing techniques. We are going for the first stage only focus on drop stop words, particular characters that appear from the HTML structure

# %%
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Initialize NLTK resources
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")


# clean the abstract by removing the characters that generate &lt;br/&gt;&lt;br/&gt;
def clean_abstract(abstract: str, lemmatize: bool = False) -> str:
    """
    Clean the abstract by:
    - lowercase
    - removing the characters that generate &lt;br/&gt;
    - removing the URLs

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


# %%
random_indexes = random.sample(range(len(abstract_narration_dataset)), 1)
for idx in random_indexes:
    print(f"Abstract {idx + 1}")
    abstract = clean_abstract(abstract_narration_dataset[idx])
    # print the abstract but not allow more than 100 characters per line
    print(textwrap.fill(abstract, 120))
    abstract = clean_abstract(abstract_narration_dataset[idx], lemmatize=True)
    # print the abstract but not allow more than 100 characters per line
    print("\nLemmatized:")
    print(textwrap.fill(abstract, 120))
    print()

# %%
# initialize the dataset including the cleaning process
abstract_narration_clean_dataset = AbstractNarrationDataset(dataset_folder, clean=CleanAbstract())
# initialize the dataset including the lemmatize process
abstract_narration_lemmatize_dataset = AbstractNarrationDataset(dataset_folder, clean=CleanAbstract(lemmatize=True))

# %% [markdown]
# Now that we have the classes to load the information an also to do a clean process we are going to do an exploratory analysis in terms of the amount of words that appears in the abstracts, such as the length of each one.

# %%
# calculate the length of the abstracts
abstracts_length = [len(abstract.split()) for abstract in abstract_narration_dataset]
abstracts_clean_length = [len(abstract.split()) for abstract in abstract_narration_clean_dataset]
abstracts_lemmatize_length = [len(abstract.split()) for abstract in abstract_narration_lemmatize_dataset]

# %%
# create a histogram of the length of the abstracts
import matplotlib.pyplot as plt

# create a figure with 3 subplots, in each subplot include the histogram of the length of the abstracts
fig, axs = plt.subplots(1, 3, figsize=(10, 4))
axs[0].hist(abstracts_length, bins=20)
axs[0].set_title("Abstracts length")
axs[0].set_xlabel("Length")
axs[0].set_ylabel("Frequency")

axs[1].hist(abstracts_clean_length, bins=20)
axs[1].set_title("Abstracts length (cleaned)")
axs[1].set_xlabel("Length")
axs[1].set_ylabel("Frequency")

axs[2].hist(abstracts_lemmatize_length, bins=20)
axs[2].set_title("Abstracts length (lemmatized)")
axs[2].set_xlabel("Length")
axs[2].set_ylabel("Frequency")

plt.tight_layout()
plt.show()

# %%
len(abstracts_clean_length)

# %%
abstract_narration_dataset[2798]

# %%
abstract_narration_clean_dataset[2798]

# %% [markdown]
# Once we clean the data the distribution of cleaned and lemmatized seems similar. This is due to in the cleaning process we are extracting stop words and punctuation that can extend the length of the abstracts. Now we are going to count the distinct words generated after each cleaning process to see if there is some word that repeat a lot and can be also reduced using a technique of cleaning.

# %%
# create a dictionary with the frequency of the words in all the abstracts
words_clean_frequency = {}
# iterate over all the abstracts
for abstract in abstract_narration_clean_dataset:
    # split the abstract into words
    words = abstract.split()
    # iterate over all the words
    for word in words:
        # if the word is not in the dictionary, add it
        if word not in words_clean_frequency:
            words_clean_frequency[word] = 0
        # increase the frequency of the word
        words_clean_frequency[word] += 1

# %%
words_clean_frequency

# %%
# transform the dictionary into a dataframe
import pandas as pd

# create a dataframe with the words and the frequency
words_clean_frequency_df = pd.DataFrame(
    {"word": list(words_clean_frequency.keys()), "frequency": list(words_clean_frequency.values())}
)

# sort the dataframe by the frequency
words_clean_frequency_df = words_clean_frequency_df.sort_values("frequency", ascending=False)

# show the first 30 rows of the dataframe
words_clean_frequency_df.head(30)

# %%
# create a dictionary with the frequency of the words in all the abstracts
words_lemmatize_frequency = {}
# iterate over all the abstracts
for abstract in abstract_narration_lemmatize_dataset:
    # split the abstract into words
    words = abstract.split()
    # iterate over all the words
    for word in words:
        # if the word is not in the dictionary, add it
        if word not in words_lemmatize_frequency:
            words_lemmatize_frequency[word] = 0
        # increase the frequency of the word
        words_lemmatize_frequency[word] += 1

# %%
# create a dataframe with the words and the frequency
words_lemmatize_frequency_df = pd.DataFrame(
    {"word": list(words_lemmatize_frequency.keys()), "frequency": list(words_lemmatize_frequency.values())}
)

# sort the dataframe by the frequency
words_lemmatize_frequency_df = words_lemmatize_frequency_df.sort_values("frequency", ascending=False).reset_index(drop=True)

# show the first 30 rows of the dataframe
words_lemmatize_frequency_df.head(30)

# %%
words_lemmatize_frequency_df[words_lemmatize_frequency_df["frequency"] >= 100].sample(30)

# %%
string = '-'
# split string by '-'
string_split = string.split('-')
connector_list = []
for i in range(len(string_split)-1):
    if string_split[i][-1].isalpha() and string_split[i+1][0].isalpha():
        connector_list.append(' ')
    else:
        connector_list.append('')
string_split[0] + ''.join([f'{connector_list[i-1]}{string_split[i]}' for i in range(1, len(string_split))])


# %%
# write the previous code in a function
def get_connector_list(string: str, connector: str) -> list:
    """
    Get a list with the connectors between the words in the string

    Arguments:
        string:
            The string to analyze.
        connector:
            The connector to use.

    Returns:
        A list with the connectors between the words in the string.
    """
    # split the string by the connector
    string_split = string.split(connector)
    connector_list = []
    # iterate over all the elements in the string_split
    for i in range(len(string_split) - 1):
        # if the last character of the first element is a letter and the first character of the second element is a letter
        if string_split[i][-1].isalpha() and string_split[i + 1][0].isalpha():
            connector_list.append(" ")
        else:
            connector_list.append(connector)
    return connector_list


# %%
# concat each value of string_split using connector_list and connector_list has one less element than string_split
result = string_split[0] + ''.join([f'{connector_list[i-1]}{string_split[i]}' for i in range(1, len(string_split))])

# %%
result

# %%
# find rows with word like 'covid'
words_clean_frequency_df[words_clean_frequency_df["word"].str.contains('covid')]

# %%
