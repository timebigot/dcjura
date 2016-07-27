$('#couponModal').on('show.bs.modal', function (event) {
    var anchor = $(event.relatedTarget);
    var title = anchor.data('title');
    var bizname = anchor.data('bizname');
    var bizaddress = anchor.data('bizaddress');
    var bizphone = anchor.data('bizphone');
    var urlcode = anchor.data('urlcode');
    var modal = $(this);

    modal.find('.coupon-title').text(title);
    modal.find('.coupon-bizname').text(bizname);
    modal.find('.coupon-urlcode').val('http://dcjura.com/c/' + urlcode)
    modal.find('.coupon-bizaddress').text('Address: ' + bizaddress);
    modal.find('.coupon-bizphone').text('Phone: ' + bizphone);
    $.ajax({
        url: 'map?url_code=' + urlcode,
        dataType: 'html',
        success: function(data) {
            $( "#map" ).append(data);
        }
    });
})
