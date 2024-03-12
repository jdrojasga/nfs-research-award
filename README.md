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

In order to not have the [dataset](https://www.nsf.gov/awardsearch/download?DownloadFileName=2020&All=true) used in this technical test in the online repo, we are putting the dataset inside the repo folder, but we are excluding the folder `\dataset` from the git flow. If you decide to put a different name please add the name in the Dataset section.