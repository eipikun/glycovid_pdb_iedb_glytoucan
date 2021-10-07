import pandas as pd
import csv

def pdb_iedb_mapping():
    array_pdb = []
    array_iedb = []
    dict_iedb = {}
    df = pd.read_csv(r"./data/iedb_map.csv", header = 0)
    cols = ['pdb', 'epitope']
    result_df = pd.DataFrame(index=[])

    # get mapping data(PDB to Epitope ID Maps) from https://www.iedb.org/database_export_v3.php
    with open('./data/iedb_map.csv') as f:
        for row in csv.reader(f):
            array_iedb.append(str(row[0]).upper())
            dict_iedb[row[0]] = row[1]
    

    # get CSV data from https://github.com/eipikun/glycovid_pdb_analysis
    with open('./data/pdbj_pdbe_relation.csv') as f:
        for row in csv.reader(f):
            array_pdb.append(row[0])

    dict_inclusion = {}
    covid_related_data = []
    for pdb in array_pdb:
        if pdb not in array_iedb:
            dict_inclusion[pdb] = 'not in iedb but in pdb'
            
    
    for iedb in array_iedb:
        if iedb not in array_pdb:
            dict_inclusion[iedb] = 'not in pdb but in iedb'
        else:
            dict_inclusion[iedb] = 'in both iedb and in pdb'
            if 'pdb' in result_df.columns:
                if len(result_df.loc[result_df['pdb'] == str(iedb).lower()]) > 0:
                    pass
                else:
                    matched_df = df[df['pdb'] == str(iedb).lower()]
                    result_df = result_df.append(matched_df, ignore_index = True)
            else:
                matched_df = df[df['pdb'] == str(iedb).lower()]
                result_df = result_df.append(matched_df, ignore_index = True)
                
    df = pd.DataFrame.from_dict(dict_inclusion, orient = 'index').rename(columns = {0: 'Type'})
    df.to_csv('./data/iedb_pdb_relation.csv')
    result_df.to_csv('./data/iedb_pdb_relation_covid.csv')

def get_iedb_df():
    df = pd.read_csv(r"./iedb_map.csv", header = 0)
    print(df)

def pdb_covid19_to_iedb_with_glytoucan():
    # load Epitope list mapped to COVID19 featured PDB
    # make modefied_pdb_iedb.csv file from iedb_pdb_relation_covid.csv by formatting [epitope, pdb] csv
    # ex)
    # epitope, pdb
    # 997006, 6w41
    # 1310987, 6wps
    # 1310987, 6wpt
    pdb_epitope_df = pd.read_csv(r"./modified_pdb_iedb.csv", header = 0)
    # load Epitope - GlyTouCan mapping data()
    # ex)
    # epitope, glytoucan_id
    # 112871,G71142DF
    # 114066,G11009BX
    # 114701,G53308XG
    epitope_glytoucan_df = pd.read_csv(r"./data/epitope_id_glytoucan_id.csv", header = 0)
    df = pd.merge(pdb_epitope_df, epitope_glytoucan_df, on='epitope')
    print(df)


#pdb_iedb_mapping()
# get_iedb_df()
# pdb_covid19_to_iedb_with_glytoucan()