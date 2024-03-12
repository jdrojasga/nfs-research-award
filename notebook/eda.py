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
# include libraries to work with XML
import xml.etree.ElementTree as ET
import xmltodict
import os
import sys
import re
import json
import random

# %%
# look for the dataset folder that is in the previous folder to this file
dataset_folder = os.path.abspath(os.path.join(os.getcwd(), '../dataset'))


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
        with open(file_path, 'r') as file:
            # read the file
            data = file.read()
            # convert the XML to a dictionary
            return xmltodict.parse(data)
    # manage error in case the file is not found
    except FileNotFoundError:
        print(f'File not found: {file_path}')
        return None


# %%
get_xml_as_dict(os.path.join(dataset_folder, 'books.xml'))

# %%
# read the file using the xmltodict library
# get a random file from the dataset folder
random_file = random.choice(os.listdir(dataset_folder))

# define the file_path
file_path = os.path.join(dataset_folder, random_file)
print('Reading file:', file_path)
# read the XML file
file_dict = get_xml_as_dict(file_path)

# %%
get_xml_as_dict(file_path)

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
    if 'rootTag' in xml_dict:
        if 'Award' in xml_dict['rootTag']:
            return xml_dict['rootTag']['Award']
        else:
            print('Award not found')
            return {}
    else:
        print('rootTag not found')
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
print(f'The amount of files disposed in the dataset is {len(os.listdir(dataset_folder))}')
print('The amount of dictionaries that have the important keys is:')
print(f'Abstracts: {keys_count.get("AbstractNarration", 0)}')
print(f'Program Element: {keys_count.get("ProgramElement", 0)}')

# %% [markdown]
# As you can note almost the 100% of the files have that value that can help us to guide our model. Now we are going to create the pipeline to clean the data. As you can see to calculate the previous values we iterate over all the files, but in fact when we are going to train a model we don't need to charge all the information, so we can create a DataLoader that will load only the information needed and this DataLoader will process the information only when is required to be used.

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
            program_element = type(award_info['ProgramElement'])
            if program_element not in programs_count:
                programs_count[program_element] = 0
            # increase the count of the programs
            programs_count[program_element] += 1
        except:
            print('ProgramElement not found')

# %%
programs_count

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
            program_element_dict = award_info['ProgramElement']
            # review if the program_element_dict is a list
            if isinstance(program_element_dict, list):
                program_element_dict = program_element_dict[0]
            program_element = program_element_dict['Text']
            if program_element not in programs_count:
                programs_count[program_element] = 0
            # increase the count of the programs
            programs_count[program_element] += 1
        except:
            print('ProgramElement not found')

# %%
programs_count


# %%
# TODO: define which model I will be use

# %% [markdown]
# ### Abstract clean pipeline
# In order to train the model ??? we have to clean all the abstracts strings and then vectorize to utilize the technique. To do that, let's review if there are special characters that we can clean easily.

# %%
# class that will be used to load the dataset
class AbstractNarrationDataset:
    def __init__(self, dataset_folder: str):
        self.dataset_folder = dataset_folder
        self.files = os.listdir(dataset_folder)

    def __len__(self):
        return len(self.files)

    def __getitem__(self, idx):
        file_name = self.files[idx]
        file_path = os.path.join(self.dataset_folder, file_name)
        file_dict = get_xml_as_dict(file_path)
        award_info = get_award_info_from_dict(file_dict)
        abstract = award_info['AbstractNarration']
        return abstract


# %%
# initialize the dataset
abstract_narration_dataset = AbstractNarrationDataset(dataset_folder)

# %%
# Select a random list of abstracts
import textwrap


random_indexes = random.sample(range(len(abstract_narration_dataset)), 3)
for idx in random_indexes:
    print(f'Abstract {idx + 1}')
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
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

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
    abstract = abstract.replace('&lt;br/&gt;', '')
    abstract = re.sub(r'http\S+', '', abstract)
    # drop the punctuation except the - character
    abstract = re.sub(r'[^\w\s-]', '', abstract)

    words = word_tokenize(abstract)
    stop_words = set(stopwords.words('english'))
    if lemmatize:
        lemmatizer = WordNetLemmatizer()
        cleaned_abstract = [lemmatizer.lemmatize(word) for word in words if word.isalnum() and word not in stop_words]
    else:
        cleaned_abstract = [word for word in words if word not in stop_words]
    return ' '.join(cleaned_abstract)


# %%
random_indexes = random.sample(range(len(abstract_narration_dataset)), 5)
for idx in random_indexes:
    print(f'Abstract {idx + 1}')
    abstract = clean_abstract(abstract_narration_dataset[idx])
    # print the abstract but not allow more than 100 characters per line
    print(textwrap.fill(abstract, 120))
    abstract = clean_abstract(abstract_narration_dataset[idx], lemmatize=True)
    # print the abstract but not allow more than 100 characters per line
    print('\nLemmatized:')
    print(textwrap.fill(abstract, 120))
    print()

# %%
abstract = word_tokenize(abstract_narration_dataset[3022])
abstract = remove_urls(abstract)
# print the abstract but not allow more than 100 characters per line
print(textwrap.fill(abstract, 120))

# %%
tokenize = word_tokenize(abstract_narration_dataset[3022])
list_stop = set(stopwords.words('english'))
abstract = [word for word in tokenize if word not in list_stop]

# %%
abstract

# %%
