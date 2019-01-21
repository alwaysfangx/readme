# Generated by Django 2.1.5 on 2019-01-21 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apistep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apistep', models.CharField(max_length=100, null=True, verbose_name='测试步骤')),
                ('apiname', models.CharField(max_length=100, verbose_name='接口名称')),
                ('apiurl', models.CharField(max_length=200, verbose_name='url地址')),
                ('apiparamvalue', models.CharField(max_length=800, verbose_name='请求参数和值')),
                ('apimethod', models.CharField(max_length=200, verbose_name='方法')),
                ('apiresult', models.CharField(max_length=200, verbose_name='预期结果')),
                ('apistatus', models.BooleanField(verbose_name='是否通过')),
                ('creat_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
            ],
        ),
        migrations.CreateModel(
            name='Apitest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apitestname', models.CharField(max_length=64, verbose_name='流程接口名称')),
                ('apitester', models.CharField(max_length=16, verbose_name='执行人')),
                ('apitestresult', models.BooleanField(verbose_name='测试结果')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
            ],
        ),
        migrations.AddField(
            model_name='apistep',
            name='Apitest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apitest.Apitest'),
        ),
    ]
