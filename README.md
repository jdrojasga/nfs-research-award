# nfs-research-award
Repository with the classification of abstracts from the NFS in order to solve the technical test to be part of Globant.

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