import pandas as pd
from connect_to_json import json_data as j

pupils = pd.DataFrame(j['pupils'])
subjects = pd.DataFrame(j['subjects'])
certificate_type = pd.DataFrame(j['certificate_type'])
certificates = pd.DataFrame(j['certificates'])

pupils_with_certificate = pd.merge(pupils, certificates, left_on='id', right_on='pupil_id', how='outer')[['id', 'name', 'type', 'subject_id', 'score']]
pupils_with_certificate_types = pd.merge(pupils_with_certificate, certificate_type, how='left', left_on='type', right_on='id')[['id_x', 'name', 'subject_id', 'score']]
pupils_with_certificate_subjects = pd.merge(pupils_with_certificate_types, subjects, how='left', left_on='subject_id', right_on='id')[['id_x', 'name_x', 'name_y', 'score']]
print(pupils_with_certificate_subjects)


