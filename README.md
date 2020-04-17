# abYsis-toolkit
A toolkit to connect, download, analysis and stat data from abYsis.org  
v1.0 by Song Liyang
------------
** Read [LISENCE](/LISENCE) first.**
> You can read, download and run materials from this repositories only for your own personal, non-commercial use. You may NOT otherwise copy, reproduce, retransmit, distribute, publish, commercially exploit or otherwise transfer any material, nor may you modify or create derivatives works of the material. If you want any rights restricted in GNU v3, you should ask [songly(at)pku.edu.cn] for my agreement.  

** Disclaimer: you should read the statment from [abYsis.org](http://www.abysis.org/) first.**
> Companies are welcome to use this public version of abYsis, but need to be aware that this is not a secure server. After trialing the system, companies wishing to install a local version of abYsis, which can also store and analyse proprietary sequence and 3D structure data, may request a commercial licence.  
-------------
## Discription
This toolkit can read a list of protein sequence from a `.csv` file in a format of `[your protein name] , [Amino acid sequence]`.  
The amino acid sequences are sent to [abYsis.org](http://www.abysis.org/)  one by one one (equivalent to submitting `Key Annotation` form).  
After abYsis finished analysis, data of every aa sequence entry was fetched, organized and exported to a `./data/[your protein name].csv` file.  
All this data files can be summarized by [data_stat.py](/data_stat.py) in a format of:  
`'your protein name', 'aa_seq','rare 1%','FR 1%', 'CDR 1%', 'outstand 1%','rare 3%','FR 3%', 'CDR 3%', 'outstand 3%'`  
The number of rare amino acid in some features (low frequency, FR or CD, outstanding aa) is calculated if you specified a low frequency threshold of 1% (`threshold1 = 1`) and 3% (`threshold2 = 3`).  

## Usage
