var tblProjects;
var ingre = {
    items: {
        cli: '',
        date_joined: '',
        date_venc: '',
        subtotal: 0.00,
        igv: 0.00,
        total: 0.00,
        projects: []
    },
    calculate_invoice: function () {
        var subtotal = 0.00;
        var igv = $('input[name="igv"]').val();
        $.each(this.items.projects, function (pos, dict) {
            dict.pos = pos;
            dict.subtotal = dict.cant * parseFloat(dict.pre);
            subtotal += dict.subtotal;
        });
        this.items.subtotal = subtotal;
        this.items.igv = this.items.subtotal * igv;
        this.items.total = this.items.subtotal + this.items.igv;

        $('input[name="subtotal"]').val(this.items.subtotal.toFixed(2));
        $('input[name="igvcalc"]').val(this.items.igv.toFixed(2));
        $('input[name="total"]').val(this.items.total.toFixed(2));
    },
    add: function (item) {
        this.items.projects.push(item);
        this.list();
    },
    list: function () {
        this.calculate_invoice();
        tblProjects = $('#tblProjects').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            data: this.items.projects,
            columns: [
                {"data": "id"},
                {"data": "name"},
                // {"data": "cate.name"},
                {"data": "pre"},
                {"data": "cant"},
                {"data": "subtotal"},
            ],
            columnDefs: [
                {
                    targets: [0],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<a rel="remove" class="btn btn-danger btn-xs btn-flat" style="color: white;"><i class="fas fa-trash-alt"></i></a>';
                    }
                },
                {
                    targets: [-3],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return 'S/.' + parseFloat(data).toFixed(2);
                    }
                },
                {
                    targets: [-2],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cant" class="form-control form-control-sm input-sm" autocomplete="off" value="' + row.cant + '">';
                    }
                },
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return 'S/.' + parseFloat(data).toFixed(2);
                    }
                },
            ],
            rowCallback(row, data, displayNum, displayIndex, dataIndex) {

                $(row).find('input[name="cant"]').TouchSpin({
                    min: 1,
                    max: 1000000000,
                    step: 1
                });

            },
            initComplete: function (settings, json) {

            }
        });
        console.clear();
        console.log(this.items);
    },
};

function formatRepo(repo) {
    if (repo.loading) {
        return repo.text;
    }

    var option = $(
        '<div class="wrapper container">' +
        '<div class="row">' +
        // '<div class="col-lg-1">' +
        // '<img src="' + repo.image + '" class="img-fluid img-thumbnail d-block mx-auto rounded">' +
        // '</div>' +
        '<div class="col-lg-11 text-left shadow-sm">' +
        //'<br>' +
        '<p style="margin-bottom: 0;">' +
        '<b>Nombre:</b> ' + repo.name + '<br>' +
        // '<b>Categor??a:</b> ' + repo.cate.name + '<br>' +
        '<b>Precio:</b> <span class="badge badge-warning">S/.' + repo.pre + '</span>' +
        '</p>' +
        '</div>' +
        '</div>' +
        '</div>');
    return option;
}

$(function () {

    $('.select2').select2({
        theme: "bootstrap4",
        language: 'es'
    });

    $('#date_joined').datetimepicker({
        format: 'YYYY-MM-DD',
        date: moment().format("YYYY-MM-DD"),
        locale: 'es',
        //minDate: moment().format("YYYY-MM-DD")
    });

    $('#date_venc').datetimepicker({
        format: 'YYYY-MM-DD',
        date: moment().format("YYYY-MM-DD"),
        locale: 'es',
        //minDate: moment().format("YYYY-MM-DD")
    });

    $("input[name='igv']").TouchSpin({
        min: 0,
        max: 100,
        step: 0.01,
        decimals: 2,
        boostat: 5,
        maxboostedstep: 10,
        postfix: '%'
    }).on('change', function () {
        ingre.calculate_invoice();
    })
        .val(0.18);

    //search products
    // $('input[name="search"]').autocomplete({
    //     source: function (request, response) {
    //         $.ajax({
    //             url: window.location.pathname,
    //             type: 'POST',
    //             data: {
    //                 'action': 'search_projects',
    //                 'term': request.term
    //             },
    //             dataType: 'json',
    //         }).done(function (data) {
    //             response(data);
    //         }).fail(function (jqXHR, textStatus, errorThrown) {
    //             //alert(textStatus + ': ' + errorThrown);
    //         }).always(function (data) {
    //
    //         });
    //     },
    //     delay: 500,
    //     minLength: 1,
    //     select: function (event, ui) {
    //         event.preventDefault();
    //         console.clear();
    //         ui.item.cant = 1;
    //         ui.item.subtotal = 0.00;
    //         console.log(vents.items);
    //         vents.add(ui.item);
    //         $(this).val('');
    //     }
    // });

    $('.btnRemoveAll').on('click', function () {
        if (ingre.items.projects.length === 0) return false;
        alert_action('Notificaci??n', '??Estas seguro de eliminar todos los items de tu detalle?', function () {
            ingre.items.projects = [];
            ingre.list();
        }, function () {
            location.href = '/erp/ingreso/list/';
        });
    });

    // event cant
    $('#tblProjects tbody')
        .on('click', 'a[rel="remove"]', function () {
            var tr = tblProjects.cell($(this).closest('td, li')).index();
            alert_action('Notificaci??n', '??Estas seguro de eliminar el producto de tu detalle?',
                function () {
                    ingre.items.projects.splice(tr.row, 1);
                    ingre.list();
                }, function () {

                });
        })
        .on('change', 'input[name="cant"]', function () {
            console.clear();
            var cant = parseInt($(this).val());
            var tr = tblProjects.cell($(this).closest('td, li')).index();
            ingre.items.projects[tr.row].cant = cant;
            ingre.calculate_invoice();
            $('td:eq(5)', tblProjects.row(tr.row).node()).html('S/.' + ingre.items.projects[tr.row].subtotal.toFixed(2));
        });

    $('.btnClearSearch').on('click', function () {
        $('input[name="search"]').val('').focus();
    });

    // event submit
    $('form').on('submit', function (e) {
        e.preventDefault();

        if (ingre.items.projects.length === 0) {
            message_error('Debe al menos tener un item en su detalle de venta');
            return false;
        }

        ingre.items.doc = $('input[name="doc"]').val();
        ingre.items.date_joined = $('input[name="date_joined"]').val();
        ingre.items.date_venc = $('input[name="date_venc"]').val();
        ingre.items.cli = $('select[name="cli"]').val();
        var parameters = new FormData();
        parameters.append('action', $('input[name="action"]').val());
        parameters.append('ingre', JSON.stringify(ingre.items));
        submit_with_ajax(window.location.pathname, 'Notificaci??n',
            '??Estas seguro de realizar la siguiente acci??n?', parameters, function (response) {
                alert_action('Notificaci??n', '??Desea imprimir la boleta de venta?', function () {
                    window.open('/erp/ingreso/invoice/pdf/' + response.id + '/', '_blank');
                    location.href = '/erp/ingreso/list/';
                }, function () {
                    location.href = '/erp/ingreso/list/';
                });
            });
    });

    // ingre.list()
    $('select[name="search"]').select2({
        theme: "bootstrap4",
        language: 'es',
        allowClear: true,
        ajax: {
            delay: 250,
            type: 'POST',
            url: window.location.pathname,
            data: function (params) {
                var queryParameters = {
                    term: params.term,
                    action: 'search_projects'
                }
                return queryParameters;
            },
            processResults: function (data) {
                return {
                    results: data
                };
            },
        },
        placeholder: 'Ingrese una descripci??n',
        minimumInputLength: 1,
        templateResult: formatRepo,
    }).on('select2:select', function (e) {
        var data = e.params.data;
        data.cant = 1;
        data.subtotal = 0.00;
        ingre.add(data);
        $(this).val('').trigger('change.select2');
    });

    // Esto se puso aqui para que funcione bien el editar y calcule bien los valores del igv. // sino tomar??a el valor del igv de la base debe
    // coger el que pusimos al inicializarlo.
    ingre.list();
});
