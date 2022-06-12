# Just another EDI Parser

[![Python - 3.9.0+](https://img.shields.io/badge/Python-3.9.0%2B-orange)](https://www.python.org/downloads/release/python-390/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/freestream/pyedi)
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/freestream/pyedi)

### PyEdi: a lightweight EDI file parser

This package provides a simple-to-use Python interface to convert the obscure EDI file format into a structured dict.
This parser just simple delivers a basic JSON object with information found in each EDI file. No inturpitabion of each segment will be done.

### Usage
To parse an EDI file simply execute the `parse_file` function.
```python
import json
from pyedi import parse_file
from pyedi.settings import Settings

transaction_sets = parse_file('./my_edi_file.txt', Settings())
print(json.dump(transaction_sets))
```

To parse an EDI string simply execute the `parse_str` function.
```python
import json
from pyedi import parse_str
from pyedi.settings import Settings

transaction_set = parse_str('ST*835*1234~BPR*I*1922.86*C*CHK************20110108~TRN*1*02790758*560894904~REF*F2*LCLA438D~DTM*405*20110104~N1*PR*BLUE CROSS AND BLUE SHIELD OF NORTH CAROLINA~N3*P O BOX 2291~N4*DURHAM*NC*27702~PER*CX*TE*8005554844~N1*PE*XYZ HEALTHCARE CORPORATION*XX*0987654321~N3*P O BOX XYZ~N4*CHARLOTTE*NC*28234~REF*TJ*123456789~LX*1~CLP*200200964A52*1*2100*1922.86*142.54*15*94151100100~NM1*QC*1*Dough*Mary****MI* YPB123456789001~DTM*050*20110103~SVC*HC:59430*1210*1057.86**1*HC:59410~DTM*472*20101231~CAS*CO*42*34.6~CAS*PR*2*117.54~REF*6R*0001~AMT*B6*1175.4~SVC*HC:59440*890*865**1*HC:59410~DTM*472*20101231~CAS*PR*3*25~REF*6R*0002~SVC*HC:59426******742*742**1~DTM*472*20101231~REF*6R*0003~AMT*B6*742~SE*33*1234~', Settings())

print(json.dump(transaction_set))
```

### Tests
Example EDI 835 files can be found in `tests/files`. To run the tests use `pytest`.
```
python -m pytest
```
