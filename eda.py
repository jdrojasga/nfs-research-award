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

# %% [markdown]
# ### Including libraries
# These libraries will be used across the jupyter notebook.

# %%
# include libraries to work with XML
import matplotlib.pyplot as plt
import xmltodict
import os
import re
import json
import random
import pandas as pd
from collections import Counter
import numpy as np
from pipeline.dataloader import AbstractNarrationDataset, CleanAbstract
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.manifold import TSNE
import textwrap

# %% [markdown]
# ## Dataset
# Now we are going to define the path in which the dataset is available, and also give a look into the XML files as dictionary using the library `xmltodict`.

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
# get a random file from the dataset folder
random_file = random.choice(os.listdir(dataset_folder))

# define the file_path
file_path = os.path.join(dataset_folder, random_file)
print("Reading file:", file_path)
# read the XML file
file_dict = get_xml_as_dict(file_path)

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
# Our objective is to classify the abstract topic, for this reason we are interested in the key `AbstractNarration`, so we are going to extract that value. Once we get a model that provide us topics for each abstract we are going to compare with the `Organization` and `ProgramElement` because these two have information related to the article.


# %%
# function to extract the information about the awards from the XML dictionary
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


# %% [markdown]
# To explore the information contained in each file, we are going to count the amount of keys that are available. We are putting special attention in the `AbstractNarration` one.

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

# %% [markdown]
# ## DataLoader
# As you can note almost the 100% of the files have that value that can help us to guide our model. Now we are going to create the pipeline to clean the data. As you can see to calculate the previous values we iterate over all the files, but in fact when we are going to train a model we don't need to charge all the information, so we can create a DataLoader that will load only the information needed and this DataLoader will process the information only when is required to be used. This DataLoader is an abstract class that is stored in the `pipeline.dataloader` module. The development of the `AbstractNarrationDataset` was doing during the construction of this Jupyter, in a first instance we thought that all the files had an abstract, which was not true, but all of these articles are being excluded in the initialization of the class.
#
# ### Abstract clean pipeline
# In order to train the model Latent Dirichlet allocation (LDA) we have to clean all the abstracts strings and then vectorize. The data clean process was an iterative execution in which were selected randomly abstracts in order to detect the possible special characters, but always having in mind that these texts are related to articles that was awarded, so the content of each one has good redaction.

# %%
# initialize the dataset
abstract_narration_dataset = AbstractNarrationDataset(dataset_folder, None)

# %%
# Select a random list of abstracts
random_indexes = random.sample(range(len(abstract_narration_dataset)), 3)
for idx in random_indexes:
    print(f"Abstract {idx + 1}")
    # print the abstract but not allow more than 100 characters per line
    print(textwrap.fill(abstract_narration_dataset[idx], 120))
    print()

# %% [markdown]
# The abstracts are paragraphs that are well written (as we mention before), so they don't need so much preprocessing techniques. We are going for the first stage only focus on drop stop words, particular characters that appear from the HTML structure. Here is a glance of the first iteration of the function to clean the text. If you want to review the final function see the class `CleanAbstract` contained in the same `pipeline.dataloader` module. The function that clean the abstracts follow the next logic:
# - lowercase
# - remove the characters that generate &lt;br/&gt;
# - remove the URLs and websites
# - remove the punctuation (except - character when appears between two words)
# - transform the strings like 'covid-19' into 'covid19'
# - remove the stop words (including new ones result of the EDA)
# - lemmatize the words, if the lemmatize is True

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


# %% [markdown]
# We pass the class `CleanAbstract` as an attribute for the pipeline, in order to iterate easily variations on the clean process that can provide us a better performance in the model.

# %%
# initialize the dataset including the cleaning process
abstract_narration_clean_dataset = AbstractNarrationDataset(
    dataset_folder, clean=CleanAbstract()
)
# initialize the dataset including the lemmatize process
abstract_narration_lemmatize_dataset = AbstractNarrationDataset(
    dataset_folder, clean=CleanAbstract(lemmatize=True)
)

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

# %% [markdown]
# Now that we have the classes to load the information an also to do a clean process we are going to do an exploratory analysis in terms of the amount of words that appears in the abstracts, such as the length of each one.

# %%
# calculate the length of the abstracts
abstracts_length = [len(abstract.split()) for abstract in abstract_narration_dataset]
abstracts_clean_length = [
    len(abstract.split()) for abstract in abstract_narration_clean_dataset
]
abstracts_lemmatize_length = [
    len(abstract.split()) for abstract in abstract_narration_lemmatize_dataset
]

# %%
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
# create a dataframe with the words and the frequency
words_clean_frequency_df = pd.DataFrame(
    {
        "word": list(words_clean_frequency.keys()),
        "frequency": list(words_clean_frequency.values()),
    }
)

# sort the dataframe by the frequency
words_clean_frequency_df = words_clean_frequency_df.sort_values(
    "frequency", ascending=False
)

# show the first 30 rows of the dataframe
words_clean_frequency_df.head(30)

# %% [markdown]
# As you can note (and it was detected in the model training) there are words that for this context we can consider as stop words, that words are `["project", "research", "using", "support", "impact", "student"]`. After include that in the clean class the words related to each context improve in difference between topic and topic.

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
    {
        "word": list(words_lemmatize_frequency.keys()),
        "frequency": list(words_lemmatize_frequency.values()),
    }
)

# sort the dataframe by the frequency
words_lemmatize_frequency_df = words_lemmatize_frequency_df.sort_values(
    "frequency", ascending=False
).reset_index(drop=True)

# show the first 30 rows of the dataframe
words_lemmatize_frequency_df.head(30)

# %% [markdown]
# ### Topic modelling
# Once the pipeline to load and transform the data is completed, we are going to use the Latent Dirichilet Allocation (LDA) algorithm in order to obtain a classification of the topics from the abstracts. To do this, we are going to use the dataset lemmatized, and we are going to set as `max_features` in the vectorizer function 800 (due the biggest one have a length of 704, but for new articles we can have a bigger length).

# %%
print(
    f"The maximum abstract length after being lemmatized is: {max(abstracts_lemmatize_length)}"
)

# %%
# using the maximum length of the abstracts as the maximum number of features
count_vectorizer = CountVectorizer(max_features=800)

# %%
abstract_term_matrix = count_vectorizer.fit_transform(
    abstract_narration_lemmatize_dataset
)

# %% [markdown]
# As the amount of organizations that has more than 100 abstracts is 9, we are going to use that as number of topics to train our model.

# %%
n_topics = 9

lda_model = LatentDirichletAllocation(
    n_components=n_topics, learning_method="online", random_state=0, verbose=0
)
lda_topic_matrix = lda_model.fit_transform(abstract_term_matrix)


# %% [markdown]
# Define a bunch of useful functions in order to review the results and extract the most common words in each topic.

# %%
# Define helper functions


def get_keys(topic_matrix: np.ndarray) -> list:
    """
    Get the keys of the topics for each abstract

    Arguments:
        topic_matrix:
            The matrix with the topics for each abstract.

    Returns:
        A list with the keys of the topics for each abstract.
    """
    keys = topic_matrix.argmax(axis=1).tolist()
    return keys


def keys_to_counts(keys: list) -> tuple:
    """
    Count the amount of times that each key appears

    Arguments:
        keys:
            The keys of the topics for each abstract.

    Returns:
        A tuple with the categories and the counts of the keys.
    """
    count_pairs = Counter(keys).items()
    categories = [pair[0] for pair in count_pairs]
    counts = [pair[1] for pair in count_pairs]
    return (categories, counts)


def get_top_n_words(
    n: int,
    keys: list,
    document_term_matrix: np.array,
    count_vectorizer: CountVectorizer,
) -> list:
    """
    Get the top n words for each topic

    Arguments:
        n:
            The number of words to get.
        keys:
            The keys of the topics for each abstract.
        document_term_matrix:
            The matrix with the words for each abstract.
        count_vectorizer:
            The CountVectorizer object.

    Returns:
        A list with the top n words for each topic.
    """
    # get the top n word indices
    top_word_indices = []
    for topic in range(n_topics):
        temp_vector_sum = 0
        for i in range(len(keys)):
            if keys[i] == topic:
                temp_vector_sum += document_term_matrix[i]
        temp_vector_sum = temp_vector_sum.toarray()
        top_n_word_indices = np.flip(np.argsort(temp_vector_sum)[0][-n:], 0)
        top_word_indices.append(top_n_word_indices)
    # get the top n words
    top_words = []
    for topic in top_word_indices:
        topic_words = []
        for index in topic:
            temp_word_vector = np.zeros((1, document_term_matrix.shape[1]))
            temp_word_vector[:, index] = 1
            the_word = count_vectorizer.inverse_transform(temp_word_vector)[0][0]
            topic_words.append(the_word.encode("ascii").decode("utf-8"))
        top_words.append(" ".join(topic_words))
    return top_words


# %%
# get the keys of the topics for each abstract
lda_keys = get_keys(lda_topic_matrix)
lda_categories, lda_counts = keys_to_counts(lda_keys)

# %%
# get a sample of the top words for each topic
top_n_words_lda = get_top_n_words(10, lda_keys, abstract_term_matrix, count_vectorizer)

for i in range(len(top_n_words_lda)):
    print("Topic {}: ".format(i + 1), top_n_words_lda[i])

# %%
# get the top 5 words
top_5_words = get_top_n_words(5, lda_keys, abstract_term_matrix, count_vectorizer)
labels = ["Topic {}: \n".format(i) + top_5_words[i] for i in lda_categories]

# create a bar plot to show the amount of abstracts for each topic and the top words
fig, ax = plt.subplots(figsize=(16, 8))
ax.bar(lda_categories, lda_counts)
ax.set_xticks(lda_categories)
ax.set_xticklabels(labels)
# rotate the labels
plt.xticks(rotation=90)
ax.set_title("LDA topic counts")
ax.set_ylabel("Number of headlines")

# %% [markdown]
# Finally, let's get a sample of the topics generated and the content of the abstracts and also the organization.

# %%
# for loop to print the top 5 words for each topic
for topic in range(len(top_5_words)):
    # select a random index for topic 0 using keys
    random_index = random.choice([i for i, key in enumerate(lda_keys) if key == topic])

    print(f"The top 5 words related to the topic {topic} are: {top_5_words[topic]}")
    print(f"The abstract is:")
    # print the abstract but not allow more than 100 characters per line
    print(textwrap.fill(abstract_narration_dataset[random_index][:240], 120))
    xml_dict = get_xml_as_dict(
        os.path.join(dataset_folder, abstract_narration_dataset.files[random_index])
    )
    abstract_dict = get_award_info_from_dict(xml_dict)
    print(f"The organization information is:")
    print(json.dumps(abstract_dict["Organization"], indent=2))
    print(f"The program element information is:")
    print(json.dumps(abstract_dict["ProgramElement"], indent=2))
    print()

# %% [markdown]
# Looking at the previous output we can see that the process is having a coincidence with the fields organization and program element. In fact, we can try to call each topic with a specific category, for example, the topic 1 is more related to `Geosciences`, in the random abstracts selected to visualize the results we can find that relationship. It's imperative to iterate this process:
# 1. Include more stop words that can be misunderstanding the results (such as `award`, `ha`, among others)
# 2. Improve the selection of the amount of topics to train the model [this article](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8534395/) has a methodology to calculate a better quantity of topics.
# 3. Visualize the results reducing the dimension (t-SNE)
# 4. Use other machine learning techniques in order to improve semantic similarity [BERTopic](https://github.com/MaartenGr/BERTopic) can be a useful tool to iterate and explore different approaches.
#
# Nice to have in the future to put in production: CLI commands to train and save the model, such as generate predictions.

# %% [markdown]
#
