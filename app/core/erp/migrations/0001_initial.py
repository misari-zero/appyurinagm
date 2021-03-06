# Generated by Django 3.2.7 on 2021-10-23 18:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_updated', models.DateTimeField(auto_now=True, null=True)),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Nombre')),
                ('desc', models.CharField(blank=True, max_length=500, null=True, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombres o Razon social')),
                ('address', models.CharField(max_length=150, verbose_name='Direccion')),
                ('ruc', models.CharField(max_length=11, unique=True, verbose_name='Ruc')),
                ('fecha', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de registro')),
                ('state', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'db_table': 'cliente',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Elemento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro', models.CharField(max_length=2, unique=True, verbose_name='Número elemento')),
                ('name', models.CharField(max_length=120, verbose_name='Nombre de elemento')),
            ],
            options={
                'verbose_name': 'Elemento',
                'verbose_name_plural': 'Elementos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Endfinanciero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de registro')),
                ('ofinan', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Obligaciones Financieras')),
                ('ventneta', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Ventas Netas')),
                ('endfinan', models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Endeudamiento Financiero')),
            ],
            options={
                'verbose_name': 'Endeudamiento',
                'verbose_name_plural': 'Endeudamientos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Mayor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre diario')),
                ('ano', models.CharField(choices=[('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025')], default='2020', max_length=10, verbose_name='Año')),
                ('mes', models.CharField(choices=[('ENERO', 'ENERO'), ('FEBRERO', 'FEBRERO'), ('MARZO', 'MARZO'), ('ABRIL', 'ABRIL'), ('MAYO', 'MAYO'), ('JUNIO', 'JUNIO'), ('JUlIO', 'JUlIO'), ('AGOSTO', 'AGOSTO'), ('SEPTIEMBRE', 'SEPTIEMBRE'), ('OCTUBRE', 'OCTUBRE'), ('NOVIEMBRE', 'NOVIEMBRE'), ('DICIEMBRE', 'DICIEMBRE')], default='NOVIEMBRE', max_length=10, verbose_name='Mes')),
                ('date_joined', models.DateField(default=datetime.datetime.now)),
                ('desc', models.CharField(max_length=50, verbose_name='Descripción')),
                ('deudor', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('acreedor', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
            ],
            options={
                'verbose_name': 'Libro Mayor',
                'verbose_name_plural': 'Libro Mayor',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombres o Razon social')),
                ('address', models.CharField(max_length=150, verbose_name='Direccion')),
                ('ruc', models.CharField(max_length=11, unique=True, verbose_name='Ruc')),
                ('fecha', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de registro')),
                ('state', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
                'db_table': 'proveedor',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Tipocuenta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=2, unique=True, verbose_name='Código')),
                ('name', models.CharField(max_length=120, verbose_name='Nombre')),
                ('elemento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.elemento')),
            ],
            options={
                'verbose_name': 'Tipocuenta',
                'verbose_name_plural': 'Tipocuentas',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc', models.CharField(max_length=20, verbose_name='Nro documento')),
                ('date_joined', models.DateField(default=datetime.datetime.now)),
                ('date_venc', models.DateField(default=datetime.datetime.now)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('igv', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('cli', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.client')),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombres de Proyecto')),
                ('ruc', models.CharField(max_length=11, unique=True, verbose_name='Ruc')),
                ('fecha_registro', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de registro')),
                ('fecha_inicio', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de inicio')),
                ('fecha_termino', models.DateField(default=datetime.datetime.now, verbose_name='Fecha de termino')),
                ('state', models.BooleanField(default=True)),
                ('cli', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.client', verbose_name='Cliente')),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
                'db_table': 'proyecto',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('desc', models.CharField(blank=True, max_length=150, null=True, verbose_name='Descripcion')),
                ('precio', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('image', models.ImageField(blank=True, null=True, upload_to='product/%Y/%m/%d', verbose_name='Imagen')),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('cate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.categoria', verbose_name='Categoría')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Plancontable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField(default=datetime.datetime.now)),
                ('name', models.CharField(max_length=120, verbose_name='Nombre')),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.tipocuenta', verbose_name='Tipo cuenta')),
            ],
            options={
                'verbose_name': 'Cuenta',
                'verbose_name_plural': 'Cuentas',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Egreso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro', models.IntegerField()),
                ('ano', models.CharField(choices=[('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025')], default='2020', max_length=10, verbose_name='Año')),
                ('mes', models.CharField(choices=[('ENERO', 'ENERO'), ('FEBRERO', 'FEBRERO'), ('MARZO', 'MARZO'), ('ABRIL', 'ABRIL'), ('MAYO', 'MAYO'), ('JUNIO', 'JUNIO'), ('JUlIO', 'JUlIO'), ('AGOSTO', 'AGOSTO'), ('SEPTIEMBRE', 'SEPTIEMBRE'), ('OCTUBRE', 'OCTUBRE'), ('NOVIEMBRE', 'NOVIEMBRE'), ('DICIEMBRE', 'DICIEMBRE')], default='NOVIEMBRE', max_length=10, verbose_name='Mes')),
                ('date_joined', models.DateField(default=datetime.datetime.now)),
                ('desc', models.CharField(max_length=50)),
                ('debe', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('haber', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('impuestos', models.CharField(max_length=3)),
                ('cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.plancontable')),
            ],
            options={
                'verbose_name': 'Egreso',
                'verbose_name_plural': 'Egresos',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Diario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nro', models.CharField(max_length=20, verbose_name='Nro documento')),
                ('ano', models.CharField(choices=[('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025')], default='2020', max_length=10, verbose_name='Año')),
                ('mes', models.CharField(choices=[('ENERO', 'ENERO'), ('FEBRERO', 'FEBRERO'), ('MARZO', 'MARZO'), ('ABRIL', 'ABRIL'), ('MAYO', 'MAYO'), ('JUNIO', 'JUNIO'), ('JUlIO', 'JUlIO'), ('AGOSTO', 'AGOSTO'), ('SEPTIEMBRE', 'SEPTIEMBRE'), ('OCTUBRE', 'OCTUBRE'), ('NOVIEMBRE', 'NOVIEMBRE'), ('DICIEMBRE', 'DICIEMBRE')], default='NOVIEMBRE', max_length=10, verbose_name='Mes')),
                ('date_joined', models.DateField(default=datetime.datetime.now)),
                ('desc', models.CharField(max_length=50)),
                ('debe', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('haber', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('impuestos', models.CharField(max_length=3)),
                ('cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.plancontable')),
            ],
            options={
                'verbose_name': 'Diario',
                'verbose_name_plural': 'Diarios',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='DetSale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('cant', models.IntegerField(default=0)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.product')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.sale')),
            ],
            options={
                'verbose_name': 'Detalle de Venta',
                'verbose_name_plural': 'Detalle de Ventas',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='categoria',
            name='codi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.plancontable', verbose_name='Nombre cuenta'),
        ),
    ]
