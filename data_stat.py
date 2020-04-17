import os
import pandas as pd


# all varies should be specified
SAVEFILE = "D://abysis_output//20200319_1//20200319_1_summary.csv"     # output csv path and name e.g. "D://abysis_output//test//summary.csv"
DATADIR = "D://abysis_output//20200319_1//data"     # Your data dir with working file e.g. "D://abysis_output//test//data"
threshold1 = 1      # percentage, e.g. 5 for under 5%
threshold2 = 3      # percentage, e.g. 5 for under 5%

filelist = os.listdir(DATADIR)

def freq_filter(df,threshold):
    fr = 0
    cdr = 0
    max = 0
    aa = ""
    for idx, row in df.iterrows():
        aa += row['residues']
        if row['frequencies'] < threshold and (row['regions'].startswith('HFR') or row['regions'].startswith('LFR')):
            fr += 1
        if row['frequencies'] < threshold and row['regions'].startswith('CDR'):
            cdr += 1
        if row['frequencies'] < threshold and row['max_residual_ratio'] > 0.5 :
            max += 1
    return fr,cdr,max,aa

outputdf = pd.DataFrame(columns=('Entry name', 'aa_seq','rare 1%','FR 1%', 'CDR 1%', 'outstand 1%','rare 3%','FR 3%', 'CDR 3%', 'outstand 3%'))

i = 0
for file in filelist:
    print(f"processing csv file {file}")
    df = pd.read_csv(f'{DATADIR}//{file}', header=0)
    # print(df)
    fr1, cdr1, max1, aa1 = freq_filter(df, threshold1)
    fr2, cdr2, max2, aa2 = freq_filter(df, threshold2)
    outputdf.loc[i] = (file, aa1, fr1 + cdr1, fr1, cdr1, max1, fr2 + cdr2, fr2, cdr2, max2)
    i += 1

outputdf.to_csv(f'{SAVEFILE}', index=False)
print(f"csv file saved as {SAVEFILE}")