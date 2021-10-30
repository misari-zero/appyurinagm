$(function () {
    $('#data').DataTable( {
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "id"},
            {"data": "nro"},
            // {"data": "ano"},
            // {"data": "mes"},
            {"data": "date_joined"},
            {"data": "cuenta.name"},
            {"data": "desc"},
            // {"data": "impuestos"},
            {"data": "debe"},
            {"data": "haber"},
            {"data": "id"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: "text-center",
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="/erp/diario/update/' + row.id + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a>';
                    buttons += '<a href="/erp/diario/delete/' + row.id + '/" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
            // {
            //     targets: [-2, -3],
            //     class: 'text-center',
            //     orderable: false,
            //     render: function (data, type, row) {
            //         return 'S/.'+parseFloat(data).toFixed(2);
            //     }
            // },
        ],
        initComplete: function (settings, json) {
        }
    });
});



// var tblSale;
//
// function format(d) {
//     console.log(d);
//     var html = '<table class="table">';
//     html += '<thead class="thead-dark">';
//     html += '<tr><th scope="col">Codigo</th>';
//     html += '<th scope="col">Cuenta</th>';
//     html += '<th scope="col">Debe</th>';
//     html += '<th scope="col">Haber</th></tr>';
//     html += '</thead>';
//     html += '<tbody>';
//     $.each(d.det, function (key, value) {
//         html+='<tr>'
//         html+='<td>'+value.cuenta.cta.name+'</td>'
//         html+='<td>'+value.cuenta.name+'</td>'
//         html+='<td>'+value.debe+'</td>'
//         html+='<td>'+value.haber+'</td>'
//         html+='</tr>';
//     });
//     html += '</tbody>';
//     return html;
// }
//
// $(function () {
//
//     tblSale = $('#data').DataTable({
//         //responsive: true,
//         scrollX: true,
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
//             {
//                 "className": 'details-control',
//                 "orderable": false,
//                 "data": null,
//                 "defaultContent": ''
//             },
//             {"data": "nro"},
//             {"data": "ano.name"},
//             {"data": "mes.name"},
//             {"data": "date_joined"},
//             {"data": "desc"},
//             {"data": "debe"},
//             {"data": "haber"},
//             {"data": "impuestos"},
//             {"data": "id"},
//         ],
//         columnDefs: [
//             {
//                 targets: [-3, -4],
//                 class: 'text-center',
//                 orderable: false,
//                 render: function (data, type, row) {
//                     return 'S/.' + parseFloat(data).toFixed(2);
//                 }
//             },
//             {
//                 targets: [-1],
//                 class: 'text-center',
//                 orderable: false,
//                 render: function (data, type, row) {
//                     var buttons = '<a href="/erp/sale/delete/' + row.id + '/" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a> ';
//                     buttons += '<a href="/erp/sale/update/' + row.id + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
//                     buttons += '<a rel="details" class="btn btn-success btn-xs btn-flat"><i class="fas fa-search"></i></a> ';
//                     buttons += '<a href="/erp/sale/invoice/pdf/'+row.id+'/" target="_blank" class="btn btn-info btn-xs btn-flat"><i class="fas fa-file-pdf"></i></a> ';
//                     return buttons;
//                 }
//             },
//         ],
//         initComplete: function (settings, json) {
//
//         }
//     });
//
//     $('#data tbody')
//         .on('click', 'a[rel="details"]', function () {
//             var tr = tblSale.cell($(this).closest('td, li')).index();
//             var data = tblSale.row(tr.row).data();
//             console.log(data);
//
//             $('#tblDet').DataTable({
//                 responsive: true,
//                 autoWidth: false,
//                 destroy: true,
//                 deferRender: true,
//                 //data: data.det,
//                 ajax: {
//                     url: window.location.pathname,
//                     type: 'POST',
//                     data: {
//                         'action': 'search_details_prod',
//                         'id': data.id
//                     },
//                     dataSrc: ""
//                 },
//                 columns: [
//                     {"data": "cuenta.cta.name"},
//                     {"data": "cuenta.name"},
//                     {"data": "debe"},
//                     {"data": "haber"},
//                 ],
//                 columnDefs: [
//                     {
//                         targets: [-1, -2],
//                         class: 'text-center',
//                         render: function (data, type, row) {
//                             return 'S/.' + parseFloat(data).toFixed(2);
//                         }
//                     },
//                 ],
//                 initComplete: function (settings, json) {
//
//                 }
//             });
//
//             $('#myModelDet').modal('show');
//         })
//         .on('click', 'td.details-control', function () {
//             var tr = $(this).closest('tr');
//             var row = tblSale.row(tr);
//             if (row.child.isShown()) {
//                 row.child.hide();
//                 tr.removeClass('shown');
//             } else {
//                 row.child(format(row.data())).show();
//                 tr.addClass('shown');
//             }
//         });
//
// });