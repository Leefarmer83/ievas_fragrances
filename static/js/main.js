$(document).ready(function () {
    $('.toast').toast('show');
    // Deals with the AJAX to shows modal template
    $(".js-subscribe-modal").click(function () {
        $.ajax({
            url: '/newsletter/add_subscriber/',
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#base-modal").modal("show");
            },
            success: function (data) {
                $("#base-modal .modal-dialog").html(data.html_modal);
            }
        });
    });
    // Deals with the form submission for adding region with AJAX
    $("#base-modal").on("submit", ".js-add-subscriber-form", function () {
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                   // $("#base-modal").modal("hide");
                   $("#base-modal .modal-dialog").html(data.html_success);
                } else {
                    $("#base-modal .modal-dialog").html(data.html_modal);
                }
            }
        });
        return false;
    });

    $(".js-add-review").click(function () {
        var button = $(this);
        $.ajax({
            url: button.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#base-modal").modal("show");
            },
            success: function (data) {
                $("#base-modal .modal-dialog").html(data.html_modal);
            }
        });
    });
    // Deals with the form submission for adding region with AJAX
    $("#base-modal").on("submit", ".js-add-review-form", function () {
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.form_is_valid) {
                   // $("#base-modal").modal("hide");
                   $("#base-modal .modal-dialog").html(data.html_success);
                   $("#nav-reviews").html(data.html_review);
                } else {
                    $("#base-modal .modal-dialog").html(data.html_modal);
                }
            }
        });
        return false;
    });
});