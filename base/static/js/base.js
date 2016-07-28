$('#couponModal').on('show.bs.modal', function (event) {
    var anchor = $(event.relatedTarget);
    var title = anchor.data('title');
    var bizname = anchor.data('bizname');
    var bizaddress = anchor.data('bizaddress');
    var bizphone = anchor.data('bizphone');
    var bizlogo = anchor.data('bizlogo');
    var urlcode = anchor.data('urlcode');
    var url = anchor.data('url');
    var modal = $(this);

    modal.find('.coupon-title').text(title);
    modal.find('.coupon-bizname').text('About ' + bizname);
    modal.find('.coupon-urlcode').val(url)
    modal.find('.coupon-bizaddress').text('Address: ' + bizaddress);
    modal.find('.coupon-bizphone').text('Phone: ' + bizphone);
    
    if (bizlogo && $('.media-image').length == 0) {
        modal.find('.media').prepend(" <div class='media-image media-left media-middle'> <img class='media-img' src='/img/" + bizlogo + "' alt='image'> </div> ");
    }

    $.ajax({
        url: 'map?url_code=' + urlcode,
        dataType: 'html',
        success: function(data) {
            $( "#map" ).append(data);
        }
    });
})

$('#couponModal').on('hidden.bs.modal', function (event) {
    $('.media-image').remove();
});
