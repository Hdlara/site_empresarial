# Generated by Django 3.2 on 2021-04-17 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210417_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('lni-mobile', 'Mobile'), ('lni-cog', 'Engrenagem'), ('lni-stats-up', 'Gráfico'), ('lni-layers', 'Design'), ('lni-rocket', 'Foguete'), ('lni-users', 'Usuarios')], max_length=12, verbose_name='Icone'),
        ),
        migrations.AlterField(
            model_name='tecnologia',
            name='icone',
            field=models.CharField(choices=[('lni-laptop-phone', 'Responsivo'), ('lni-cog', 'Engrenagem'), ('lni-layers', 'Design'), ('lni-rocket', 'Foguete'), ('lni-leaf', 'Folha')], max_length=20, verbose_name='Icone'),
        ),
    ]
