# inspire-hep
Fetch citations and self-excluded citations for each article listed in `mypub.py`, create bibtex file `mypub.bib`, and create a csv files with columns of `texkeys, arxiv_eprints, preprint_date, citation_count, citation_count_without_self_citations, doi, title`.

## Instructions: 
* write down the HEP Inspire-ID in `mypub.py`
* run `python update.py`
It will produce two files `mypub.bib` and `mypub.csv`.

## Get bib
```bash
python get_bib.py test_bib.txt
```

## Example of json file from Inspire-API
```json
launching API: https://inspirehep.net/api/literature/1851403
{ 'created': '2021-03-15T00:00:00+00:00',
  'id': '1851403',
  'links': { 'bibtex': 'https://inspirehep.net/api/literature/1851403?format=bibtex',
             'citations': 'https://inspirehep.net/api/literature/?q=refersto%3Arecid%3A1851403',
             'json': 'https://inspirehep.net/api/literature/1851403?format=json',
             'latex-eu': 'https://inspirehep.net/api/literature/1851403?format=latex-eu',
             'latex-us': 'https://inspirehep.net/api/literature/1851403?format=latex-us'},
  'metadata': { '$schema': 'https://inspirehep.net/schemas/records/hep.json',
                'abstracts': [ { 'source': 'Springer',
                                 'value': 'The Exa.TrkX project has applied '
                                          'geometric learning concepts such as '
                                          'metric learning and graph neural '
                                          'networks to HEP particle tracking. '
                                          'Exa.TrkX’s tracking pipeline groups '
                                          'detector measurements to form track '
                                          'candidates and filters them. The '
                                          'pipeline, originally developed '
                                          'using the TrackML dataset (a '
                                          'simulation of an LHC-inspired '
                                          'tracking detector), has been '
                                          'demonstrated on other detectors, '
                                          'including DUNE Liquid Argon TPC and '
                                          'CMS High-Granularity Calorimeter. '
                                          'This paper documents new '
                                          'developments needed to study the '
                                          'physics and computing performance '
                                          'of the Exa.TrkX pipeline on the '
                                          'full TrackML dataset, a first step '
                                          'towards validating the pipeline '
                                          'using ATLAS and CMS data. The '
                                          'pipeline achieves tracking '
                                          'efficiency and purity similar to '
                                          'production tracking algorithms. '
                                          'Crucially for future HEP '
                                          'applications, the pipeline benefits '
                                          'significantly from GPU '
                                          'acceleration, and its computational '
                                          'requirements scale close to '
                                          'linearly with the number of '
                                          'particles in the event.'},
                               { 'source': 'arXiv',
                                 'value': 'The Exa.TrkX project has applied '
                                          'geometric learning concepts such as '
                                          'metric learning and graph neural '
                                          'networks to HEP particle tracking. '
                                          "Exa.TrkX's tracking pipeline groups "
                                          'detector measurements to form track '
                                          'candidates and filters them. The '
                                          'pipeline, originally developed '
                                          'using the TrackML dataset (a '
                                          'simulation of an LHC-inspired '
                                          'tracking detector), has been '
                                          'demonstrated on other detectors, '
                                          'including DUNE Liquid Argon TPC and '
                                          'CMS High-Granularity Calorimeter. '
                                          'This paper documents new '
                                          'developments needed to study the '
                                          'physics and computing performance '
                                          'of the Exa.TrkX pipeline on the '
                                          'full TrackML dataset, a first step '
                                          'towards validating the pipeline '
                                          'using ATLAS and CMS data. The '
                                          'pipeline achieves tracking '
                                          'efficiency and purity similar to '
                                          'production tracking algorithms. '
                                          'Crucially for future HEP '
                                          'applications, the pipeline benefits '
                                          'significantly from GPU '
                                          'acceleration, and its computational '
                                          'requirements scale close to '
                                          'linearly with the number of '
                                          'particles in the event.'}],
                'arxiv_eprints': [ { 'categories': [ 'physics.data-an',
                                                     'cs.LG',
                                                     'hep-ex'],
                                     'value': '2103.06995'}],
                'authors': [ { 'affiliations': [ { 'record': { '$ref': 'https://inspirehep.net/api/institutions/902953'},
                                                   'value': 'LBL, Berkeley'}],
                               'affiliations_identifiers': [ { 'schema': 'GRID',
                                                               'value': 'grid.184769.5'}],
                               'full_name': 'Ju, Xiangyang',
                               'ids': [ { 'schema': 'ORCID',
                                          'value': '0000-0002-9745-1638'},
                                        { 'schema': 'INSPIRE BAI',
                                          'value': 'X.Ju.1'}],
                               'raw_affiliations': [ { 'value': 'Lawrence '
                                                                'Berkeley '
                                                                'National '
                                                                'Laboratory, '
                                                                'Berkeley, CA, '
                                                                'USA'}],
                               'record': { '$ref': 'https://inspirehep.net/api/authors/1071841'},
                               'signature_block': 'Jx',
                               'uuid': '054497e0-aa77-4517-b0af-445ab505b46b'},
                             { 'affiliations': [ { 'record': { '$ref': 'https://inspirehep.net/api/institutions/902953'},
                                                   'value': 'LBL, Berkeley'}],
                               'affiliations_identifiers': [ { 'schema': 'GRID',
                                                               'value': 'grid.184769.5'}],
                               'full_name': 'Murnane, Daniel',
                               'ids': [ { 'schema': 'INSPIRE BAI',
                                          'value': 'D.Murnane.1'}],
                               'raw_affiliations': [ { 'value': 'Lawrence '
                                                                'Berkeley '
                                                                'National '
                                                                'Laboratory, '
                                                                'Berkeley, CA, '
                                                                'USA'}],
                               'record': { '$ref': 'https://inspirehep.net/api/authors/1632634'},
                               'signature_block': 'MARNANd',
                               'uuid': '4c62c35d-821f-4abd-af4f-371861538b42'},
                             { 'affiliations': [ { 'record': { '$ref': 'https://inspirehep.net/api/institutions/902953'},
                                                   'value': 'LBL, Berkeley'}],
                               'affiliations_identifiers': [ { 'schema': 'GRID',
                                                               'value': 'grid.184769.5'}],
                               'full_name': 'Calafiura, Paolo',
                               'ids': [ { 'schema': 'INSPIRE BAI',
                                          'value': 'P.Calafiura.1'}],
                               'raw_affiliations': [ { 'value': 'Lawrence '
                                                                'Berkeley '
                                                                'National '
                                                                'Laboratory, '
                                                                'Berkeley, CA, '
                                                                'USA'}],
                               'record': { '$ref': 'https://inspirehep.net/api/authors/1014750'},
                               'signature_block': 'CALAFARp',
                               'uuid': 'd0d5b843-e7f1-4204-a0f5-46e5fe2cc329'},
                             { 'affiliations': [ { 'record': { '$ref': 'https://inspirehep.net/api/institutions/902953'},
                                                   'value': 'LBL, Berkeley'}],
                               'affiliations_identifiers': [ { 'schema': 'GRID',
                                                               'value': 'grid.184769.5'}],
                               'full_name': 'Choma, Nicholas',
                               'ids': [ { 'schema': 'INSPIRE BAI',
                                          'value': 'N.Choma.1'}],
                               'raw_affiliations': [ { 'value': 'Lawrence '
                                                                'Berkeley '
                                                                'National '
                                                                'Laboratory, '
                                                                'Berkeley, CA, '
                                                                'USA'}],
                               'record': { '$ref': 'https://inspirehep.net/api/authors/1926110'},
                               'signature_block': 'CANn',
                               'uuid': '4170e220-23bf-420d-a494-61cf6189b26c'},
                             { 'affiliations': [ { 'record': { '$ref': 'https://inspirehep.net/api/institutions/902953'},
                                                   'value': 'LBL, Berkeley'}],
                               'affiliations_identifiers': [ { 'schema': 'GRID',
                                                               'value': 'grid.184769.5'}],
                               'full_name': 'Conlon, Sean',
                               'ids': [ { 'schema': 'INSPIRE BAI',
                                          'value': 'S.Conlon.1'}],
                               'raw_affiliations': [ { 'value': 'Lawrence '
                                                                'Berkeley '
                                                                'National '
                                                                'Laboratory, '
                                                                'Berkeley, CA, '
                                                                'USA'}],
                               'record': { '$ref': 'https://inspirehep.net/api/authors/1926111'},
                               'signature_block': 'CANLANs',
                               'uuid': 'd398b335-af8c-4d31-ad86-7410ea0b9604'},
                             { 'affiliations': [ { 'record': { '$ref': 'https://inspirehep.net/api/institutions/902953'},
                                                   'value': 'LBL, Berkeley'}],
                               'affiliations_identifiers': [ { 'schema': 'GRID',
                                                               'value': 'grid.184769.5'}],
                               'full_name': 'Farrell, Steven',
                               'ids': [ { 'schema': 'INSPIRE BAI',
                                          'value': 'S.Farrell.2'}],
                               'raw_affiliations': [ { 'value': 'Lawrence '
                                                                'Berkeley '
                                                                'National '
                                                                'Laboratory, '
                                                                'Berkeley, CA, '
                                                                'USA'}],
                               'record': { '$ref': 'https://inspirehep.net/api/authors/1054600'},
                               'signature_block': 'FARALs',
                               'uuid': '523cc78e-9ffa-431e-aa65-1152f77f5ebf'},
                             { 'affiliations': [ { 'record': { '$ref': 'https://inspirehep.net/api/institutions/902953'},
                                                   'value': 'LBL, Berkeley'}],
                               'affiliations_identifiers': [ { 'schema': 'GRID',
                                                               'value': 'grid.184769.5'}],
                               'full_name': 'Xu, Yaoyuan',
                               'ids': [ { 'schema': 'INSPIRE BAI',
                                          'value': 'Y.Xu.47'}],
                               'raw_affiliations': [ { 'value': 'Lawrence '
                                                                'Berkeley '
                                                                'National '
                                                                'Laboratory, '
                                                                'Berkeley, CA, '
                                                                'USA'}],
                               'record': { '$ref': 'https://inspirehep.net/api/authors/1926112'},
                               'signature_block': 'Xy',
                               'uuid': '54dbdc01-7177-4ade-99a6-70985d472361'},
                             { 'affiliations': [ { 'record': { '$ref': 'https://inspirehep.net/api/institutions/902711'},
                                                   'value': 'Caltech'}],
                               'affiliations_identifiers': [ { 'schema': 'GRID',
                                                               'value': 'grid.20861.3d'}],
                               'full_name': 'Spiropulu, Maria',
                               'ids': [ { 'schema': 'INSPIRE BAI',
                                          'value': 'M.Spiropulu.1'}],
                               'raw_affiliations': [ { 'value': 'California '
                                                                'Institute of '
                                                                'Technology, '
                                                                'Pasadena, CA, '
                                                                'USA'}],
                               'record': { '$ref': 'https://inspirehep.net/api/authors/987865'},
                               'signature_block': 'SPARAPALm',
                               'uuid': '84a2dd46-dfb2-429d-b7c2-94313186e560'},
                             { 'affiliations': [ { 'record': { '$ref': 'https://inspirehep.net/api/institutions/902711'},
                                                   'value': 'Caltech'}],
                               'affiliations_identifiers': [ { 'schema': 'GRID',
                                                               'value': 'grid.20861.3d'}],
                               'full_name': 'Vlimant, Jean-Roch',
                               'ids': [ { 'schema': 'INSPIRE BAI',
                                          'value': 'J.R.Vlimant.1'}],
                               'raw_affiliations': [ { 'value': 'California '
                                                                'Institute of '
                                                                'Technology, '
                                                                'Pasadena, CA, '
                                                                'USA'}],
                               'record': { '$ref': 'https://inspirehep.net/api/authors/1023557'},
                               'signature_block': 'VLANADj',
                               'uuid': '8534ab30-a82f-413e-b4e2-7be5378d2392'},
                             { 'affiliations': [ { 'record': { '$ref': 'https://inspirehep.net/api/institutions/902734'},
                                                   'value': 'Cincinnati U.'}],
                               'affiliations_identifiers': [ { 'schema': 'GRID',
                                                               'value': 'grid.24827.3b'}],
                               'full_name': 'Aurisano, Adam',
                               'ids': [ { 'schema': 'INSPIRE BAI',
                                          'value': 'A.Aurisano.1'}],
                               'raw_affiliations': [ { 'value': 'University of '
                                                                'Cincinnati, '
                                                                'Cincinnati, '
                                                                'OH, USA'}],
                               'record': { '$ref': 'https://inspirehep.net/api/authors/1021053'},
                               'signature_block': 'ARASANa',
                               'uuid': '20270d96-7e95-4d60-b7c4-01223280eff6'},
                             { 'affiliations': [ { 'record': { '$ref': 'https://inspirehep.net/api/institutions/902734'},
                                                   'value': 'Cincinnati U.'}],
                               'affiliations_identifiers': [ { 'schema': 'GRID',
                                                               'value': 'grid.24827.3b'}],
                               'full_name': 'Hewes, Jeremy',
                               'ids': [ { 'schema': 'INSPIRE BAI',
                                          'value': 'J.Hewes.1'}],
                               'raw_affiliations': [ { 'value': 'University of '
                                                                'Cincinnati, '
                                                                'Cincinnati, '
                                                                'OH, USA'}],
                               'record': { '$ref': 'https://inspirehep.net/api/authors/1408419'},
                               'signature_block': 'Hj',
                               'uuid': 'd1204d7d-5e5d-4797-9832-ba24489623bf'},
                             { 'affiliations': [ { 'record': { '$ref': 'https://inspirehep.net/api/institutions/902796'},
                                                   'value': 'Fermilab'}],
                               'affiliations_identifiers': [ { 'schema': 'GRID',
                                                               'value': 'grid.417851.e'}],
                               'full_name': 'Cerati, Giuseppe',
                               'ids': [ { 'schema': 'INSPIRE BAI',
                                          'value': 'G.B.Cerati.1'}],
                               'raw_affiliations': [ { 'value': 'Fermi '
                                                                'National '
                                                                'Accelerator '
                                                                'Laboratory, '
                                                                'Batavia, IL, '
                                                                'USA'}],
                               'record': { '$ref': 'https://inspirehep.net/api/authors/1064383'},
                               'signature_block': 'CARATg',
                               'uuid': '8ffbd014-8c15-4b38-b011-4a59801083e6'},
                             { 'affiliations': [ { 'record': { '$ref': 'https://inspirehep.net/api/institutions/902796'},
                                                   'value': 'Fermilab'}],
                               'affiliations_identifiers': [ { 'schema': 'GRID',
                                                               'value': 'grid.417851.e'}],
                               'full_name': 'Gray, Lindsey',
                               'ids': [ { 'schema': 'INSPIRE BAI',
                                          'value': 'Lindsey.A.Gray.1'}],
                               'raw_affiliations': [ { 'value': 'Fermi '
                                                                'National '
                                                                'Accelerator '
                                                                'Laboratory, '
                                                                'Batavia, IL, '
                                                                'USA'}],
                               'record': { '$ref': 'https://inspirehep.net/api/authors/1059457'},
                               'signature_block': 'GRYl',
                               'uuid': '52a7a010-5c05-42c3-858b-075c2592f536'},
                             { 'affiliations': [ { 'record': { '$ref': 'https://inspirehep.net/api/institutions/902796'},
                                                   'value': 'Fermilab'}],
                               'affiliations_identifiers': [ { 'schema': 'GRID',
                                                               'value': 'grid.417851.e'}],
                               'full_name': 'Klijnsma, Thomas',
                               'ids': [ { 'schema': 'INSPIRE BAI',
                                          'value': 'T.Klijnsma.2'}],
                               'raw_affiliations': [ { 'value': 'Fermi '
                                                                'National '
                                                                'Accelerator '
                                                                'Laboratory, '
                                                                'Batavia, IL, '
                                                                'USA'}],
                               'record': { '$ref': 'https://inspirehep.net/api/authors/1396923'},
                               'signature_block': 'CLAJNSNt',
                               'uuid': 'd11050b4-8fd9-4a83-8a5b-d51dfc0c6d63'},
                             { 'affiliations': [ { 'record': { '$ref': 'https://inspirehep.net/api/institutions/902796'},
                                                   'value': 'Fermilab'}],
                               'affiliations_identifiers': [ { 'schema': 'GRID',
                                                               'value': 'grid.417851.e'}],
                               'full_name': 'Kowalkowski, Jim',
                               'ids': [ { 'schema': 'INSPIRE BAI',
                                          'value': 'J.Kowalkowski.1'}],
                               'raw_affiliations': [ { 'value': 'Fermi '
                                                                'National '
                                                                'Accelerator '
                                                                'Laboratory, '
                                                                'Batavia, IL, '
                                                                'USA'}],
                               'record': { '$ref': 'https://inspirehep.net/api/authors/1070006'},
                               'signature_block': 'CALCASCj',
                               'uuid': '322012cd-2e8f-484e-8f4b-638e27b703b3'},
                             { 'affiliations': [ { 'record': { '$ref': 'https://inspirehep.net/api/institutions/1112663'},
                                                   'value': 'Illinois U., '
                                                            'Urbana (main)'}],
                               'affiliations_identifiers': [ { 'schema': 'GRID',
                                                               'value': 'grid.35403.31'}],
                               'full_name': 'Atkinson, Markus',
                               'ids': [ { 'schema': 'INSPIRE BAI',
                                          'value': 'M.Atkinson.1'}],
                               'raw_affiliations': [ { 'value': 'University of '
                                                                'Illinois at '
                                                                'Urbana-Champaign, '
                                                                'Urbana, IL, '
                                                                'USA'}],
                               'record': { '$ref': 'https://inspirehep.net/api/authors/1074385'},
                               'signature_block': 'ATCANSANm',
                               'uuid': '64505d97-d4b5-41fa-aeec-05073a3efa80'},
                             { 'affiliations': [ { 'record': { '$ref': 'https://inspirehep.net/api/institutions/1112663'},
                                                   'value': 'Illinois U., '
                                                            'Urbana (main)'}],
                               'affiliations_identifiers': [ { 'schema': 'GRID',
                                                               'value': 'grid.35403.31'}],
                               'full_name': 'Neubauer, Mark',
                               'ids': [ { 'schema': 'INSPIRE BAI',
                                          'value': 'M.S.Neubauer.1'}],
                               'raw_affiliations': [ { 'value': 'University of '
                                                                'Illinois at '
                                                                'Urbana-Champaign, '
                                                                'Urbana, IL, '
                                                                'USA'}],
                               'record': { '$ref': 'https://inspirehep.net/api/authors/995835'},
                               'signature_block': 'NABARm',
                               'uuid': '8e6c2a69-2948-446d-86d2-8c2753fa5f9b'},
                             { 'affiliations': [ { 'record': { '$ref': 'https://inspirehep.net/api/institutions/903139'},
                                                   'value': 'Princeton U.'}],
                               'affiliations_identifiers': [ { 'schema': 'GRID',
                                                               'value': 'grid.16750.35'}],
                               'full_name': 'DeZoort, Gage',
                               'ids': [ { 'schema': 'INSPIRE BAI',
                                          'value': 'G.Dezoort.1'}],
                               'raw_affiliations': [ { 'value': 'Princeton '
                                                                'University, '
                                                                'Princeton, '
                                                                'NJ, USA'}],
                               'record': { '$ref': 'https://inspirehep.net/api/authors/1694015'},
                               'signature_block': 'DASADg',
                               'uuid': '3fa0e791-a30c-4f31-a9f2-afaa20eb4676'},
                             { 'affiliations': [ { 'record': { '$ref': 'https://inspirehep.net/api/institutions/903139'},
                                                   'value': 'Princeton U.'}],
                               'affiliations_identifiers': [ { 'schema': 'GRID',
                                                               'value': 'grid.16750.35'}],
                               'full_name': 'Thais, Savannah',
                               'ids': [ { 'schema': 'INSPIRE BAI',
                                          'value': 'S.Thais.1'}],
                               'raw_affiliations': [ { 'value': 'Princeton '
                                                                'University, '
                                                                'Princeton, '
                                                                'NJ, USA'}],
                               'record': { '$ref': 'https://inspirehep.net/api/authors/1191655'},
                               'signature_block': 'Ts',
                               'uuid': '91735e29-abcf-4815-915d-138473fd4de8'},
                             { 'affiliations': [ { 'record': { '$ref': 'https://inspirehep.net/api/institutions/903338'},
                                                   'value': 'Washington U., '
                                                            'Seattle'}],
                               'affiliations_identifiers': [ { 'schema': 'GRID',
                                                               'value': 'grid.34477.33'}],
                               'full_name': 'Chauhan, Aditi',
                               'ids': [ { 'schema': 'INSPIRE BAI',
                                          'value': 'A.Chauhan.2'}],
                               'raw_affiliations': [ { 'value': 'University of '
                                                                'Washington, '
                                                                'Seattle, WA, '
                                                                'USA'}],
                               'record': { '$ref': 'https://inspirehep.net/api/authors/1926113'},
                               'signature_block': 'CANa',
                               'uuid': 'e8003187-3abc-44dd-94a8-78d6c522cec7'},
                             { 'affiliations': [ { 'record': { '$ref': 'https://inspirehep.net/api/institutions/903338'},
                                                   'value': 'Washington U., '
                                                            'Seattle'}],
                               'affiliations_identifiers': [ { 'schema': 'GRID',
                                                               'value': 'grid.34477.33'}],
                               'full_name': 'Schuy, Alex',
                               'ids': [ { 'schema': 'INSPIRE BAI',
                                          'value': 'A.Schuy.1'}],
                               'raw_affiliations': [ { 'value': 'University of '
                                                                'Washington, '
                                                                'Seattle, WA, '
                                                                'USA'}],
                               'record': { '$ref': 'https://inspirehep.net/api/authors/1926114'},
                               'signature_block': 'SYa',
                               'uuid': 'b1a497f3-d40e-4ab8-a599-e68a1fe0cce0'},
                             { 'affiliations': [ { 'record': { '$ref': 'https://inspirehep.net/api/institutions/903338'},
                                                   'value': 'Washington U., '
                                                            'Seattle'}],
                               'affiliations_identifiers': [ { 'schema': 'GRID',
                                                               'value': 'grid.34477.33'}],
                               'full_name': 'Hsu, Shih-Chieh',
                               'ids': [ { 'schema': 'INSPIRE BAI',
                                          'value': 'S.C.Hsu.1'}],
                               'raw_affiliations': [ { 'value': 'University of '
                                                                'Washington, '
                                                                'Seattle, WA, '
                                                                'USA'}],
                               'record': { '$ref': 'https://inspirehep.net/api/authors/1028683'},
                               'signature_block': 'HSs',
                               'uuid': '191d2848-9487-4641-8145-e42dd6133374'},
                             { 'affiliations': [ { 'record': { '$ref': 'https://inspirehep.net/api/institutions/911228'},
                                                   'value': 'Youngstown State '
                                                            'U.'}],
                               'affiliations_identifiers': [ { 'schema': 'GRID',
                                                               'value': 'grid.268467.9'}],
                               'full_name': 'Ballow, Alex',
                               'ids': [ { 'schema': 'INSPIRE BAI',
                                          'value': 'A.Ballow.1'}],
                               'raw_affiliations': [ { 'value': 'Youngstown '
                                                                'State '
                                                                'University, '
                                                                'Youngstown, '
                                                                'OH, USA'}],
                               'record': { '$ref': 'https://inspirehep.net/api/authors/1926115'},
                               'signature_block': 'BALa',
                               'uuid': 'be4a7ac9-5bd4-44f3-bcc4-a516d9197045'},
                             { 'affiliations': [ { 'record': { '$ref': 'https://inspirehep.net/api/institutions/911228'},
                                                   'value': 'Youngstown State '
                                                            'U.'}],
                               'affiliations_identifiers': [ { 'schema': 'GRID',
                                                               'value': 'grid.268467.9'}],
                               'full_name': 'Lazar, Alina',
                               'ids': [ { 'schema': 'INSPIRE BAI',
                                          'value': 'A.Lazar.2'}],
                               'raw_affiliations': [ { 'value': 'Youngstown '
                                                                'State '
                                                                'University, '
                                                                'Youngstown, '
                                                                'OH, USA'}],
                               'record': { '$ref': 'https://inspirehep.net/api/authors/1926117'},
                               'signature_block': 'LASARa',
                               'uuid': '28c217ec-599a-490a-ad7d-3fc1034b74d5'}],
                'citation_count': 11,
                'citation_count_without_self_citations': 6,
                'citeable': True,
                'control_number': 1851403,
                'core': True,
                'curated': True,
                'document_type': ['article'],
                'documents': [ { 'description': 'Fulltext from Publisher',
                                 'filename': 'document',
                                 'fulltext': True,
                                 'key': '067e108e8df55fe501517f211ff94e34',
                                 'url': 'https://inspirehep.net/files/067e108e8df55fe501517f211ff94e34'},
                               { 'description': 'Fulltext',
                                 'filename': 'fermilab-pub-21-100-scd.pdf',
                                 'fulltext': True,
                                 'key': '8b30717a7271797e5f674982ecd24927',
                                 'original_url': 'https://lss.fnal.gov/archive/2021/pub/fermilab-pub-21-100-scd.pdf',
                                 'url': 'https://inspirehep.net/files/8b30717a7271797e5f674982ecd24927'}],
                'dois': [ { 'source': 'Springer',
                            'value': '10.1140/epjc/s10052-021-09675-8'},
                          { 'material': 'publication',
                            'source': 'arXiv',
                            'value': '10.1140/epjc/s10052-021-09675-8'}],
                'external_system_identifiers': [ { 'schema': 'OSTI',
                                                   'value': '1824310'}],
                'figures': [ { 'caption': 'A simulated HL-LHC collision event '
                                          '(top) as seen by the TrackML '
                                          'tracking '
                                          'detector~\\cite{TrackMLAccuracy2019}. '
                                          'The detector schematic (bottom) '
                                          'shows the top half of the detector '
                                          'projected on the r-z plane. The '
                                          'z-axis is along the beam direction.',
                               'filename': 'trackml_display.png',
                               'key': '76290ab2370986fdda0a86ca0170038b',
                               'label': 'fig:trackml_detector',
                               'material': 'preprint',
                               'source': 'arxiv',
                               'url': 'https://inspirehep.net/files/76290ab2370986fdda0a86ca0170038b'},
                             { 'caption': 'A simulated HL-LHC collision event '
                                          '(top) as seen by the TrackML '
                                          'tracking '
                                          'detector~\\cite{TrackMLAccuracy2019}. '
                                          'The detector schematic (bottom) '
                                          'shows the top half of the detector '
                                          'projected on the r-z plane. The '
                                          'z-axis is along the beam direction.',
                               'filename': 'trackml_detector.png',
                               'key': '65f63bfdce2db2af207dc3bbb7b92408',
                               'label': 'fig:trackml_detector',
                               'material': 'preprint',
                               'source': 'arxiv',
                               'url': 'https://inspirehep.net/files/65f63bfdce2db2af207dc3bbb7b92408'},
                             { 'caption': 'Reconstruction wall time per event '
                                          'as a function of the average number '
                                          'of interactions per bunch crossing '
                                          '\\mmu. Top: ATLAS Run~2 Inner '
                                          'Detector reconstruction with '
                                          'default '
                                          'configurations~\\cite{ATLASCompRes}. '
                                          'Bottom: CMS time spent in tracking '
                                          'sequence for 2016 tracking, 2017 '
                                          'tracking with conventional seeding, '
                                          'and 2017 tracking with Cellular '
                                          'Automaton (CA) '
                                          'seeding~\\cite{CMSCompRes}.',
                               'filename': 'ATLAS_reco_WtPerEvent_NOfit_revised.png',
                               'key': '867f6aacb56a046055c299f4969cb826',
                               'label': 'fig:atlas_reco_time',
                               'material': 'preprint',
                               'source': 'arxiv',
                               'url': 'https://inspirehep.net/files/867f6aacb56a046055c299f4969cb826'},
                             { 'caption': 'Reconstruction wall time per event '
                                          'as a function of the average number '
                                          'of interactions per bunch crossing '
                                          '\\mmu. Top: ATLAS Run~2 Inner '
                                          'Detector reconstruction with '
                                          'default '
                                          'configurations~\\cite{ATLASCompRes}. '
                                          'Bottom: CMS time spent in tracking '
                                          'sequence for 2016 tracking, 2017 '
                                          'tracking with conventional seeding, '
                                          'and 2017 tracking with Cellular '
                                          'Automaton (CA) '
                                          'seeding~\\cite{CMSCompRes}.',
                               'filename': 'CMS_ttbar_phase0_phase1ca_vs_pu_time_vs_pu.png',
                               'key': '3ca1c5036d1bd02b80a7ecd00bfd21f9',
                               'label': 'fig:atlas_reco_time',
                               'material': 'preprint',
                               'source': 'arxiv',
                               'url': 'https://inspirehep.net/files/3ca1c5036d1bd02b80a7ecd00bfd21f9'},
                             { 'caption': 'A typical event distribution of '
                                          'spacepoints projected on the '
                                          '$x$-$z$ plane, parallel to the beam '
                                          'direction (left), and the $x$-$y$ '
                                          'plane, orthogonal to the beam '
                                          'direction (right).',
                               'filename': 'detector_scatter.png',
                               'key': '230f2fef4846e1d63682e3874ab68375',
                               'label': 'fig:distributions',
                               'material': 'preprint',
                               'source': 'arxiv',
                               'url': 'https://inspirehep.net/files/230f2fef4846e1d63682e3874ab68375'},
                             { 'caption': 'Stages of the TrackML track '
                                          'formation inference pipeline. Light '
                                          'red boxes are trainable stages.',
                               'filename': 'pipeline.png',
                               'key': '724bcf0598d1fcfd75fec54e476cf985',
                               'label': 'fig:pipeline',
                               'material': 'preprint',
                               'source': 'arxiv',
                               'url': 'https://inspirehep.net/files/724bcf0598d1fcfd75fec54e476cf985'},
                             { 'caption': 'Top row: selected, reconstructable, '
                                          'and matched particles (left) and '
                                          'tracking efficiency (right) as a '
                                          'function of \\pt\\ for particles '
                                          'with $|\\eta| < 4$. Bottom row: '
                                          'selected, reconstructable, and '
                                          'matched particles (left) and '
                                          'tracking efficiency (right) as a '
                                          'function of $\\eta$ for $\\pt > '
                                          '0.5$~GeV. The definition of '
                                          "``selected'', ``reconstructable'', "
                                          "and ``matched'' can be found in "
                                          '\\S~\\ref{sec:effpur}',
                               'filename': 'out_pt-cut0.0_4.png',
                               'key': '4c32339ba9d22a229768200887b2010f',
                               'label': 'fig:res_pt_eta',
                               'material': 'preprint',
                               'source': 'arxiv',
                               'url': 'https://inspirehep.net/files/4c32339ba9d22a229768200887b2010f'},
                             { 'caption': 'Top row: selected, reconstructable, '
                                          'and matched particles (left) and '
                                          'tracking efficiency (right) as a '
                                          'function of \\pt\\ for particles '
                                          'with $|\\eta| < 4$. Bottom row: '
                                          'selected, reconstructable, and '
                                          'matched particles (left) and '
                                          'tracking efficiency (right) as a '
                                          'function of $\\eta$ for $\\pt > '
                                          '0.5$~GeV. The definition of '
                                          "``selected'', ``reconstructable'', "
                                          "and ``matched'' can be found in "
                                          '\\S~\\ref{sec:effpur}',
                               'filename': 'out_pt-cut0.0_4_ratio.png',
                               'key': 'e367bade9dcf585539364d4a2316a51a',
                               'label': 'fig:res_pt_eta',
                               'material': 'preprint',
                               'source': 'arxiv',
                               'url': 'https://inspirehep.net/files/e367bade9dcf585539364d4a2316a51a'},
                             { 'caption': 'Top row: selected, reconstructable, '
                                          'and matched particles (left) and '
                                          'tracking efficiency (right) as a '
                                          'function of \\pt\\ for particles '
                                          'with $|\\eta| < 4$. Bottom row: '
                                          'selected, reconstructable, and '
                                          'matched particles (left) and '
                                          'tracking efficiency (right) as a '
                                          'function of $\\eta$ for $\\pt > '
                                          '0.5$~GeV. The definition of '
                                          "``selected'', ``reconstructable'', "
                                          "and ``matched'' can be found in "
                                          '\\S~\\ref{sec:effpur}',
                               'filename': 'out_eta-cut0.5_4.png',
                               'key': '11e9d0dd31b66738e490713abf02fc9c',
                               'label': 'fig:res_pt_eta',
                               'material': 'preprint',
                               'source': 'arxiv',
                               'url': 'https://inspirehep.net/files/11e9d0dd31b66738e490713abf02fc9c'},
                             { 'caption': 'Top row: selected, reconstructable, '
                                          'and matched particles (left) and '
                                          'tracking efficiency (right) as a '
                                          'function of \\pt\\ for particles '
                                          'with $|\\eta| < 4$. Bottom row: '
                                          'selected, reconstructable, and '
                                          'matched particles (left) and '
                                          'tracking efficiency (right) as a '
                                          'function of $\\eta$ for $\\pt > '
                                          '0.5$~GeV. The definition of '
                                          "``selected'', ``reconstructable'', "
                                          "and ``matched'' can be found in "
                                          '\\S~\\ref{sec:effpur}',
                               'filename': 'out_eta-cut0.5_4_ratio.png',
                               'key': 'd3a7f0b3e97de64456bdb393a5fb8710',
                               'label': 'fig:res_pt_eta',
                               'material': 'preprint',
                               'source': 'arxiv',
                               'url': 'https://inspirehep.net/files/d3a7f0b3e97de64456bdb393a5fb8710'},
                             { 'caption': 'Mean and standard deviation of the '
                                          'technical efficiency (top) and '
                                          'purity (bottom) as a function of '
                                          'the total number of spacepoints in '
                                          'an event.',
                               'filename': 'mean_track_eff.png',
                               'key': '384cc07d85027814092295a4970b0fb4',
                               'label': 'fig:res_vs_hits',
                               'material': 'preprint',
                               'source': 'arxiv',
                               'url': 'https://inspirehep.net/files/384cc07d85027814092295a4970b0fb4'},
                             { 'caption': 'Mean and standard deviation of the '
                                          'technical efficiency (top) and '
                                          'purity (bottom) as a function of '
                                          'the total number of spacepoints in '
                                          'an event.',
                               'filename': 'mean_track_pur.png',
                               'key': '81a2839796393f2ef484689fcbcd259b',
                               'label': 'fig:res_vs_hits',
                               'material': 'preprint',
                               'source': 'arxiv',
                               'url': 'https://inspirehep.net/files/81a2839796393f2ef484689fcbcd259b'},
                             { 'caption': '\\textit{Relative} technical '
                                          'efficiency as a function of \\pt. '
                                          'Each curve shows the ratio of '
                                          '$\\textnormal{eff}(\\textnormal{noise}=N\\%) '
                                          '/ '
                                          '\\textnormal{eff}(\\textnormal{noise}=0)$.',
                               'filename': 'trkeff_pt_noises.png',
                               'key': 'edf118f7d18da51a3eff2a6f25041416',
                               'label': 'fig:noise',
                               'material': 'preprint',
                               'source': 'arxiv',
                               'url': 'https://inspirehep.net/files/edf118f7d18da51a3eff2a6f25041416'},
                             { 'caption': 'Time per training epoch (left) and '
                                          'Strong scaling efficiency (right) '
                                          "for GNN's distributed training. The "
                                          'top row refers to the Horovod '
                                          'implementation, the bottom row to '
                                          'the \\textsc{tf.distributed} one. '
                                          'The first bin in the bottom left '
                                          'diagram refers to the serial case, '
                                          'in which the input graph is not '
                                          'padded.',
                               'filename': 'timing_data_distributed_training_reducedGraph_hvd.png',
                               'key': 'ff5c3db2bd7e34edc92ca2fea079e57a',
                               'label': 'fig:strong_scaling_hvd',
                               'material': 'preprint',
                               'source': 'arxiv',
                               'url': 'https://inspirehep.net/files/ff5c3db2bd7e34edc92ca2fea079e57a'},
                             { 'caption': 'Time per training epoch (left) and '
                                          'Strong scaling efficiency (right) '
                                          "for GNN's distributed training. The "
                                          'top row refers to the Horovod '
                                          'implementation, the bottom row to '
                                          'the \\textsc{tf.distributed} one. '
                                          'The first bin in the bottom left '
                                          'diagram refers to the serial case, '
                                          'in which the input graph is not '
                                          'padded.',
                               'filename': 'scalability_reducedGraph_hvd.png',
                               'key': '5fff882d4783dd333d9b598cc93e0d6d',
                               'label': 'fig:strong_scaling_hvd',
                               'material': 'preprint',
                               'source': 'arxiv',
                               'url': 'https://inspirehep.net/files/5fff882d4783dd333d9b598cc93e0d6d'},
                             { 'caption': 'Time per training epoch (left) and '
                                          'Strong scaling efficiency (right) '
                                          "for GNN's distributed training. The "
                                          'top row refers to the Horovod '
                                          'implementation, the bottom row to '
                                          'the \\textsc{tf.distributed} one. '
                                          'The first bin in the bottom left '
                                          'diagram refers to the serial case, '
                                          'in which the input graph is not '
                                          'padded.',
                               'filename': 'timing_data_distributed_training_reducedGraph.png',
                               'key': 'fbac1c1794d86a7186f7af58e9b909bc',
                               'label': 'fig:strong_scaling_hvd',
                               'material': 'preprint',
                               'source': 'arxiv',
                               'url': 'https://inspirehep.net/files/fbac1c1794d86a7186f7af58e9b909bc'},
                             { 'caption': 'Time per training epoch (left) and '
                                          'Strong scaling efficiency (right) '
                                          "for GNN's distributed training. The "
                                          'top row refers to the Horovod '
                                          'implementation, the bottom row to '
                                          'the \\textsc{tf.distributed} one. '
                                          'The first bin in the bottom left '
                                          'diagram refers to the serial case, '
                                          'in which the input graph is not '
                                          'padded.',
                               'filename': 'scalability_reducedGraph.png',
                               'key': 'd4bc1981283388e87862c033eceac00c',
                               'label': 'fig:strong_scaling_hvd',
                               'material': 'preprint',
                               'source': 'arxiv',
                               'url': 'https://inspirehep.net/files/d4bc1981283388e87862c033eceac00c'},
                             { 'caption': 'Total inference time as a function '
                                          'of number of spacepoints in each '
                                          'event for CPUs (top) and GPUs '
                                          '(bottom).',
                               'filename': 'cpu_13nhits.png',
                               'key': 'eb618772299437053272114e2735ea59',
                               'label': 'fig:inf_timing_vs_nhits',
                               'material': 'preprint',
                               'source': 'arxiv',
                               'url': 'https://inspirehep.net/files/eb618772299437053272114e2735ea59'},
                             { 'caption': 'Total inference time as a function '
                                          'of number of spacepoints in each '
                                          'event for CPUs (top) and GPUs '
                                          '(bottom).',
                               'filename': 'gpu_8khits.png',
                               'key': '6a2cca5272f46ad9a1ca9df58e446307',
                               'label': 'fig:inf_timing_vs_nhits',
                               'material': 'preprint',
                               'source': 'arxiv',
                               'url': 'https://inspirehep.net/files/6a2cca5272f46ad9a1ca9df58e446307'},
                             { 'caption': 'The effect of using augmented '
                                          'training data during training on '
                                          'the verification loss and training '
                                          'loss. Reflecting across the '
                                          'phi-axis shows an overall '
                                          'improvement in performance as this '
                                          'produces the charge conjugate '
                                          'partner of the input graph.',
                               'filename': 'phi_reflections.png',
                               'key': 'bf0d65f00ad9a2e3038de502461e772d',
                               'label': 'fig:phi-reflect',
                               'material': 'preprint',
                               'source': 'arxiv',
                               'url': 'https://inspirehep.net/files/bf0d65f00ad9a2e3038de502461e772d'}],
                'imprints': [{'date': '2021-10-06'}],
                'inspire_categories': [ { 'source': 'arxiv',
                                          'term': 'Experiment-HEP'},
                                        { 'source': 'arxiv',
                                          'term': 'Computing'},
                                        {'term': 'Experiment-HEP'},
                                        {'term': 'Computing'}],
                'keywords': [ {'schema': 'INSPIRE', 'value': 'performance'},
                              {'schema': 'INSPIRE', 'value': 'CMS'},
                              { 'schema': 'INSPIRE',
                                'value': 'tracking detector'},
                              {'schema': 'INSPIRE', 'value': 'neural network'},
                              {'schema': 'INSPIRE', 'value': 'acceleration'},
                              {'schema': 'INSPIRE', 'value': 'calorimeter'},
                              { 'schema': 'INSPIRE',
                                'value': 'particle identification: efficiency'},
                              {'schema': 'INSPIRE', 'value': 'cluster'},
                              {'schema': 'INSPIRE', 'value': 'tracks'},
                              {'schema': 'INSPIRE', 'value': 'ATLAS'},
                              {'schema': 'INSPIRE', 'value': 'DUNE'},
                              { 'schema': 'INSPIRE',
                                'value': 'track data analysis'},
                              { 'schema': 'INSPIRE',
                                'value': 'data analysis method'},
                              { 'schema': 'INSPIRE',
                                'value': 'numerical calculations: Monte '
                                         'Carlo'}],
                'legacy_creation_date': '2021-03-15',
                'legacy_version': '20210503180030.0',
                'license': [ { 'imposing': 'Springer',
                               'license': 'CC-BY-4.0',
                               'url': 'http://creativecommons.org/licenses/by/4.0/'},
                             { 'license': 'CC BY-SA 4.0',
                               'material': 'preprint',
                               'url': 'http://creativecommons.org/licenses/by-sa/4.0/'}],
                'preprint_date': '2021-03-11',
                'publication_info': [ { 'artid': '876',
                                        'journal_issue': '10',
                                        'journal_record': { '$ref': 'https://inspirehep.net/api/journals/1613946'},
                                        'journal_title': 'Eur.Phys.J.C',
                                        'journal_volume': '81',
                                        'page_start': '876',
                                        'year': 2021}],
                'refereed': True,
                'references': [ ],
                'report_numbers': [{'value': 'FERMILAB-PUB-21-100-SCD'}],
                'texkeys': ['Ju:2021ayy'],
                'titles': [ { 'source': 'Springer',
                              'title': 'Performance of a geometric deep '
                                       'learning pipeline for HL-LHC particle '
                                       'tracking'},
                            { 'source': 'arXiv',
                              'title': 'Performance of a Geometric Deep '
                                       'Learning Pipeline for HL-LHC Particle '
                                       'Tracking'},
                            { 'source': 'arXiv',
                              'title': 'Physics and Computing Performance of '
                                       'the Exa.TrkX TrackML Pipeline'}],
                'urls': [ { 'description': 'Fermilab Library Server',
                            'value': 'https://lss.fnal.gov/archive/2021/pub/fermilab-pub-21-100-scd.pdf'}]},
  'revision_id': 57,
  'updated': '2021-10-29T21:53:19.551422+00:00',
  'uuid': '20bc9a0a-abc0-40ad-83a1-31536fc0ab74'}



{ 'arxiv_category': 'physics.data-an',
  'arxiv_eprints': '2103.06995',
  'bibtex': '@article{Ju:2021ayy,\n'
            ' archiveprefix = {arXiv},\n'
            ' author = {Ju, Xiangyang and others},\n'
            ' doi = {10.1140/epjc/s10052-021-09675-8},\n'
            ' eprint = {2103.06995},\n'
            ' journal = {Eur. Phys. J. C},\n'
            ' number = {10},\n'
            ' pages = {876},\n'
            ' primaryclass = {physics.data-an},\n'
            ' reportnumber = {FERMILAB-PUB-21-100-SCD},\n'
            ' title = {{Performance of a geometric deep learning pipeline for '
            'HL-LHC particle tracking}},\n'
            ' volume = {81},\n'
            ' year = {2021}\n'
            '}\n'
            '\n',
  'citation_count': 11,
  'citation_count_without_self_citations': 6,
  'doi': '10.1140/epjc/s10052-021-09675-8',
  'preprint_date': '2021-03-11',
  'texkeys': 'Ju:2021ayy',
  'title': 'Performance of a geometric deep learning pipeline for HL-LHC '
           'particle tracking'}

```

