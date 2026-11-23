# Why Does ChatGPT "Delve" So Much? Exploring the Sources of Lexical Overrepresentation in Large Language Models

This repository contains the code and data of the paper "Why Does ChatGPT "Delve" So Much? Exploring the Sources of Lexical Overrepresentation in Large Language Models".

## Abstract
Scientific English is currently undergoing rapid change, with words like "delve," "intricate," and "underscore" appearing far more frequently than just a few years ago. It is widely assumed that scientists' use of large language models (LLMs) is responsible for such trends. We develop a formal, transferable method to characterize these linguistic changes. Application of our method yields 21 focal words whose increased occurrence in scientific abstracts is likely the result of LLM usage. We then pose "the puzzle of lexical overrepresentation": WHY are such words overused by LLMs? We fail to find evidence that lexical overrepresentation is caused by model architecture, algorithm choices, or training data. To assess whether reinforcement learning from human feedback (RLHF) contributes to the overuse of focal words, we undertake comparative model testing and conduct an exploratory online study. While the model testing is consistent with RLHF playing a role, our experimental results suggest that participants may be reacting differently to "delve" than to other focal words. With LLMs quickly becoming a driver of global language change, investigating these potential sources of lexical overrepresentation is important. We note that while insights into the workings of LLMs are within reach, a lack of transparency surrounding model development remains an obstacle to such research.

## Citation

If you use this code or data, a citation is appreciated (though not required; see the licence).

```bibtex
@inproceedings{juzek-ward-2025-delve,
  title     = {Why Does ChatGPT "Delve" So Much? Exploring the Sources of Lexical Overrepresentation in Large Language Models},
  author    = {Juzek, Tom S. and Ward, Zina B.},
  booktitle = {Proceedings of the 31st International Conference on Computational Linguistics (COLING 2025)},
  year      = {2025},
  pages     = {6397--6411},
  url       = {https://aclanthology.org/2025.coling-main.426/}
}
```

## Repository Contents

- **data/**: Contains sample data. Actual data files are hundred of gigabytes big, and have to be built locally with the code in /code/get_human_data/ and /other_datasets/. 
- **code/**: Python scripts used for the extraction of focal words (brute_force_div.py and incl.ods in /analysis/), model testing (PPAID_calc_normalised_entropy_with_llama.ipynb in /analysis/), and generating AI abstracts (in /generate_ai_data/). Plots can be generated with the code in /plot/ and the code for the experimental website can be found in /website/. 

### Requirements and running the code

- Python 3.9+
- Install required packages via pip

## Licence

- **Code** (`code/`): MIT No Attribution (MIT-0). See [`LICENSE`](LICENSE). Use it freely, no attribution required.
- **Data** (`data/`): CC0 1.0 Universal (public domain dedication). See [`LICENSE-DATA`](LICENSE-DATA).

**Note on data.** The files in `data/` are small samples of PubMed abstracts, included for research. The full datasets are not redistributed here; they are rebuilt locally from PubMed, arXiv, and Wikipedia using the scripts in `code/get_human_data/` and `code/other_datasets/`. The CC0 dedication covers our own contributions (the focal-word analyses, generated abstracts, tables, plots, and the rating-study code); the underlying source texts remain under their respective terms.

The included paper PDF remains under its own terms (CC BY 4.0; COLING 2025, ACL Anthology), separate from the code and data licences above.

## AI Assistance

Repository polished with Claude Code.

## Contact
For any questions or issues, please contact Tom Juzek or Zina Ward.
