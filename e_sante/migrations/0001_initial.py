# Generated by Django 3.2.6 on 2021-09-14 10:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cabinet',
            fields=[
                ('id_cabinet', models.AutoField(primary_key=True, serialize=False)),
                ('intitule', models.CharField(max_length=254)),
                ('address', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254)),
                ('tel', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('fax', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
            ],
        ),
        migrations.CreateModel(
            name='FichePatient',
            fields=[
                ('id_fiche', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=254)),
                ('prenom', models.CharField(max_length=254)),
                ('address', models.CharField(max_length=254)),
                ('age', models.IntegerField()),
                ('sexe', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('U', 'Unsure')], default=None, max_length=1)),
                ('tel', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None)),
                ('email', models.EmailField(max_length=254)),
                ('group_sanguin', models.CharField(choices=[('O+', 'O+'), ('O-', 'O-'), ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-')], default=None, max_length=3)),
                ('NSS', models.CharField(max_length=254)),
                ('profession', models.CharField(max_length=254)),
                ('motif_consultation', models.CharField(max_length=254)),
                ('nom_etablissement_universitaire', models.CharField(max_length=254)),
                ('date_naiss', models.DateField()),
                ('lieu_naiss', models.CharField(max_length=254)),
                ('situation', models.CharField(choices=[('celebataire', 'celebataire'), ('Marié', 'Marié'), ('Divorcé', 'Divorcé'), ('veuf', 'veuf')], default=None, max_length=11)),
                ('filiére', models.CharField(max_length=254)),
                ('à_fumer', models.CharField(choices=[('Oui', 'Oui'), ('Non', 'Non')], default=None, max_length=3)),
                ('à_chiquer', models.CharField(choices=[('Oui', 'Oui'), ('Non', 'Non')], default=None, max_length=3)),
                ('à_prise', models.CharField(choices=[('Oui', 'Oui'), ('Non', 'Non')], default=None, max_length=3)),
                ('nbr_cigarettes', models.IntegerField(blank=True)),
                ('nbr_boites', models.IntegerField(blank=True)),
                ('age_à_la_premiére_prise', models.IntegerField()),
                ('ancien_fumeur', models.CharField(choices=[('Oui', 'Oui'), ('Non', 'Non')], default=None, max_length=3)),
                ('periode_exposition', models.IntegerField(blank=True)),
                ('Affections_congénitales', models.TextField(max_length=254)),
                ('Maladies_génerale', models.TextField(max_length=254)),
                ('Interventions_chirurgicales', models.TextField(max_length=254)),
                ('Réactions_allergique_aux_médicaments', models.TextField(max_length=254)),
                ('id_medecin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fich_med', to=settings.AUTH_USER_MODEL)),
                ('id_patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fich_patient', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rdv',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('num_rdv', models.IntegerField(default='1')),
                ('id_medecin', models.ForeignKey(default='3', on_delete=django.db.models.deletion.CASCADE, related_name='rdv_med', to=settings.AUTH_USER_MODEL)),
                ('id_patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rdv_patient', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ordonnance',
            fields=[
                ('id_ordonnance', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('medicament', models.CharField(max_length=254)),
                ('observation', models.TextField(max_length=254)),
                ('name_patient', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='ORD_patient', to='e_sante.fichepatient')),
            ],
        ),
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id_consultation', models.AutoField(primary_key=True, serialize=False)),
                ('contenue', models.TextField(max_length=254)),
                ('antecedant', models.CharField(max_length=254)),
                ('traitement', models.CharField(max_length=254)),
                ('date_consultation', models.DateTimeField()),
                ('id_patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cons_patient', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]