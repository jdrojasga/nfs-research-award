# nfs-research-award
Repository with the classification of abstracts from the NFS in order to solve the technical test to be part of Globant.

## Instructions

The idea of this challenge is to identify in a better way your capacities to translate data into assets, we expect a good pipeline and solution that you can understand and translate. Select one of the below problems where it is affordable to create an asset using python (scripts files is prefer) where we can identify whole data process, not only the modeling part, like data pipeline/flow, but you can develop a notebook file. Remember to make it available over github

*Hint:*
- Highlight variables or patterns using EDA
- Be sure to clarify your hypothesis
- Validate your functions
- Be clear with the pipeline
- Readme and Requirements files are a plus

Your task is developing an unsupervised model which classifies abstracts into a topic (discover them!). Indeed, your goal is to group abstracts based on their semantic similarity. **Aside notes: All fields in every abstract file wouldn’t be needed. Be keen.**

## Installation

To use this repo first, you have to create an environment using conda:

```bash
conda create -n globant python=3.10
conda activate globant
```

Then [install poetry](https://python-poetry.org/docs/#installing-with-the-official-installer) following the instructions of your OS. Once you install poetry and add to the CLI. You can test if every is working:

```bash
poetry --version
```

## Dataset

In order to not have the [dataset](https://www.nsf.gov/awardsearch/download?DownloadFileName=2020&All=true) used in this technical test in the online repo, we are putting the dataset inside the repo folder, but we are excluding the folder `\dataset` from the git flow. If you decide to put a different name please update the new path to use the jupyter notebook.

## Pipeline and clean process

There were created the classes `AbstractNarrationDataset` and `CleanAbstract` in the module `pipeline.dataloader` to interact with the dataset folder. In the first one you get an iterable that can be passed to interact with the abstract information of any file, and include the clean process that is stored in the second mentioned class. To see more details about the process and clean rules defined for the dataset available see the jupyter notebook `eda.py`.

## Model

It was trained a LDA model using 9 topics (following the amount of Organizations in the dataset), and we obtain the results that you can see in the following subsection. Looking the output we can see that the process is having a coincidence with the fields organization and program element. In fact, we can try to call each topic with a specific category, for example, the topic 1 is more related to `Geosciences`, in the random abstracts selected to visualize the results we can find that relationship. 

### Next steps

It's imperative to iterate this process:
1. Include more stop words that can be misunderstanding the results (such as `award`, `ha`, among others)
2. Improve the selection of the amount of topics to train the model [this article](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8534395/) has a methodology to calculate a better quantity of topics.
3. Visualize the results reducing the dimension (t-SNE)
4. Use other machine learning techniques in order to improve semantic similarity [BERTopic](https://github.com/MaartenGr/BERTopic) can be a useful tool to iterate and explore different approaches.

Nice to have in the future to put in production: CLI commands to train and save the model, such as generate predictions.

### Results

```python
The top 5 words related to the topic 0 are: ha nsf award data new
The abstract is:
The photosynthetic microbes – the phytoplankton – generate about 50% of the oxygen and organic matter produced on Earth
each year and serve as the base of marine food webs. Flow cytometers are essential oceanographic instruments that rapidl
The organization information is:
{
  "Code": "06040100",
  "Directorate": {
    "Abbreviation": "GEO",
    "LongName": "Directorate For Geosciences"
  },
  "Division": {
    "Abbreviation": "OCE",
    "LongName": "Division Of Ocean Sciences"
  }
}
The program element information is:
{
  "Code": "1680",
  "Text": "OCEAN TECH & INTERDISC COORDIN"
}

The top 5 words related to the topic 1 are: water soil carbon change ha
The abstract is:
The COVID-19 restrictions in the Denver Metro area present an unprecedented opportunity to understand how urban river
water quality might improve during times of greatly reduced traffic. Cleaner, fishable and swimmable urban rivers would
be
The organization information is:
{
  "Code": "06030000",
  "Directorate": {
    "Abbreviation": "GEO",
    "LongName": "Directorate For Geosciences"
  },
  "Division": {
    "Abbreviation": "EAR",
    "LongName": "Division Of Earth Sciences"
  }
}
The program element information is:
[
  {
    "Code": "1579",
    "Text": "Hydrologic Sciences"
  },
  {
    "Code": "7222",
    "Text": "XC-Crosscutting Activities Pro"
  },
  {
    "Code": "7643",
    "Text": "EnvS-Environmtl Sustainability"
  }
]

The top 5 words related to the topic 2 are: material new ha high broader
The abstract is:
The broader impact/commercial potential of this I-Corps project is the development of high-performance filters to
improve access to safe and reliable drinking water. Contaminated drinking water is a public health crisis affecting
hundreds o
The organization information is:
{
  "Code": "15030000",
  "Directorate": {
    "Abbreviation": "TIP",
    "LongName": "Dir for Tech, Innovation, & Partnerships"
  },
  "Division": {
    "Abbreviation": "TI",
    "LongName": "Translational Impacts"
  }
}
The program element information is:
{
  "Code": "8023",
  "Text": "I-Corps"
}

The top 5 words related to the topic 3 are: cell ha protein specie plant
The abstract is:
This project will improve understanding of an important class of proteins, the so-called receptor-like kinases. Like
cellular sentries, receptor-like kinases have crucial functions in sensing and orchestrating responses to environmental
cue
The organization information is:
{
  "Code": "08090000",
  "Directorate": {
    "Abbreviation": "BIO",
    "LongName": "Direct For Biological Sciences"
  },
  "Division": {
    "Abbreviation": "IOS",
    "LongName": "Division Of Integrative Organismal Systems"
  }
}
The program element information is:
{
  "Code": "1329",
  "Text": "Plant Genome Research Project"
}

The top 5 words related to the topic 4 are: theory quantum ha new model
The abstract is:
This research project will develop new statistical methods for program evaluation with the goal of improving their
reliability and scope in real-life applications. Program evaluation methods are widely used in a variety of disciplines
in th
The organization information is:
{
  "Code": "04050000",
  "Directorate": {
    "Abbreviation": "SBE",
    "LongName": "Direct For Social, Behav & Economic Scie"
  },
  "Division": {
    "Abbreviation": "SES",
    "LongName": "Divn Of Social and Economic Sciences"
  }
}
The program element information is:
[
  {
    "Code": "1320",
    "Text": "Economics"
  },
  {
    "Code": "1333",
    "Text": "Methodology, Measuremt & Stats"
  }
]

The top 5 words related to the topic 5 are: data ocean change ha model
The abstract is:
This award is funded in whole or in part under the American Rescue Plan Act of 2021 (Public Law 117-2).
&lt;br/&gt;&lt;br/&gt;The world’s marine ecosystems are currently experiencing many pressures from human activities. For
example, warmin
The organization information is:
{
  "Code": "06030000",
  "Directorate": {
    "Abbreviation": "GEO",
    "LongName": "Directorate For Geosciences"
  },
  "Division": {
    "Abbreviation": "EAR",
    "LongName": "Division Of Earth Sciences"
  }
}
The program element information is:
{
  "Code": "7222",
  "Text": "XC-Crosscutting Activities Pro"
}

The top 5 words related to the topic 6 are: stem program science education learning
The abstract is:
For nearly four decades, the National Science Foundation (NSF) has played a leadership role in provisioning advanced
cyberinfrastructure capabilities for the Nation's Science and Engineering (S&amp;E) researchers. An important component
in
The organization information is:
{
  "Code": "05090000",
  "Directorate": {
    "Abbreviation": "CSE",
    "LongName": "Direct For Computer & Info Scie & Enginr"
  },
  "Division": {
    "Abbreviation": "OAC",
    "LongName": "Office of Advanced Cyberinfrastructure (OAC)"
  }
}
The program element information is:
{
  "Code": "7781",
  "Text": "Leadership-Class Computing"
}

The top 5 words related to the topic 7 are: data ha covid19 social broader
The abstract is:
This award provides support to U.S. researchers participating in a project competitively selected by a 55-country
initiative on global change research through the Belmont Forum.  The Belmont Forum is a consortium of research funding
organiz
The organization information is:
{
  "Code": "06010000",
  "Directorate": {
    "Abbreviation": "GEO",
    "LongName": "Directorate For Geosciences"
  },
  "Division": {
    "Abbreviation": "RISE",
    "LongName": "Div of Res, Innovation, Synergies, & Edu"
  }
}
The program element information is:
[
  {
    "Code": "7222",
    "Text": "XC-Crosscutting Activities Pro"
  },
  {
    "Code": "7313",
    "Text": "Intl Global Change Res & Coord"
  }
]

The top 5 words related to the topic 8 are: data system learning ha model
The abstract is:
Trusted hardware is the foundation of cybersecurity. The International Symposium on Hardware-Oriented Security and Trust
(HOST) is a leading forum for hardware security researchers. This travel grant enables student researchers to attend th
The organization information is:
{
  "Code": "05050000",
  "Directorate": {
    "Abbreviation": "CSE",
    "LongName": "Direct For Computer & Info Scie & Enginr"
  },
  "Division": {
    "Abbreviation": "CNS",
    "LongName": "Division Of Computer and Network Systems"
  }
}
The program element information is:
{
  "Code": "8060",
  "Text": "Secure &Trustworthy Cyberspace"
}
```