from django.contrib.auth.models import User
from django.db import models


class DomainConfig(models.Model):
    """meta data about a domain"""
    class Meta:
        app_label = 'raas'
    user = models.ForeignKey(User)
    domain = models.CharField(max_length=255)
    # number of recommendation to return
    number_of_rec = models.IntegerField(default=5)
    filename = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Field(models.Model):
    class Meta:
        app_label = 'raas'

    FIELD_TYPE_UNKNOWN = 0
    FIELD_TYPE_TEXT = 1
    FIELD_TYPE_NUMERIC = 2
    FIELD_TYPE_DATE = 3
    FIELD_TYPE_DATETIME = 4
    FIELD_TYPE_NUM_RANGE = 5
    FIELD_TYPE_DATE_RANGE = 6
    FIELD_TYPE_TAGS = 7
    FIELD_TYPE_DICT = 8
    FIELD_TYPE_ID = 9
    FIELD_TYPE_SINGLE = 10
    FIELD_TYPE_LOCATION = 11
    FIELD_TYPE_INTEGER = 12
    FIELD_TYPE_FLOAT = 13
    FIELD_TYPE_BOOLEAN = 14
    FIELD_TYPE_KEYWORDS = 15
    FIELD_TYPE_RESERVED4 = 16
    FIELD_TYPE_RESERVED5 = 17

    FIELD_TYPES = (
        (FIELD_TYPE_UNKNOWN, 'unknown'),
        (FIELD_TYPE_TEXT, 'text'),
        (FIELD_TYPE_NUMERIC, 'numeric'),
        (FIELD_TYPE_DATE, 'date'),
        (FIELD_TYPE_DATETIME, 'datetime'),
        (FIELD_TYPE_NUM_RANGE, 'numeric_range'),
        (FIELD_TYPE_DATE_RANGE, 'date_range'),
        (FIELD_TYPE_TAGS, 'tags'),
        (FIELD_TYPE_DICT, 'dict'),
        (FIELD_TYPE_ID, 'id'),
        (FIELD_TYPE_SINGLE, 'single'),
        (FIELD_TYPE_LOCATION, 'location'),
        (FIELD_TYPE_INTEGER, 'integer'),
        (FIELD_TYPE_FLOAT, 'float'),
        (FIELD_TYPE_BOOLEAN, 'boolean'),
        (FIELD_TYPE_KEYWORDS, 'keywords'),
        (FIELD_TYPE_RESERVED4, 'Reserved4'),
        (FIELD_TYPE_RESERVED5, 'Reserved5'))

    field_dict = {}
    domain = models.ForeignKey(DomainConfig)
    name = models.CharField(max_length=100, default="")
    ftype = models.IntegerField(choices=FIELD_TYPES, default=0)
    column = models.IntegerField()

    @classmethod
    def get_field_dict(cls):
        if not cls.field_dict:
            for k, v in cls.FIELD_TYPES:
                cls.field_dict[v] = k
        return cls.field_dict

    @classmethod
    def get_field_type(cls, field):
        """Given a field id, get the field name"""
        if (field < len(cls.FIELD_TYPES)):
            return cls.FIELD_TYPES[field][1]
        return 'unknown'

    @classmethod
    def get_field_class_name(cls, field):
        """Given a field name, get the field class name"""
        return field.capitalize() + "Field"


class SearchModel(models.Model):
    """Recommendation model for search job"""
    class Meta:
        app_label = 'raas'
    domain = models.ForeignKey(DomainConfig)
    name = models.CharField(max_length=50, default="")
    description = models.TextField(default="")
    content = models.TextField(default="")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class RankModel(models.Model):
    """Recommendation model for rank job"""
    class Meta:
        app_label = 'raas'
    domain = models.ForeignKey(DomainConfig)
    name = models.CharField(max_length=50, default="")
    description = models.TextField(default="")
    content = models.TextField(default="")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class RecModel(models.Model):
    """Recommendation model default meta data"""
    class Meta:
        app_label = 'raas'
    domain = models.ForeignKey(DomainConfig)
    current_search_model = models.ForeignKey(SearchModel, null=True, blank=True)
    current_rank_model = models.ForeignKey(RankModel, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class DocumentFile(models.Model):
    """Document in DB to source data file relation"""
    FILE_STATUS = (
        (0, 'ready'),
        (1, 'stored')
    )
    class Meta:
        app_label = 'raas'
    domain = models.ForeignKey(DomainConfig)
    file = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=FILE_STATUS, default=0)

