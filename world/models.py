# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models

class Border(models.Model):
    class Meta:
        verbose_name = '行政区域データ'  # オブジェクトの人間が読める名前(単数)小文字でよい
        verbose_name_plural = '行政区域データ'  # オブジェクトの複数の名前 小文字でよい

    n03_001 = models.CharField(max_length=50)
    n03_002 = models.CharField(max_length=50)
    n03_003 = models.CharField(max_length=50)
    n03_004 = models.CharField(max_length=50)
    n03_007 = models.CharField(max_length=50)
    geom = models.PolygonField(srid=4326)

    def __str__(self):
        return self.n03_004

class School(models.Model):
    class Meta:
        verbose_name = '小学校区データ'  # オブジェクトの人間が読める名前(単数)小文字でよい
        verbose_name_plural = '小学校区データ'  # オブジェクトの複数の名前 小文字でよい

    a27_001 = models.CharField(max_length=50)
    a27_002 = models.CharField(max_length=50)
    a27_003 = models.CharField(max_length=50)
    a27_004 = models.CharField(max_length=50)
    geom = models.PointField(srid=4326)

    def __str__(self):
        return self.a27_003

class Facility(models.Model):
    class Meta:
        verbose_name = '公共施設データ '  # オブジェクトの人間が読める名前(単数)小文字でよい
        verbose_name_plural = '公共施設データ '  # オブジェクトの複数の名前 小文字でよい

    p02_001 = models.CharField(max_length=50)
    p02_002 = models.CharField(max_length=50)
    p02_003 = models.CharField(max_length=50)
    p02_004 = models.CharField(max_length=50)
    p02_005 = models.CharField(max_length=50)
    p02_006 = models.CharField(max_length=50)
    p02_007 = models.CharField(max_length=50)
    geom = models.PointField(srid=4326)

    def __str__(self):
        return self.p02_004

class Busstop(models.Model):
    class Meta:
        verbose_name = 'バス停留所データ'  # オブジェクトの人間が読める名前(単数)小文字でよい
        verbose_name_plural = 'バス停留所データ'  # オブジェクトの複数の名前 小文字でよい

    p11_001 = models.CharField(max_length=256)
    p11_002 = models.CharField(max_length=256)
    p11_003_1 = models.CharField(max_length=256)
    p11_003_2 = models.CharField(max_length=256)
    p11_003_3 = models.CharField(max_length=256)
    p11_003_4 = models.CharField(max_length=256)
    p11_003_5 = models.CharField(max_length=256)
    p11_003_6 = models.CharField(max_length=256)
    p11_003_7 = models.CharField(max_length=256)
    p11_003_8 = models.CharField(max_length=256)
    p11_003_9 = models.CharField(max_length=256)
    p11_003_10 = models.CharField(max_length=256)
    p11_003_11 = models.CharField(max_length=256)
    p11_003_12 = models.CharField(max_length=256)
    p11_003_13 = models.CharField(max_length=256)
    p11_003_14 = models.CharField(max_length=256)
    p11_003_15 = models.CharField(max_length=256)
    p11_003_16 = models.CharField(max_length=256)
    p11_003_17 = models.CharField(max_length=256)
    p11_003_18 = models.CharField(max_length=256)
    p11_003_19 = models.CharField(max_length=256)
    p11_004_1 = models.CharField(max_length=256)
    p11_004_2 = models.CharField(max_length=256)
    p11_004_3 = models.CharField(max_length=256)
    p11_004_4 = models.CharField(max_length=256)
    p11_004_5 = models.CharField(max_length=256)
    p11_004_6 = models.CharField(max_length=256)
    p11_004_7 = models.CharField(max_length=256)
    p11_004_8 = models.CharField(max_length=256)
    p11_004_9 = models.CharField(max_length=256)
    p11_004_10 = models.CharField(max_length=256)
    p11_004_11 = models.CharField(max_length=256)
    p11_004_12 = models.CharField(max_length=256)
    p11_004_13 = models.CharField(max_length=256)
    p11_004_14 = models.CharField(max_length=256)
    p11_004_15 = models.CharField(max_length=256)
    p11_004_16 = models.CharField(max_length=256)
    p11_004_17 = models.CharField(max_length=256)
    p11_004_18 = models.CharField(max_length=256)
    p11_004_19 = models.CharField(max_length=256)
    geom = models.PointField(srid=4326)

    def __str__(self):
        return self.p11_001
