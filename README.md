# abYsis-toolkit
A toolkit to bulk-submission, download, analysis and summarizing data from [abYsis.org](http://www.abysis.org/)  
https://github.com/Song-Liyang/abYsis-toolkit  
This program was written by Song Liyang (songly@pku.edu.cn), Peking University.

abYsis is a famous web-based antibody research system that includes an integrated database of antibody sequence and structure data. It's very useful for antibody research when we want a quick homology search and annotation of a antibody sequences using the Blast algorithm.   
With the lack of API sockets for this platform, here is a toolkit to query, download, parse and stat the data from abYsis.  

**Read [LISENCE](/LISENCE) first.**
> You can read, download and run materials from this repositories only for your own personal, non-commercial use. You may NOT otherwise copy, reproduce, retransmit, distribute, publish, commercially exploit or otherwise transfer any material, nor may you modify or create derivatives works of the material. If you want any rights restricted in GNU v3, you should ask [songly(at)pku.edu.cn] for my agreement.  

**Disclaimer: you should read the statment from [abYsis.org](http://www.abysis.org/) first.**
> Companies are welcome to use this public version of abYsis, but need to be aware that this is not a secure server. After trialing the system, companies wishing to install a local version of abYsis, which can also store and analyse proprietary sequence and 3D structure data, may request a commercial licence.  

## Discription
##### Input
Firstly, [abysis_main.py](./abysis_main) will read a list of protein sequence from a `.csv` file in a format of `[your protein name] , [Amino acid sequence]` for each entry.  
##### Query to abYsis
The amino acid sequences are then sent to [abYsis.org](http://www.abysis.org/)  one by one one (equivalent to submitting "Key Annotation" form in browser).  
Numbering scheme and CDR region definition can be specified by`NUMBERING_SCHEME` and `CDR_REGION` in [abysis_main.py](./abysis_main), all five Numbering scheme/CDR definitions are supported here:
- Numbering scheme: Kabat, Chothia, Martin, IMGT, Aho
- CDR regions: Kabat, Chothia, AbM, Contact, IMGT

>For definitions, see [manual from abysis.org](http://www.abysis.org/help/index.html) (About Definitions > Numbering Schemes).  

#### Data extraction and saving
After abYsis finished analysis, data of every aa sequence entry was fetched, organized and exported to a `./data/[your protein name].csv` file.  

Each `.csv` data file shows features of every amino acid sequencially. The features contains:
1. residues: amino acid residue.
2. scheme_number: position numbering of certain schemes.
3. regions: CDR or FR region name.
4. frequencies: frequencies of each amino acid.
5. max_residues: residue with max frequency at this position
6. max_residual_ratio: the frequency of residue with max frequency at this position  
(the max_residues is the most outstanding residue of "Distribution for position" histogram)  

#### Data summary
All this data files exported by [abysis_main.py](./abysis_main) can be summarized by [data_stat.py](./data_stat.py).  

For each protein data file, the number of rare amino acid in some features (like low frequency, HFR/LFR or CDR, outstanding aa) is calculated if you specified a low frequency threshold of 1% (`threshold1 = 1`) and 3% (`threshold2 = 3`).  
The output `.csv` file shows counts of:  
`'your protein name', 'aa_seq','rare 1%','FR 1%', 'CDR 1%', 'outstand 1%','rare 3%','FR 3%', 'CDR 3%', 'outstand 3%'`  

## Usage
abYsis-toolkit need WebDriver to connect with abYsis server. Please check your Chrome browser version and download related [ChromeDriver](https://chromedriver.chromium.org/) to your Python directory.  

Download all files from this repository(https://github.com/Song-Liyang/abYsis-toolkit).    

Prepare your input `.csv` file in a format of `[your protein name] , [Amino acid sequence]` for each entry and put in a new working directory.  
This toolkit was not packed into executable command line, please feel free to specify parameters in the script.

Before running [abysis_main.py](./abysis_main), please specify parameters below:
```
# all varies should be specified
FILEDIR = "D://abysis_output//test"     # Your working dir with input file e.g. "D://abysis_output//test"
INPUT = "input.csv"         # Your input file name e.g. "input.csv"
NUMBERING_SCHEME = "kabat"                    # Numbering Scheme name, lowercase
CDR_REGION = "kabat"                          # CDR_region definition, lowercase
```
Output files will be saved at "data" folder in your `FILEDIR` folder, named by input.    

For summarizing the output files, please specify parameters below and run [data_stat.py](./data_stat.py).
```
# all varies should be specified
SAVEFILE = "D://abysis_output//test//summary.csv"  # output csv path and name e.g. "D://abysis_output//test//summary.csv"
DATADIR = "D://abysis_output//test//data"          # Your data dir with working file e.g. "D://abysis_output//test//data"
threshold1 = 1      # percentage, e.g. 5 for under 5%
threshold2 = 3      # percentage, e.g. 5 for under 5%
```
The counts of amino acids with under-threshold-frequency will be summarized in `SAVEFILE`.

***If you need any help or want to fork this repository for other usage, please contact me!***
