import pandas as pd
import numpy as np
from connect_to_json import json_data as j


certificates = pd.DataFrame(j['certificates'])

def dist(x):
    return x.max() - x.min()

sertifikat_types = certificates.groupby('type')['id'].agg(['max', 'min', dist]).reset_index()
print(sertifikat_types)
