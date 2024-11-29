# Generated by Django 5.1.3 on 2024-11-23 10:33

import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
        ('wagtailcore', '0094_alter_page_locale'),
        ('wagtailimages', '0027_image_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('banner_heading', models.CharField(max_length=250)),
                ('banner_subheading', models.CharField(blank=True, max_length=250, null=True)),
                ('banner_description', wagtail.fields.RichTextField(blank=True)),
                ('intro', wagtail.fields.RichTextField(blank=True)),
                ('body', wagtail.fields.RichTextField(blank=True)),
                ('banner_header_image', models.ForeignKey(blank=True, help_text='Banner image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Banner Image')),
            ],
            options={
                'verbose_name': 'Blog Index Page',
                'verbose_name_plural': 'Blog Index Pages',
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='BlogPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('banner_heading', models.CharField(max_length=250)),
                ('banner_subheading', models.CharField(blank=True, max_length=250, null=True)),
                ('banner_description', wagtail.fields.RichTextField(blank=True)),
                ('date', models.DateField(verbose_name='Post date')),
                ('author', wagtail.fields.StreamField([('job_card_block', 0)], block_lookup={0: ('Blog.blocks.JobCardBlock', (), {})})),
                ('reading_time', models.CharField(max_length=50, verbose_name='Read Time')),
                ('intro', wagtail.fields.RichTextField(blank=True)),
                ('banner_header_image', models.ForeignKey(blank=True, help_text='Banner image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image', verbose_name='Banner Image')),
                ('banner_image', models.ForeignKey(blank=True, help_text='Banner image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('thumbnail_image', models.ForeignKey(blank=True, help_text='Thumbnail Image (238x170px recommended)', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'verbose_name': 'Blog Page',
                'verbose_name_plural': 'Blog Pages',
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='BlogPageTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='Blog.blogpage')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_items', to='taggit.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='blogpage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='Blog.BlogPageTag', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]