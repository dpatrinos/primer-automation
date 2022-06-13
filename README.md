
# primer-automation
[![Github All Releases](https://img.shields.io/github/downloads/dpatrinos/primer-automation/total.svg)]()
[![MIT License](https://img.shields.io/badge/license-MIT-blue)](https://github.com/dpatrinos/primer-automation/blob/main/LICENSE)

A python-based script that uses the NCBI Rat Genome Database v6.0 to create .fasta files for the nucleotide sequences of novel exon pairs

## Getting Started

Import data from Box (protected) to ~/ then run the following in terminal:

```bash
  git clone https://github.com/dpatrinos/primer-automation.git
  cd primer-automation
  pip install -r requirements.txt
  mv ~/data ~/primer-automation/
```

Run script from project directory:
```bash
  python script.py
```

## Acknowledgements

 - [National Center for Biotechnology Information](https://www.ncbi.nlm.nih.gov/data-hub/taxonomy/10116/)
 - Emma Aldrich and Lauren Shelby, Project Splice: Analyzing the Effect of Diet and Estrogen on mRNA Alternative Splicing in Rats, September 2021.
 - Jacob S. Roberts, Ron A. Perets, Kathryn S. Sarfert, John J. Bowman, Patrick A. Ozark, Gregg B. Whitworth, Sarah N. Blythe, and Natalia Toporikova, High-fat high-sugar diet induces polycystic ovary syndrome in a rodent model, *Biology of Reproduction*, Volume 96, Issue 3, March 2017, Pages 551–562, https://doi.org/10.1095/biolreprod.116.142786
 - Washington and Lee University Summer Research Scholars Program, Lexington, VA

## License
primer-automation is released under an [MIT](https://github.com/dpatrinos/primer-automation/blob/main/LICENSE) license.

