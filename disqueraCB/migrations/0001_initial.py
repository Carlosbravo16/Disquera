# Generated by Django 4.1.1 on 2023-07-29 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombreAlbum', models.CharField(max_length=100)),
                ('anioPublicacion', models.CharField(max_length=5)),
                ('fotoAlbum', models.CharField(max_length=255)),
                ('estadoAlbum', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Disquera',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nitdisquera', models.CharField(max_length=25)),
                ('nombredisquera', models.CharField(max_length=100)),
                ('telefonodisquera', models.CharField(max_length=15)),
                ('direcciondisquera', models.CharField(max_length=100)),
                ('estadodisquera', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombreAlbum', models.CharField(max_length=50)),
                ('estadoGenero', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Cancion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombreCancion', models.CharField(max_length=100)),
                ('duracionCancion', models.IntegerField()),
                ('estadoCancion', models.BooleanField()),
                ('iddAlbumfk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disqueraCB.album')),
            ],
        ),
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('noDocumento', models.CharField(max_length=25)),
                ('tipoDocumento', models.CharField(max_length=20)),
                ('nombreArtista', models.CharField(max_length=50)),
                ('apellidoArtista', models.CharField(max_length=50)),
                ('nombreArtistico', models.CharField(max_length=50)),
                ('fNacimArtist', models.DateField(blank=True, null=True)),
                ('emailArtista', models.CharField(max_length=100)),
                ('fotoArtista', models.ImageField(blank=True, null=True, upload_to='imagenes/')),
                ('estadoArtista', models.BooleanField()),
                ('iddisquerafk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disqueraCB.disquera')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='idartistafk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disqueraCB.artista'),
        ),
        migrations.AddField(
            model_name='album',
            name='idgenerofk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disqueraCB.genero'),
        ),
    ]
