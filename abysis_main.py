
import os
import pandas as pd
from multiprocessing import Pool, cpu_count

from abysis.data_extractor import data_fetch, data_analyse
from abysis.web_scraper import get_driver, connect_to_base,write_to_file

# all varies should be specified
FILEDIR = "D://abysis_output//test"     # Your working dir with input file e.g. "D://abysis_output//test"
INPUT = "input.csv"         # Your input file name e.g. "input.csv"
NUMBERING_SCHEME = "kabat"                    # Numbering Scheme name, lowercase
CDR_REGION = "kabat"                          # CDR_region definition, lowercase


def input_reader(input_filename):
    df = pd.read_csv(f'{FILEDIR}//{input_filename}',header=None)
    input_zip = zip(df[0],df[1])
    return input_zip

def run_process(aa_id, aa_sequence):
    browser = get_driver()
    connect_return = connect_to_base(browser, aa_sequence, aa_id)
    if connect_return[0]:
        # sleep(2)
        # html = browser.page_source
        idnum = connect_return[1]
        browser.quit()
        fetch = data_fetch(idnum, aa_id, aa_sequence, NUMBERING_SCHEME, CDR_REGION)
        if fetch[0]:
            output_df = data_analyse(fetch[1], CDR_REGION)
            write_to_file(output_df, aa_id, FILEDIR)
        else:
            print(f'Error fetching data from abysis, aa_id= {aa_id}, aa_seq={aa_sequence}')

    else:
        print(f'Error connecting to abysis, aa_id= {aa_id}')
        browser.quit()

if __name__ == '__main__':
    # set variables

    os.makedirs(f'{FILEDIR}//data', exist_ok=True)
    input_zip = input_reader(INPUT)
    # scrape and crawl
    with Pool(cpu_count()-1) as p:
        p.starmap(run_process, input_zip)
    p.close()
    p.join()
