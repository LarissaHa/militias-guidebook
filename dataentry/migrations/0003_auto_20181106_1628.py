# Generated by Django 2.0.9 on 2018-11-06 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dataentry', '0002_target_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('abbreviation', models.CharField(max_length=3, verbose_name='Abbreviation')),
                ('code', models.IntegerField(verbose_name='Code')),
                ('level1region', models.CharField(choices=[('Asia', 'Asia'), ('Africa', 'Africa'), ('Americas', 'Americas'), ('Oceania', 'Oceania'), ('Europe', 'Europe')], default='Africa', max_length=30, verbose_name='Level 1 Region')),
                ('level2region', models.CharField(choices=[('Eastern Africa', 'Eastern Africa'), ('Middle Africa', 'Middle Africa'), ('Northern Africa', 'Northern Africa'), ('Southern Africa', 'Southern Africa'), ('Western Africa', 'Western Africa'), ('Caribbean', 'Caribbean'), ('Central America', 'Central America'), ('South America', 'South America'), ('Northern America', 'Northern America'), ('Central Asia', 'Central Asia'), ('Eastern Asia', 'Eastern Asia'), ('Southern Asia', 'Southern Asia'), ('South-Eastern Asia', 'South-Eastern Asia'), ('Western Asia', 'Western Asia'), ('Eastern Europe', 'Eastern Europe'), ('Northern Europe', 'Northern Europe'), ('Southern Europe', 'Southern Europe'), ('Western Europe', 'Western Europe'), ('Australia and New Zealand', 'Australia and New Zealand'), ('Melanesia', 'Melanesia'), ('Micronesia', 'Micronesia'), ('Polynesia', 'Polynesia')], default='Eastern Africa', max_length=30, verbose_name='Level 2 Region')),
                ('isoalpha2', models.CharField(blank=True, max_length=2, verbose_name='Abbrev. (2 letter)')),
            ],
            options={
                'verbose_name': 'country',
                'verbose_name_plural': 'countries',
            },
        ),
        migrations.CreateModel(
            name='Ethnic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(help_text='Please enter EPR group name and add country in brackets. Example: Israeli Arabs (Israel)', max_length=200, verbose_name='EPR Name (Country)')),
                ('cowgroupid', models.PositiveIntegerField(blank=True, default=0, help_text='Please provide EPR cowgroupid', null=True, verbose_name='cowgroupid')),
            ],
            options={
                'verbose_name': 'Ethnic Group (EPR)',
                'verbose_name_plural': 'Ethnic Groups (EPR)',
            },
        ),
        migrations.CreateModel(
            name='Evidence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=300, verbose_name='Publication')),
                ('date', models.DateField(help_text='Please use the following format: YYYY-MM-DD.')),
                ('quote', models.TextField(max_length=1500)),
            ],
            options={
                'verbose_name': 'piece of evidence',
                'verbose_name_plural': 'pieces of evidence',
            },
        ),
        migrations.CreateModel(
            name='GovernmentCreator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='GovernmentLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MemberCharacteristic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(choices=[('1981', '1981'), ('1982', '1982'), ('1983', '1983'), ('1984', '1984'), ('1985', '1985'), ('1986', '1986'), ('1987', '1987'), ('1988', '1988'), ('1989', '1989'), ('1990', '1990'), ('1991', '1991'), ('1992', '1992'), ('1993', '1993'), ('1994', '1994'), ('1995', '1995'), ('1996', '1996'), ('1997', '1997'), ('1998', '1998'), ('1999', '1999'), ('2000', '2000'), ('2001', '2001'), ('2002', '2002'), ('2003', '2003'), ('2004', '2004'), ('2005', '2005'), ('2006', '2006'), ('2007', '2007'), ('2008', '2008'), ('2009', '2009'), ('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015')], default='1981', max_length=4, verbose_name='Year')),
                ('incidents', models.IntegerField(verbose_name='Number of incidents')),
            ],
        ),
        migrations.CreateModel(
            name='PGAG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('madeup', models.BooleanField(default=False, verbose_name='Name assigned by coder')),
                ('date_formed', models.DateField(help_text='Please use the following format: YYYY-MM-DD.', verbose_name='Date formed or first mentioned')),
                ('accuracy_formed', models.CharField(choices=[('dec', 'decade'), ('yr', 'year'), ('mo', 'month'), ('dy', 'day')], default='dy', max_length=30, verbose_name='Accuracy of date formed')),
                ('date_dissolved', models.DateField(blank=True, help_text='Please use the following format: YYYY-MM-DD.', null=True, verbose_name='Date dissolved')),
                ('accuracy_dissolved', models.CharField(choices=[('dec', 'decade'), ('yr', 'year'), ('mo', 'month'), ('dy', 'day')], default='dy', max_length=30, verbose_name='Accuracy of date dissolved')),
                ('prior_group', models.CharField(choices=[('noinf', 'no information'), ('yes', 'yes'), ('no', 'no'), ('unclear', 'unclear')], default='noinf', max_length=30, verbose_name='Former Existing Group?')),
                ('prior_armed', models.CharField(choices=[('noinf', 'no information'), ('yes', 'yes'), ('no', 'no'), ('unclear', 'unclear'), ('NA', 'NA')], default='NA', max_length=30, verbose_name='Former Armed Group?')),
                ('prior_rebel', models.CharField(choices=[('noinf', 'no information'), ('yes', 'yes'), ('no', 'no'), ('unclear', 'unclear'), ('NA', 'NA')], default='NA', max_length=30, verbose_name='Former Rebel Group?')),
                ('post_rebel', models.CharField(choices=[('noinf', 'no information'), ('yes', 'yes'), ('no', 'no'), ('unclear', 'unclear')], default='noinf', max_length=30, verbose_name='PGM becomes Rebel Group?')),
                ('pmc', models.CharField(choices=[('noinf', 'no information'), ('yes', 'yes'), ('no', 'no'), ('unclear', 'unclear')], default='noinf', max_length=30, verbose_name='PMC')),
                ('government_relation', models.CharField(choices=[('type1or2', 'unclear (type 1 or 2)'), ('type2', 'semi-official (type 2)'), ('type1', 'informal (type 1)'), ('unclear', 'unclear')], default='type1', max_length=30, verbose_name='Government relation')),
                ('gov_formed', models.CharField(choices=[('noinf', 'no information'), ('yes', 'yes'), ('no', 'no'), ('unclear', 'unclear')], default='noinf', max_length=30, verbose_name='Created by Government?')),
                ('party_id', models.CharField(blank=True, help_text='Name of Political Party linked to PGM', max_length=100, null=True, verbose_name='Name of Party Link')),
                ('government_trained', models.CharField(choices=[('noinf', 'no information'), ('yes', 'yes'), ('no', 'no'), ('unclear', 'unclear')], default='noinf', max_length=30)),
                ('information_shared', models.CharField(choices=[('noinf', 'no information'), ('yes', 'yes'), ('no', 'no'), ('unclear', 'unclear')], default='noinf', max_length=30, verbose_name='Shared information')),
                ('personnel_shared', models.CharField(choices=[('noinf', 'no information'), ('yes', 'yes'), ('no', 'no'), ('unclear', 'unclear')], default='noinf', max_length=30, verbose_name='Shared personnel')),
                ('other_connection', models.CharField(blank=True, max_length=400, verbose_name='Other connection')),
                ('info_ethnic_targ', models.CharField(choices=[('giv', 'given'), ('inf', 'inferred'), ('na', 'not applicable')], default='na', max_length=30, verbose_name='Quality of Information for Ethnic Targeting')),
                ('info_ethnic_mem', models.CharField(choices=[('giv', 'given'), ('inf', 'inferred'), ('na', 'not applicable')], default='na', max_length=30, verbose_name='Quality of Information for Ethnic Membership')),
                ('info_ethnic_purp', models.CharField(choices=[('giv', 'given'), ('inf', 'inferred'), ('na', 'not applicable')], default='na', max_length=30, verbose_name='Quality of Information for Ethnic Purpose')),
                ('location', models.CharField(blank=True, help_text='Primary location of activities', max_length=200, null=True)),
                ('headcount_low', models.PositiveIntegerField(blank=True, null=True, verbose_name='Minimum headcount')),
                ('headcount_high', models.PositiveIntegerField(blank=True, null=True, verbose_name='Maximum headcount')),
                ('origin', models.TextField(blank=True, max_length=500)),
                ('termination', models.TextField(blank=True, max_length=500)),
                ('other', models.TextField(blank=True, max_length=1000)),
                ('forced_mem', models.CharField(choices=[('giv', 'given'), ('inf', 'inferred'), ('na', 'not applicable')], default='na', max_length=30, verbose_name='Forced Membership')),
                ('primary_mem', models.CharField(choices=[('noinf', 'no information'), ('ethnic', 'ethnic'), ('ideological', 'ideological'), ('local', 'local'), ('nationalist', 'nationalist'), ('noncivilian', 'non-civilian'), ('political', 'political'), ('religious', 'religious'), ('other', 'other'), ('unclear', 'unclear')], default='noinf', max_length=30, verbose_name='Primary Membership')),
                ('alt_primary_mem', models.CharField(choices=[('noinf', 'no information'), ('ethnic', 'ethnic'), ('ideological', 'ideological'), ('local', 'local'), ('nationalist', 'nationalist'), ('noncivilian', 'non-civilian'), ('political', 'political'), ('religious', 'religious'), ('other', 'other'), ('unclear', 'unclear')], default='noinf', max_length=30, verbose_name='Alternative Primary Membership')),
                ('purpose_text', models.TextField(blank=True, max_length=1000, verbose_name='Purpose')),
                ('treatment_civilians', models.TextField(blank=True, max_length=1000, verbose_name='Treatment of Civilians')),
                ('members_killed', models.CharField(choices=[('noinf', 'no information'), ('never', 'never'), ('rarely', 'rarely'), ('sometimes', 'sometimes'), ('often', 'often'), ('unclear', 'unclear')], default='noinf', max_length=30)),
                ('members_coerced', models.CharField(choices=[('noinf', 'no information'), ('yes', 'yes'), ('no', 'no'), ('unclear', 'unclear')], default='noinf', max_length=30)),
                ('members_paid', models.CharField(choices=[('noinf', 'no information'), ('yes', 'yes'), ('no', 'no'), ('unclear', 'unclear')], default='noinf', max_length=30, verbose_name='Members paid')),
                ('size', models.TextField(blank=True, max_length=1000, verbose_name='Size')),
                ('weapon_training', models.TextField(blank=True, max_length=1000, verbose_name='Weapons and Training')),
                ('organisation', models.TextField(blank=True, max_length=1000, verbose_name='Organisation')),
                ('reason_membership', models.TextField(blank=True, max_length=1000, verbose_name='Reasons for Membership')),
                ('reference_meta', models.TextField(blank=True, help_text='Please add references in alphabetical order and insert an empty line after each reference.', max_length=10000, verbose_name='References for Meta-Analysis')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dataentry.Country')),
                ('ethnic_mem', models.ManyToManyField(blank=True, help_text='Select or add EPR Group', null=True, related_name='ethnic_target', to='dataentry.Ethnic', verbose_name='Ethnic Membership')),
                ('ethnic_purp', models.ManyToManyField(blank=True, help_text='Select or add EPR Group', null=True, related_name='ethnic_mem', to='dataentry.Ethnic', verbose_name='Ethnic Purpose')),
                ('ethnic_targ', models.ManyToManyField(blank=True, help_text='Select or add EPR Group', null=True, to='dataentry.Ethnic', verbose_name='Ethnic Target')),
                ('government_creator', models.ManyToManyField(blank=True, to='dataentry.GovernmentCreator', verbose_name='Creating Government Institution')),
                ('government_link', models.ManyToManyField(to='dataentry.GovernmentLink')),
                ('membership', models.ManyToManyField(to='dataentry.MemberCharacteristic')),
            ],
            options={
                'verbose_name': 'PGM',
                'verbose_name_plural': 'PGMs',
            },
        ),
        migrations.CreateModel(
            name='Purpose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'group purpose',
            },
        ),
        migrations.CreateModel(
            name='RelativeBenefit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TermType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Termination Type',
                'verbose_name_plural': 'Termination Types',
            },
        ),
        migrations.CreateModel(
            name='TypeViolence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'type of violence',
                'verbose_name_plural': 'types of violence',
            },
        ),
        migrations.CreateModel(
            name='UCDP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'UCDP Actor ID',
            },
        ),
        migrations.AlterModelOptions(
            name='support',
            options={'verbose_name': 'type of material support', 'verbose_name_plural': 'types of material support'},
        ),
        migrations.RenameField(
            model_name='target',
            old_name='target_name',
            new_name='type',
        ),
        migrations.RemoveField(
            model_name='support',
            name='supporters',
        ),
        migrations.RemoveField(
            model_name='support',
            name='target',
        ),
        migrations.RemoveField(
            model_name='support',
            name='votes',
        ),
        migrations.RemoveField(
            model_name='target',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='support',
            name='type',
            field=models.CharField(default='x', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pgag',
            name='post_ucdp',
            field=models.ManyToManyField(blank=True, related_name='prior_group', to='dataentry.UCDP', verbose_name='UCDP Actor ID of successor rebel group'),
        ),
        migrations.AddField(
            model_name='pgag',
            name='predecessor_group',
            field=models.ManyToManyField(blank=True, null=True, to='dataentry.PGAG'),
        ),
        migrations.AddField(
            model_name='pgag',
            name='prior_ucdp',
            field=models.ManyToManyField(blank=True, to='dataentry.UCDP', verbose_name='UCDP Actor ID of former rebel group'),
        ),
        migrations.AddField(
            model_name='pgag',
            name='purpose',
            field=models.ManyToManyField(to='dataentry.Purpose'),
        ),
        migrations.AddField(
            model_name='pgag',
            name='relative_benefit',
            field=models.ManyToManyField(blank=True, null=True, to='dataentry.RelativeBenefit', verbose_name='Relative Benefit'),
        ),
        migrations.AddField(
            model_name='pgag',
            name='successor_group',
            field=models.ManyToManyField(blank=True, null=True, related_name='successors', to='dataentry.PGAG'),
        ),
        migrations.AddField(
            model_name='pgag',
            name='support_types',
            field=models.ManyToManyField(to='dataentry.Support', verbose_name='Types of material support'),
        ),
        migrations.AddField(
            model_name='pgag',
            name='supporters',
            field=models.ManyToManyField(blank=True, null=True, related_name='sponsors', to='dataentry.Country', verbose_name='State sponsors'),
        ),
        migrations.AddField(
            model_name='pgag',
            name='target',
            field=models.ManyToManyField(blank=True, null=True, to='dataentry.Target'),
        ),
        migrations.AddField(
            model_name='pgag',
            name='termination_types',
            field=models.ManyToManyField(blank=True, to='dataentry.TermType', verbose_name='Termination Types'),
        ),
        migrations.AddField(
            model_name='pgag',
            name='type_violence',
            field=models.ManyToManyField(blank=True, null=True, to='dataentry.TypeViolence', verbose_name='Types of Violence'),
        ),
        migrations.AddField(
            model_name='operation',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='dataentry.PGAG'),
        ),
        migrations.AddField(
            model_name='evidence',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='backing', to='dataentry.PGAG'),
        ),
    ]