from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('status', models.CharField(choices=[('published', 'Published'), ('draft', 'Draft')], max_length=20)),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_Article.author')),
                ('category_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_Article.category')),
                ('tags', models.ManyToManyField(blank=True, to='app_Article.tag')),
            ],
        ),
    ]
