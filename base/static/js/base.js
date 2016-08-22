$('#couponModal').on('show.bs.modal', function (event) {
    var anchor = $(event.relatedTarget);
    var urlcode = anchor.data('urlcode');
    var modal = $(this);
    var content = modal.find('#couponModalContent')

    $.ajax({
        url: '/process/' + urlcode,
        dataType: 'html',
        success: function(data) {
            content.replaceWith(data)
        }
    });

    $('#couponModal').on('hidden.bs.modal', function (event) {
        modal.find('#couponModalContent').empty();
    });
});
$("#buttonSearch").click(function() {
    $("#buttonSearch .fa-search, #buttonSearch .fa-close").toggleClass("fa-search fa-close");
    $("#formSearch").toggleClass("visible-sm-down hidden-sm-down")
});
