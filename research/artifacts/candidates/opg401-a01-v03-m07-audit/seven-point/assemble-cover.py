"""Reassemble readable certificate rows; no search or mathematical trust claim."""
import hashlib
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
DIGESTS=[
'47363ec50eb404b032e5d41ae05a959f39e47a50989f0ac04f5875367a72f6cc',
'a9994817b0b08ff8da1bc03fe9f54d8f07ba30873eb8f7d61b9efa2b62ec12ba',
'88dd835bb14d356323373a5ba6fda946e7276ff50e6338759d03cfde1e92ef1d',
'35f861efdd1b04259008e35d576a7879fef53b36ade2b8621861cc8b60518026',
'f8525d3cd55b7f56f5c48763946ad094304ecf6ac2658d6886e123acd910c0d2']
EXPECTED='481592caf5b356242a393caaf58294872afbe131049c8fe0575dcddcb492413b'
rows=[]
for i,digest in enumerate(DIGESTS,1):
    raw=(ROOT/f'cover-part-{i}.json').read_bytes()
    if hashlib.sha256(raw).hexdigest()!=digest:raise ValueError('certificate part digest mismatch')
    part=json.loads(raw)
    if len(part)!=(26 if i<5 else 25):raise ValueError('certificate part row count')
    rows.extend(part)
d={'verdict':'candidate_only','encoding':'row=[n,edge_mask,witnesses]; edge bits use combinations(range(n),2); witness=bad_boundary_index:base20_vertex_colors; outside order=P,Q,R,S; alphabet=0123456789abcdefghij',
'bad_boundaries':[[0,0,0,0],[0,0,0,1],[0,0,0,2],[0,0,1,1],[0,0,2,1],[0,0,19,1],[1,0,2,0],[1,0,2,1],[7,0,19,1],[8,0,0,1],[14,0,2,0],[14,0,2,1]],'covers':rows}
raw=(json.dumps(d,separators=(',',':'))+'\n').encode()
if hashlib.sha256(raw).hexdigest()!=EXPECTED:raise ValueError('assembled certificate digest mismatch')
p=ROOT/'cover.json'
if p.exists() and p.read_bytes()!=raw:raise FileExistsError('refusing to overwrite a different certificate')
if not p.exists():p.write_bytes(raw)
print(json.dumps({'assembled_bytes':len(raw),'sha256':EXPECTED,'rows':len(rows),'verdict':'candidate_only'}))
