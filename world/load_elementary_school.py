# -*- coding: utf-8 -*-
import os
from django.contrib.gis.utils import LayerMapping
from world.models import School

# Modelとファイルのカラムのマッピング
mapping = {
    'a27_001' : 'A27_001',
    'a27_002' : 'A27_002',
    'a27_003' : 'A27_003',
    'a27_004' : 'A27_004',
    'geom'    : 'POINT',
}
# ファイルパス
geojson_file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'elementary_school.geojson'))

# 実行
def run(verbose=True):
    lm = LayerMapping(School, geojson_file, mapping, transform=False, encoding='UTF-8')
    lm.save(strict=True, verbose=verbose)