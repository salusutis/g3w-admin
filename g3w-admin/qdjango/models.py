from django.conf import settings
from django.db import models
from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField
from django.utils.translation import ugettext_lazy as _
from autoslug.utils import slugify
from core.models import Group
from .utils.storage import QgisFileOverwriteStorage
from model_utils import Choices
import os


def get_project_file_path(instance, filename):
    """Custom name for uploaded project files."""

    group_name = slugify(unicode(instance.group.name))
    project_name = slugify(unicode(instance.title))
    filename = u'{}_{}.qgs'.format(group_name, project_name)
    return os.path.join('projects', filename)

def get_thumbnail_path(instance, filename):
    """Custom name for uploaded thumbnails."""
    group_name = slugify(unicode(instance.group.name))
    project_name = slugify(unicode(instance.title))
    ext = filename.split('.')[-1]
    filename = u'{}_{}.{}'.format(group_name, project_name, ext)
    return os.path.join('thumbnails', filename)

class Project(TimeStampedModel):
    """A QGIS project."""

    # Project file
    qgis_file = models.FileField(
        _('QGIS project file'),
        upload_to=get_project_file_path,
        storage=QgisFileOverwriteStorage()
        )

    # General info
    title = models.CharField(_('Title'), max_length=255)
    description = models.TextField(_('Description'), blank=True)
    slug = AutoSlugField(
        _('Slug'), populate_from='title', unique=True, always_update=True
        )
    is_active = models.BooleanField(_('Is active'), default=1)

    # Thumbnail
    thumbnail = models.ImageField(_('Thumbnail'), blank=True, null=True)

    # Group
    group = models.ForeignKey(Group, related_name='qdjango_project_group', verbose_name=_('Group'))


    # Extent
    initial_extent = models.CharField(_('Initial extent'), max_length=255)
    max_extent = models.CharField(_('Max extent'), max_length=255)

    # Whether current project acts as a panoramic map within group
    is_panoramic_map = models.BooleanField(_('Is panoramic map'), default=0)

    #Qgis version project
    qgis_version = models.CharField(_('Qgis project version'), max_length=255, default='')

    class Meta:
        unique_together = (('title', 'group'))
        permissions = (
            ('view_project', 'Can view project'),
        )


class Layer(models.Model):
    """A QGIS layer."""

    TYPES = Choices(
        ('postgres', _('Postgres')),
        ('spatialite', _('SpatiaLite')),
        ('wfs', _('WFS')),
        ('wms', _('WMS')),
        ('ogr', _('OGR')),
        ('gdal', _('GDAL')),
        )
    # General info
    name = models.CharField(_('Name'), max_length=255)
    title = models.CharField(_('Title'), max_length=255, blank=True)
    description = models.TextField(_('Description'), blank=True)
    slug = AutoSlugField(
        _('Slug'), populate_from='name', unique=True, always_update=True
        )
    is_active = models.BooleanField(_('Is active'), default=1)
    # Project
    project = models.ForeignKey(Project, verbose_name=_('Project'))
    # Type and content
    layer_type = models.CharField(_('Type'), choices=TYPES, max_length=255)
    datasource = models.TextField(_('Datasource'))
    is_visible = models.BooleanField(_('Is visible'), default=1)
    order = models.IntegerField(_('Order'),default=1)
    # Optional data file (non-postgres layers need it)
    data_file = models.FileField(
        _('Associated data file'),
        upload_to=settings.DATASOURCE_PATH,
        blank=True,
        null=True
        )
    # Database columns (postgres layers need it)
    database_columns = models.TextField(_('Database columns'), blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        unique_together = (('name', 'project',),)
        ordering = ['order']
        permissions = (
            ('view_layer', 'Can view layer'),
        )