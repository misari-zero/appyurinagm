from django.db import models
from datetime import datetime
from django.forms import model_to_dict, TextInput

from app.settings import MEDIA_URL, STATIC_URL
from core.erp.choices import mes_choices, ano_choices
from core.models import BaseModel
from django.forms import model_to_dict
from django.db.models import signals


class Client(models.Model):
    # type = models.ForeignKey(Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, verbose_name='Nombres o Razon social')
    address = models.CharField(max_length=150, verbose_name='Direccion')
    ruc = models.CharField(max_length=11, unique=True, verbose_name='Ruc')
    fecha = models.DateField(default=datetime.now, verbose_name='Fecha de registro')
    # gender = models.CharField(max_length=10, choices=gender_choices, default='male', verbose_name='Sexo')
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        item['fecha'] = self.fecha.strftime('%Y-%m-%d')
        return item

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'cliente'
        ordering = ['id']

class Proveedor(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombres o Razon social')
    address = models.CharField(max_length=150, verbose_name='Direccion')
    ruc = models.CharField(max_length=11, unique=True, verbose_name='Ruc')
    fecha = models.DateField(default=datetime.now, verbose_name='Fecha de registro')
    # gender = models.CharField(max_length=10, choices=gender_choices, default='male', verbose_name='Sexo')
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        item['fecha'] = self.fecha.strftime('%Y-%m-%d')
        return item

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        db_table = 'proveedor'
        ordering = ['id']


class Elemento(models.Model):
    nro = models.CharField(max_length=2, verbose_name='Número elemento', unique=True)
    name = models.CharField(max_length=120, verbose_name='Nombre de elemento')

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item


    class Meta:
        verbose_name = 'Elemento'
        verbose_name_plural = 'Elementos'
        ordering = ['id']


class Tipocuenta(models.Model):
    codigo = models.CharField(max_length=2, verbose_name='Código', unique=True)
    name = models.CharField(max_length=120, verbose_name='Nombre')
    elemento = models.ForeignKey(Elemento, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Tipocuenta'
        verbose_name_plural = 'Tipocuentas'
        ordering = ['id']


class Plancontable(models.Model):
    date_joined = models.DateField(default=datetime.now)
    tipo = models.ForeignKey(Tipocuenta, on_delete=models.CASCADE, verbose_name='Tipo cuenta')
    name = models.CharField(max_length=120, verbose_name='Nombre')
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    # cta = models.CharField(max_length=7, verbose_name='CTA', unique=True)

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        item['tipo'] = self.tipo.toJSON()
        return item

    class Meta:
        verbose_name = 'Cuenta'
        verbose_name_plural = 'Cuentas'
        ordering = ['id']

# def update_debe(sender, instance, **kwargs):
#     instance.diario.debe += instance.total
#     instance.diario.save()
# #register the signal
# signals.post_save.connect(update_debe, sender=Plancontable, dispatch_uid="update_debe_count")

# class AsientoContable(models.Model):
#     nro = models.IntegerField(max_digits=5, verbose_name='#Asiento')
#     fecha = models.DateField(default=datetime.now, verbose_name='Fecha')
#     glosario = models.CharField(max_length=120, verbose_name='Glosa')
#     doc = models.IntegerField(max_digits=8, verbose_name='Documento')
#     tipo_doc = models.CharField(max_length=120, verbose_name='Tipo de Documento')
#     cuenta = models.ForeignKey(Plancontable, on_delete=models.CASCADE, verbose_name='CUENTA')
#     detalle = models.CharField(max_length=120, verbose_name='DETALLE DE CUENTA')
#     debe = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='DEBE')
#     haber = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='HABER')
#
#     def __str__(self):
#         return self.glosario
#
#     class Meta:
#         verbose_name = 'Asiento'
#         verbose_name_plural = 'Asientos'
#         ordering = ['id']
#
#     def toJSON(self):
#         item = model_to_dict(self)
#         item['fecha'] = self.fecha.strftime('%Y-%m-%d')
#         item['glosario'] = self.cli.toJSON()
#         item['glosario'] = format(self.pre, '.2f')
#         return item

class Categoria(BaseModel):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    desc = models.CharField(max_length=500, blank=True, null=True, verbose_name='Descripción')
    codi = models.ForeignKey(Plancontable, on_delete=models.CASCADE, verbose_name='Nombre cuenta')

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre')
    cate = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoría')
    desc = models.CharField(max_length=150, verbose_name='Descripcion', null=True, blank=True)
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True, verbose_name='Imagen')
    state = models.BooleanField(default=True, verbose_name='Estado')

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        item['cate'] = self.cate.toJSON()
        item['image'] = self.get_image()
        item['precio'] = format(self.precio, '.2f')
        return item

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']


class Project(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombres de Proyecto')
    cli = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Cliente')
    ruc = models.CharField(max_length=11, unique=True, verbose_name='Ruc')
    pre = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio')
    fecha_registro = models.DateField(default=datetime.now, verbose_name='Fecha de registro')
    fecha_inicio = models.DateField(default=datetime.now, verbose_name='Fecha de inicio')
    fecha_termino = models.DateField(default=datetime.now, verbose_name='Fecha de termino')
    # image = models.ImageField(upload_to='project/%Y/%m/%d', null=True, blank=True, verbose_name='Imagen')
    state = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        item['cli'] = self.cli.toJSON()
        item['pre'] = format(self.pre, '.2f')
        item['fecha_registo'] = self.fecha_registro.strftime('%Y-%m-%d')
        item['fecha_inicio'] = self.fecha_inicio.strftime('%Y-%m-%d')
        item['fecha_termino'] = self.fecha_termino.strftime('%Y-%m-%d')
        # item['image'] = self.get_image()
        return item

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        db_table = 'proyecto'
        ordering = ['id']

class Sale(models.Model):
    doc = models.CharField(max_length=20, verbose_name="Nro documento")
    cli = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now)
    date_venc = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    igv = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.cli.name

    def toJSON(self):
        item = model_to_dict(self)
        # item['doc'] = self.doc.toJSON()
        item['cli'] = self.cli.toJSON()
        item['subtotal'] = format(self.subtotal, '.2f')
        item['igv'] = format(self.igv, '.2f')
        item['total'] = format(self.total, '.2f')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['date_venc'] = self.date_venc.strftime('%Y-%m-%d')
        item['det'] = [i.toJSON() for i in self.detsale_set.all()]
        return item

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']


class DetSale(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cant = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.prod.name

    def toJSON(self):
        item = model_to_dict(self, exclude=['sale'])
        item['prod'] = self.prod.toJSON()
        item['price'] = format(self.price, '.2f')
        item['subtotal'] = format(self.subtotal, '.2f')
        return item

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalle de Ventas'
        ordering = ['id']


class Ingreso(models.Model):
    doc = models.CharField(max_length=20, verbose_name="Nro documento")
    cli = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now)
    date_venc = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    igv = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.cli.name

    def toJSON(self):
        item = model_to_dict(self)
        item['cli'] = self.cli.toJSON()
        item['subtotal'] = format(self.subtotal, '.2f')
        item['igv'] = format(self.igv, '.2f')
        item['total'] = format(self.total, '.2f')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['date_venc'] = self.date_venc.strftime('%Y-%m-%d')
        item['det'] = [i.toJSON() for i in self.detingreso_set.all()]
        return item

    class Meta:
        verbose_name = 'Ingreso'
        verbose_name_plural = 'Ingresos'
        ordering = ['id']

class DetIngreso(models.Model):
    ingreso = models.ForeignKey(Ingreso, on_delete=models.CASCADE)
    proj = models.ForeignKey(Project, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cant = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.proj.name

    def toJSON(self):
        item = model_to_dict(self, exclude=['ingreso'])
        item['proj'] = self.proj.toJSON()
        item['price'] = format(self.price, '.2f')
        item['subtotal'] = format(self.subtotal, '.2f')
        return item

    class Meta:
        verbose_name = 'Detalle de Ingreso'
        verbose_name_plural = 'Detalle de Ingresos'
        ordering = ['id']


class Diario(models.Model):
    nro = models.CharField(max_length=20, verbose_name="Nro documento")
    ano = models.CharField(max_length=10, choices=ano_choices, default='2020', verbose_name='Año')
    mes = models.CharField(max_length=10, choices=mes_choices, default='NOVIEMBRE', verbose_name='Mes')
    date_joined = models.DateField(default=datetime.now)
    cuenta = models.ForeignKey(Plancontable, on_delete=models.CASCADE)
    desc = models.CharField(max_length=50)
    debe = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    haber = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    impuestos = models.CharField(max_length=3)

    def __str__(self):
        return self.desc

    def toJSON(self):
        item = model_to_dict(self)
        item['ano'] = {'id': self.ano, 'name': self.get_ano_display()}
        item['mes'] = {'id': self.mes, 'name': self.get_mes_display()}
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['cuenta'] = self.cuenta.toJSON()
        # item['desc'] = self.desc.toJSON()
        # item['debe'] = format(self.debe, '.2f')
        # item['haber'] = format(self.haber, '.2f')
        # item['impuestos'] = self.impuestos.toJSON()
        return item

    class Meta:
        verbose_name = 'Diario'
        verbose_name_plural = 'Diarios'
        ordering = ['id']


class Egreso(models.Model):
    nro = models.IntegerField()
    ano = models.CharField(max_length=10, choices=ano_choices, default='2020', verbose_name='Año')
    mes = models.CharField(max_length=10, choices=mes_choices, default='NOVIEMBRE', verbose_name='Mes')
    date_joined = models.DateField(default=datetime.now)
    cuenta = models.ForeignKey(Plancontable, on_delete=models.CASCADE)
    desc = models.CharField(max_length=50)
    debe = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    haber = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    impuestos = models.CharField(max_length=3)

    def __str__(self):
        return self.desc

    def toJSON(self):
        item = model_to_dict(self)
        item['ano'] = {'id': self.ano, 'name': self.get_ano_display()}
        item['mes'] = {'id': self.mes, 'name': self.get_mes_display()}
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['cuenta'] = self.cuenta.toJSON()
        # item['desc'] = self.desc.toJSON()
        # item['debe'] = format(self.debe, '.2f')
        # item['haber'] = format(self.haber, '.2f')
        # item['impuestos'] = self.impuestos.toJSON()
        return item

    class Meta:
        verbose_name = 'Egreso'
        verbose_name_plural = 'Egresos'
        ordering = ['id']


class Mayor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nombre diario')
    ano = models.CharField(max_length=10, choices=ano_choices, default='2020', verbose_name='Año')
    mes = models.CharField(max_length=10, choices=mes_choices, default='NOVIEMBRE', verbose_name='Mes')
    date_joined = models.DateField(default=datetime.now)
    # cuenta = models.ForeignKey(Plancontable, on_delete=models.CASCADE)
    desc = models.CharField(max_length=50, verbose_name='Descripción')
    deudor = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    acreedor = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.desc

    def toJSON(self):
        item = model_to_dict(self)
        item['name'] = self.name.toJSON()
        item['ano'] = {'id': self.ano, 'name': self.get_ano_display()}
        item['mes'] = {'id': self.mes, 'name': self.get_mes_display()}
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['cuenta'] = self.cuenta.toJSON()
        return item

    class Meta:
        verbose_name = 'Libro Mayor'
        verbose_name_plural = 'Libro Mayor'
        ordering = ['id']


class Endfinanciero(models.Model):
    # mes = models.CharField(max_length=10, choices=mes_choices, default='NOVIEMBRE', verbose_name='Mes')
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de registro' )
    ofinan = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Obligaciones Financieras')
    ventneta = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Ventas Netas')
    endfinan = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Endeudamiento Financiero')

    def __str__(self):
        return self.mes

    def toJSON(self):
        item = model_to_dict(self)
        item['ofinan'] = format(self.ofinan, '.2f')
        item['ventneta'] = format(self.ventneta, '.2f')
        item['endfinan'] = format(self.endfinan, '.2f')
        return item

    class Meta:
        verbose_name = 'Endeudamiento'
        verbose_name_plural = 'Endeudamientos'
        ordering = ['id']

class RentaActivo(models.Model):
    utineta = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Utilidad Neta')
    actitotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Activo Total')
    rentaactivo = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name="Rentabilida sobre Activo")
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de registro')

    def __str__(self):
        return self.utineta

    def toJSON(self):
        item = model_to_dict(self)
        item['utineta'] = format(self.utineta, '.2f')
        item['actitotal'] = format(self.actitotal, '.2f')
        item['rentaactivo'] = format(self.rentaactivol, '.2f')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        return item

    class Meta:
        verbose_name = 'RentaActivo'
        verbose_name_plural = 'RentaActivos'
        ordering = ['id']

class RentaPatrimonio(models.Model):
    utineta = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Utilidad Neta')
    patritotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Patrimonio Total')
    rentapatrimonio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de registro')

    def __str__(self):
        return self.utineta

    def toJSON(self):
        item = model_to_dict(self)
        item['utineta'] = format(self.utineta, '.2f')
        item['patritotal'] = format(self.patritotal, '.2f')
        item['rentaactivo'] = format(self.rentaactivo, '.2f')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')

    class Meta:
        verbose_name = 'RentaPatrimonio'
        verbose_name_plural = 'RentaPatrimonios'
        ordering = ['id']

def update_rentapatrimonio(sender, instance, **kwargs):
    instance.rentapatrimonio == (instance.utineta / instance.patritotal)*100
    instance.rentapatrimonio.save()
signals.post_save.connect(update_rentapatrimonio, sender=RentaPatrimonio, dispatch_uid="update_rentapatrimonio")