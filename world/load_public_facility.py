# -*- coding: utf-8 -*-
import os
from django.contrib.gis.utils import LayerMapping
from world.models import Facility

# Modelとファイルのカラムのマッピング
mapping = {
    'p02_001' : 'P02_001',
    'p02_002' : 'P02_002',
    'p02_003' : 'P02_003',
    'p02_004' : 'P02_004',
    'p02_005' : 'P02_005',
    'p02_006' : 'P02_006',
    'p02_007' : 'P02_007',
    'geom'    : 'POINT',
}

# ファイルパス
geojson_file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'public_facility.geojson'))

# 実行
def run(verbose=True):
    lm = LayerMapping(Facility, geojson_file, mapping, transform=False, encoding='UTF-8')
    lm.save(strict=True, verbose=verbose)
