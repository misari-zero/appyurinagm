// var compro = {
//     items: {
//         comprobante: '',
//         numero: '',
//         fecha: '',
//         cli: '',
//         subtotal: 0.00,
//         iva: 0.00,
//         total: 0.00,
//         plancontable: []
//     },
//     add: function (item) {
//         this.items.plancontable.push(item);
//         this.list();
//     },
//     list: function () {
//         $('#tblPlancontable').DataTable({
//             responsive: true,
//             autoWidth: false,
//             destroy: true,
//             data: this.items.plancontable,
//             columns: [
//                 {"data": "id"},
//                 {"data": "cod"},
//                 {"data": "name"},
//                 {"data": "tipo.name"},
//                 // {"data": "cuenta.name"},
//                 {"data": "debe"},
//                 {"data": "haber"},
//             ],
//             columnDefs: [
//                 {
//                     targets: [0],
//                     class: 'text-center',
//                     orderable: false,
//                     render: function (data, type, row) {
//                         return '<a rel="remove" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
//                     }
//                 },
//                 {
//                     targets: [-3],
//                     class: 'text-center',
//                     orderable: false,
//                     render: function (data, type, row) {
//                         return 'S/.' + parseFloat(data).toFixed(2);
//                     }
//                 },
//                 {
//                     targets: [-2],
//                     class: 'text-center',
//                     orderable: false,
//                     render: function (data, type, row) {
//                         return '<input type="text" name="cant" class="form-control form-control-sm" autocomplete="off" value="' + row.debe+ '">';
//                     }
//                 },
//                 {
//                     targets: [-1],
//                     class: 'text-center',
//                     orderable: false,
//                     render: function (data, type, row) {
//                         return 'S/.' + parseFloat(data).toFixed(2);
//                     }
//                 },
//             ],
//             initComplete: function (settings, json) {
//
//             }
//         });
//     },
// };
//
// $(function () {
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
//     //     step: 0.1,
//     //     decimals: 2,
//     //     boostat: 5,
//     //     maxboostedstep: 10,
//     //     postfix: '%'
//     // });
//
//
//     // search plancontable
//     $('input[name="search"]').autocomplete({
//         source: function (request, response) {
//             $.ajax({
//                 url: window.location.pathname,
//                 type: 'POST',
//                 data: {
//                     'action': 'search_contable',
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
//             console.log(compro.items);
//             compro.add(ui.item);
//             $(this).val('');
//         }
//     });
// });
