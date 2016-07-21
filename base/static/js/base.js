$('#couponModal').on('show.bs.modal', function (event) {
    var anchor = $(event.relatedTarget) // Button that triggered the modal
    var title = anchor.data('title')
    var bizname = anchor.data('bizname')
    var modal = $(this)
    modal.find('.coupon-title').text(title)
    modal.find('.coupon-bizname').text(bizname)
})
