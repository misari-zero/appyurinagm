// var tblProducts;
// var vents = {
//     items: {
//         nro: '',
//         date_joined: '',
//         ano: '',
//         mes: '',
//         impuestos: '',
//         debe: 0.00,
//         haber: 0.00,
//         products: []
//     },
//     calculate_invoice: function () {
//         var debe = 0.00;
//         var haber = 0.00;
//         // var iva = $('input[name="iva"]').val();
//         $.each(this.items.products, function (pos, dict) {
//             dict.pos = pos;
//             dic.debe = dict.debe;
//             dic.haber = dict.haber;
//             // dict.debe = dict.cant * parseFloat(dict.pvp);
//             debe += dict.debe;
//             haber += dict.haber;
//         });
//
//         this.items.debe = debe;
//         this.items.haber = haber;
//         // this.items.iva = this.items.subtotal * iva;
//         // this.items.total = this.items.subtotal + this.items.iva;
//
//         $('input[name="debe"]').val(this.items.debe.toFixed(2));
//         $('input[name="haber"]').val(this.items.haber.toFixed(2));
//         // $('input[name="total"]').val(this.items.total.toFixed(2));
//     },
//     add: function (item) {
//         this.items.products.push(item);
//         this.list();
//     },
//     list: function () {
//         this.calculate_invoice();
//         tblProducts = $('#tblProducts').DataTable({
//             responsive: true,
//             autoWidth: false,
//             destroy: true,
//             data: this.items.products,
//             columns: [
//                 {"data": "id"},
//                 {"data": "name"},
//                 {"data": "tipo.name"},
//                 {"data": "debe"},
//                 {"data": "haber"},
//             ],
//             columnDefs: [
//                 {
//                     targets: [0],
//                     class: 'text-center',
//                     orderable: false,
//                     render: function (data, type, row) {
//                         return '<a rel="remove" class="btn btn-danger btn-xs btn-flat" style="color: #ffffff;"><i class="fas fa-trash-alt"></i></a>';
//                     }
//                 },
//                 {
//                     targets: [-1, -2],
//                     class: 'text-center',
//                     orderable: false,
//                     render: function (data, type, row) {
//                         return '<input type="text" name="haber" class="form-control form-control-sm input-sm" autocomplete="off">';
//                     }
//                 }
//             ],
//             // rowCallback(row, data, displayNum, displayIndex, dataIndex) {
//             //
//             //     $(row).find('input[name="cant"]').TouchSpin({
//             //         min: 1,
//             //         max: 1000000000,
//             //         step: 1
//             //     });
//             //
//             // },
//             initComplete: function (settings, json) {
//
//             }
//         });
//         console.clear();
//         console.log(this.items);
//     },
// };
//
// function formatRepo(repo) {
//     if (repo.loading) {
//         return repo.text;
//     }
//
//     var option = $(
//         '<div class="wrapper container">' +
//         '<div class="row">' +
//         '<div class="col-lg-12 text-left shadow-sm">' +
//         //'<br>' +
//         '<p style="margin-bottom: 0;">' +
//         // '<b>Cuenta::</b> ' + repo.cta5 + '<br>' +
//         '<b>Cuenta:</b> ' + repo.name + '<br>' +
//         '<b>Tipo:</b> ' + repo.tipo.name + '<br>' +
//         '</p>' +
//         '</div>' +
//         '</div>' +
//         '</div>');
//
//     return option;
// }
//
// $(function () {
//
//     $('.select2').select2({
//         theme: "bootstrap4",
//         language: 'es'
//     });
//
//     $('#date_joined').datetimepicker({
//         format: 'YYYY-MM-DD',
//         date: moment().format("YYYY-MM-DD"),
//         locale: 'es',
//         //minDate: moment().format("YYYY-MM-DD")
//     });
//
//     // $("input[name='iva']").TouchSpin({
//     //     min: 0,
//     //     max: 100,
//     //     step: 0.01,
//     //     decimals: 2,
//     //     boostat: 5,
//     //     maxboostedstep: 10,
//     //     postfix: '%'
//     // }).on('change', function () {
//     //     vents.calculate_invoice();
//     // })
//     //     .val(0.18);
//
//     //search products
//     $('input[name="search"]').autocomplete({
//         source: function (request, response) {
//             $.ajax({
//                 url: window.location.pathname,
//                 type: 'POST',
//                 data: {
//                     'action': 'search_products',
//                     'term': request.term
//                 },
//                 dataType: 'json',
//             }).done(function (data) {
//                 response(data);
//             }).fail(function (jqXHR, textStatus, errorThrown) {
//                 //alert(textStatus + ': ' + errorThrown);
//             }).always(function (data) {
//
//             });
//         },
//         delay: 500,
//         minLength: 1,
//         select: function (event, ui) {
//             event.preventDefault();
//             console.clear();
//             ui.item.debe = 0.00;
//             ui.item.haber = 0.00;
//             console.log(vents.items);
//             vents.add(ui.item);
//             $(this).val('');
//         }
//     });
//
//     $('.btnRemoveAll').on('click', function () {
//         if (vents.items.products.length === 0) return false;
//         alert_action('Notificación', '¿Estas seguro de eliminar todos los items de tu detalle?', function () {
//             vents.items.products = [];
//             vents.list();
//         }, function () {
//             location.href = '/erp/diario/list/';
//         });
//     });
//
//     // event cant
//     $('#tblProducts tbody')
//         .on('click', 'a[rel="remove"]', function () {
//             var tr = tblProducts.cell($(this).closest('td, li')).index();
//             alert_action('Notificación', '¿Estas seguro de eliminar el producto de tu detalle?',
//                 function () {
//                     vents.items.products.splice(tr.row, 1);
//                     vents.list();
//                 }, function () {
//
//                 });
//         })
//     // .on('change', 'input[name="debe"]', function () {
//     //     console.clear();
//     //     var debe = 0.00;
//     //     var tr = tblProducts.cell($(this).closest('td, li')).index();
//     //     vents.items.plan[tr.row].debe = debe;
//     //     vents.calculate_invoice();
//     //     $('td:eq(4)', tblProducts.row(tr.row).node()).html('S/.' + vents.items.plan[tr.row].debe.toFixed(2));
//     //     var haber = 0.00;
//     //     var tr = tblProducts.cell($(this).closest('td, li')).index();
//     //     vents.items.plan[tr.row].haber = haber;
//     //     vents.calculate_invoice();
//     //     $('td:eq(5)', tblProducts.row(tr.row).node()).html('S/.' + vents.items.plan[tr.row].haber.toFixed(2));
//     // });
//
//     $('.btnClearSearch').on('click', function () {
//         $('input[name="search"]').val('').focus();
//     });
//
//     // event submit
//     $('form').on('submit', function (e) {
//         e.preventDefault();
//
//         if (vents.items.products.length === 0) {
//             message_error('Debe al menos tener un item en su detalle');
//             return false;
//         }
//         vents.items.nro = $('input[name="nro"]').val();
//         vents.items.ano = $('input[name="ano"]').val();
//         vents.items.mes = $('input[name="mes"]').val();
//         vents.items.date_joined = $('input[name="date_joined"]').val();
//         vents.items.desc = $('input[name="desc"]').val();
//         vents.items.impuestos = $('input[name="impuestos"]').val();
//         var parameters = new FormData();
//         parameters.append('action', $('input[name="action"]').val());
//         parameters.append('vents', JSON.stringify(vents.items));
//         submit_with_ajax(window.location.pathname, 'Notificación',
//             '¿Estas seguro de realizar la siguiente acción?', parameters, function (response) {
//                 alert_action('Notificación', '¿Desea imprimir el listado?', function () {
//                     window.open('/erp/diario/invoice/pdf/' + response.id + '/', '_blank');
//                     location.href = '/erp/diario/list/';
//                 }, function () {
//                     location.href = '/erp/diario/list/';
//                 });
//             });
//     });
//
//     // vents.list()
//     $('select[name="search"]').select2({
//         theme: "bootstrap4",
//         language: 'es',
//         allowClear: true,
//         ajax: {
//             delay: 250,
//             type: 'POST',
//             url: window.location.pathname,
//             data: function (params) {
//                 var queryParameters = {
//                     term: params.term,
//                     action: 'search_products'
//                 }
//                 return queryParameters;
//             },
//             processResults: function (data) {
//                 return {
//                     results: data
//                 };
//             },
//         },
//         placeholder: 'Ingrese una descripción',
//         minimumInputLength: 1,
//         templateResult: formatRepo,
//     }).on('select2:select', function (e) {
//         var data = e.params.data;
//         data.debe = 0.00;
//         data.haber = 0.00;
//         vents.add(data);
//         $(this).val('').trigger('change.select2');
//     });
//
//     // Esto se puso aqui para que funcione bien el editar y calcule bien los valores del iva. // sino tomaría el valor del iva de la base debe
//     // coger el que pusimos al inicializarlo.
//     vents.list();
// });