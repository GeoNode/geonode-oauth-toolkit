from django.db import migrations
import uuid

def gen_uuid(apps, schema_editor):
    MyModel = apps.get_model('oauth2_provider', 'idtoken')
    for row in MyModel.objects.all():
        row.jti = uuid.uuid4()
        row.save(update_fields=['jti'])

class Migration(migrations.Migration):

    dependencies = [
        ('oauth2_provider', '0014_auto_20210510_0935'),
    ]

    operations = [
        migrations.RunPython(gen_uuid, reverse_code=migrations.RunPython.noop),
    ]
