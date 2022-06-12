import os
from pyedi import parse_file, parse_str
from pyedi.settings import Settings

current_path = os.path.dirname(os.path.abspath(__file__))


def test_parse_str():
    transaction_set = parse_str('ST*835*1234~BPR*I*1922.86*C*CHK************20110108~TRN*1*02790758*560894904~REF*F2*LCLA438D~DTM*405*20110104~N1*PR*BLUE CROSS AND BLUE SHIELD OF NORTH CAROLINA~N3*P O BOX 2291~N4*DURHAM*NC*27702~PER*CX*TE*8005554844~N1*PE*XYZ HEALTHCARE CORPORATION*XX*0987654321~N3*P O BOX XYZ~N4*CHARLOTTE*NC*28234~REF*TJ*123456789~LX*1~CLP*200200964A52*1*2100*1922.86*142.54*15*94151100100~NM1*QC*1*Dough*Mary****MI* YPB123456789001~DTM*050*20110103~SVC*HC:59430*1210*1057.86**1*HC:59410~DTM*472*20101231~CAS*CO*42*34.6~CAS*PR*2*117.54~REF*6R*0001~AMT*B6*1175.4~SVC*HC:59440*890*865**1*HC:59410~DTM*472*20101231~CAS*PR*3*25~REF*6R*0002~SVC*HC:59426******742*742**1~DTM*472*20101231~REF*6R*0003~AMT*B6*742~SE*33*1234~', Settings())

    assert 'ST' in transaction_set, 'Missing ST segment in transaction'

    transaction_set = transaction_set['ST']

    assert len(transaction_set) == 1, 'Too many ST transactions'

def test_parse_file1():
    transaction_sets = parse_file(
        current_path + '/files/file1.txt', Settings())

    assert len(transaction_sets) == 1, 'Too many transactions'

    transaction_set = transaction_sets[0]

    assert 'ST' in transaction_set, 'Missing ST segment in transaction'

    transaction_set = transaction_sets[0]['ST']

    assert len(transaction_set) == 1, 'Too many ST transactions'


def test_parse_file2():
    transaction_sets = parse_file(
        current_path + '/files/file2.txt', Settings())

    assert len(transaction_sets) == 1, 'Too many transactions'

    transaction_set = transaction_sets[0]

    assert 'ISA' in transaction_set, 'Missing ISA segment in transaction'

    transaction_set = transaction_sets[0]['ISA']

    assert len(transaction_set) == 1, 'Too many ISA transactions'


def test_parse_file3():
    transaction_sets = parse_file(
        current_path + '/files/file3.txt', Settings())

    assert len(transaction_sets) == 1, 'Too many transactions'

    transaction_set = transaction_sets[0]

    assert 'ISA' in transaction_set, 'Missing ISA segment in transaction'

    transaction_set = transaction_sets[0]['ISA']

    assert len(transaction_set) == 1, 'Too many ISA transactions'


def test_parse_file4():
    transaction_sets = parse_file(
        current_path + '/files/file4.txt', Settings())

    assert len(transaction_sets) == 1, 'Too many transactions'

    transaction_set = transaction_sets[0]

    assert 'ISA' in transaction_set, 'Missing ISA segment in transaction'

    transaction_set = transaction_sets[0]['ISA']

    assert len(transaction_set) == 1, 'Too many ISA transactions'


def test_parse_file5():
    transaction_sets = parse_file(
        current_path + '/files/file5.txt', Settings())

    assert len(transaction_sets) == 1, 'Too many transactions'

    transaction_set = transaction_sets[0]

    assert 'ST' in transaction_set, 'Missing ST segment in transaction'

    transaction_set = transaction_sets[0]['ST']

    assert len(transaction_set) == 1, 'Too many ST transactions'


def test_parse_file214():
    transaction_sets = parse_file(
        current_path + '/files/214.txt', Settings())

    assert len(transaction_sets) == 1, 'Too many transactions'

    transaction_set = transaction_sets[0]

    assert 'ISA' in transaction_set, 'Missing ISA segment in transaction'

    transaction_set = transaction_sets[0]['ISA']

    assert len(transaction_set) == 1, 'Too many ISA transactions'


def test_parse_file315():
    transaction_sets = parse_file(
        current_path + '/files/315.txt', Settings())

    assert len(transaction_sets) == 1, 'Too many transactions'

    transaction_set = transaction_sets[0]

    assert 'ISA' in transaction_set, 'Missing ISA segment in transaction'

    transaction_set = transaction_sets[0]['ISA']

    assert len(transaction_set) == 1, 'Too many ISA transactions'


def test_parse_file810():
    transaction_sets = parse_file(
        current_path + '/files/810.txt', Settings())

    assert len(transaction_sets) == 1, 'Too many transactions'

    transaction_set = transaction_sets[0]

    assert 'ISA' in transaction_set, 'Missing ISA segment in transaction'

    transaction_set = transaction_sets[0]['ISA']

    assert len(transaction_set) == 1, 'Too many ISA transactions'


def test_parse_file820():
    transaction_sets = parse_file(
        current_path + '/files/820.txt', Settings())

    assert len(transaction_sets) == 1, 'Too many transactions'

    transaction_set = transaction_sets[0]

    assert 'ISA' in transaction_set, 'Missing ISA segment in transaction'

    transaction_set = transaction_sets[0]['ISA']

    assert len(transaction_set) == 1, 'Too many ISA transactions'
