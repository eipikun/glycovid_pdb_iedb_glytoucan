# Program of analysing IEDB - GlyTouCan mapped data to COVID19 featured PDB
## Analysis Steps
### Step 0(optional)
You are required to install those module to execute analysis.py in advance.
- beautifulsoup4==4.10.0
- certifi==2021.5.30
- charset-normalizer==2.0.6
- idna==3.2
- numpy==1.21.2
- pandas==1.3.3
- python-dateutil==2.8.2
- pytz==2021.1
- requests==2.26.0
- six==1.16.0
- soupsieve==2.2.1
- urllib3==1.26.7

version information is stored in requirements.txt
to make virtual enviroment with those module above, please execute the commands below.
```
python3 -m venv venv
```
```
. venv/bin/activate
```
```
pip3 install -r requirements.txt
```

### Function 1(pdb_iedb_mapping)
#### You would be able to get two files
- iedb_pdb_relation.csv : inclusive relationdata (COVID19 featured PDB data and IEDB epitope)
- iedb_pdb_relation_covid.csv : epitope id data mapped to pdb(COVID19 featured)

### Function 2(pdb_covid19_to_iedb_with_glytoucan)
print iedb epitope data linked to GlyTouCan and COVID19 featured pdb relation
※On the day commited, data is not found