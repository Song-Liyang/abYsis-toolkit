
import requests
import hjson
import time

def data_fetch(idNum, aa_id, aa_sequence, CDR_REGION):
    "Download and parse the data, save to a csv file"
    # 请求数据
    numUrl = 'http://home.stagleys.co.uk/abysis/sequence_input/key_annotation/numberingPanel.cgi'
    numForm = f"uid=ID{idNum}&selectedColour=Taylor&scheme_name={CDR_REGION}&region_def_name={CDR_REGION}&format=summary_format&aa_sequence={aa_sequence}&organism_id=not_selected"
    # heatmapUrl = 'http://home.stagleys.co.uk/abysis/sequence_input/key_annotation/heatmapPanel.cgi'
    # heatmapForm = f"uid=ID{idNum}&selectedColour=Taylor&scheme_name={CDR_REGION}&region_def_name={CDR_REGION}&scaled=0&distribution_target=ID{idNum}_heatmapdistribution&aa_sequence={aa_sequence}&organism_id=not_selected&organism_id2=31"
    connection_attempts = 0
    while connection_attempts < 10:
        try:
            numRes = requests.post(numUrl, data=numForm).text.splitlines()
            # heatmapRes = requests.post(heatmapUrl, data=heatmapForm).text.splitlines()
            print(f"{aa_id} (Request ID {idNum} ) data fetched", time.ctime())
            return True,numRes
        except Exception as ex:
            connection_attempts += 1
            print(f'Error fetching data of {aa_id} (Request ID {idNum} )')
            print(f'Attempt #{connection_attempts}.')
    return False,connection_attempts

def data_analyse(numRes, CDR_REGION):
    # residues extract
    for line in numRes:
        if line.startswith("var residues = "):
            match = line.lstrip("var residues = ").rstrip(";")
            residues = hjson.loads(match)

    # schemeNumber extract, use "CDR_REGION" for para
    for line in numRes:
        if line.startswith("var schemeNumbers = "):
            match = line.lstrip("var schemeNumbers = ").rstrip(";")
            schemeDict = hjson.loads(match)
    scheme = schemeDict[f"{CDR_REGION}"]

    # cdrRegion extract, use "CDR_REGION" for para
    for line in numRes:
        if line.startswith("var regions = "):
            match = line.lstrip("var regions = ").rstrip(";")
            regionsDict = hjson.loads(match)
    for entry in regionsDict:
        if entry['region_def_name'] == f"{CDR_REGION}":
            regions = entry['cdrRegion']

    # Frequencies extract
    for line in numRes:
        if line.startswith("var frequencies = "):
            match = line.lstrip("var frequencies = ").rstrip(";")
            freqsDict = hjson.loads(match)
    for entry in freqsDict:
        if entry['schemename'] == f"{CDR_REGION}":
            freqs = entry['freqs']

    # Frequencies extract
    for line in numRes:
        if line.startswith("var resFrequencies = "):
            match = line.lstrip("var resFrequencies = ").rstrip(";")
            resfreqsDict = hjson.loads(match)
    resfreqsDict = hjson.loads(match)
    for entry in resfreqsDict['org1']:
        if entry['scheme_name'] == f"{CDR_REGION}":
            resfreqs = entry['frequencies']

    # list max frequent residuals in distribution

    for site in resfreqs:
        total = site['total']
        countDict = site['counts']
        Max = countDict[0]['c']
        Maxaa = countDict[0]['aa']
        for i in countDict:
            if i['c'] > Max:
                Max = i['c']
                Maxaa = i['aa']
        site['maxfreqs'] = Max / total
        site['maxaa'] = Maxaa

    maxPercentage = [site['maxfreqs'] for site in resfreqs]
    maxResiduals = [site['maxaa'] for site in resfreqs]
    df = {'residues':residues, 'scheme_number':scheme, 'regions':regions, 'frequencies':freqs, 'max_residuals':maxResiduals, 'max_residual_ratio':maxPercentage}

    return df