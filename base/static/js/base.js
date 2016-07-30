$('#couponModal').on('show.bs.modal', function (event) {
    var anchor = $(event.relatedTarget);
    var title = anchor.data('title');
    var couptitle = anchor.data('couptitle');
    var expdate = anchor.data('expdate');
    var bizname = anchor.data('bizname');
    var bizaddress = anchor.data('bizaddress');
    var bizphone = anchor.data('bizphone');
    var bizlogo = anchor.data('bizlogo');
    var urlcode = anchor.data('urlcode');
    var url = anchor.data('url');
    var modal = $(this);

    modal.find('.coupon-title').text(title);
    modal.find('.coupon-couptitle').append(couptitle);
    modal.find('.coupon-bizname').text('About ' + bizname);
    modal.find('.coupon-urlcode').val(url)
    modal.find('.coupon-bizphone').text('Phone: ' + bizphone);
    
    if (expdate && expdate != 'None' && $('.coupon-exp-date').length == 0) {
        modal.find('.coupon-body').append("<span class='coupon-exp-date'>Expires: " + expdate + "</span>");
    }
    
    if (bizlogo && $('.media-image').length == 0) {
        modal.find('.media').prepend(" <div class='media-image media-left media-top'> <img class='media-img' src='/img/" + bizlogo + "' alt='image'> </div> ");
    }

    if (bizaddress && $('').length == 0) {
        modal.find('.coupon-bizaddress').text('Address: ' + bizaddress);
        $.ajax({
            url: 'map?url_code=' + urlcode,
            dataType: 'html',
            success: function(data) {
                $( ".map-container" ).append("<div id='map'></div>");
                $( "#map" ).append(data);
            }
        });
    }
})

$('#couponModal').on('hidden.bs.modal', function (event) {
    $('.coupon-couptitle').find('p').remove();
    $('.media-image').remove();
    $('.coupon-exp-date').remove();
    $('#map').remove();
    $('.coupon-bizaddress').empty();
});
