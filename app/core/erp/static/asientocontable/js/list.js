// $(function () {
//     $('#data').DataTable( {
//         responsive: true,
//         autoWidth: false,
//         destroy: true,
//         deferRender: true,
//         ajax: {
//             url: window.location.pathname,
//             type: 'POST',
//             data: {
//                 'action': 'searchdata'
//             },
//             dataSrc: ""
//         },
//         columns: [
//             {"data": "id"},
//             {"data": "as_con"},
//             {"data": "fecha"},
//             {"data": "ano"},
//             {"data": "mes"},
//             {"data": "mes"},
//             {"data": "glosa"},
//             {"data": "cuenta"},
//             {"data": "detalle"},
//             {"data": "debe"},
//             {"data": "haber"},
//             {"data": "subtotal1"},
//             {"data": "subtotal2"},
//             {"data": "subtotal2"},
//         ],
//         columnDefs: [
//             {
//                 targets: [-1],
//                 class: "text-center",
//                 orderable: false,
//                 render: function (data, type, row) {
//                     var buttons = '<a href="/erp/asientocontable/update/' + row.id + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a>';
//                     buttons += '<a href="/erp/asientocontable/delete/' + row.id + '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
//                     return buttons;
//                 }
//             },
//         ],
//         initComplete: function (settings, json) {
//         }
//     });
// });