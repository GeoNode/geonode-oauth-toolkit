from django.db import migrations, models
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
        migrations.AlterField(
            model_name='idtoken',
            name='jti',
            field=models.UUIDField(default=uuid.uuid4, editable=False,
                                   unique=True, verbose_name='JWT Token ID'),
        ),
        migrations.RunPython(gen_uuid, reverse_code=migrations.RunPython.noop),
    ]
