$(document).ready(function() {
    $('.add-to-cart').submit(function(event) {
        event.preventDefault();
        let form = $(this);
        let itemId = form.find('input[name="product_pk"]').val();
        let amount = form.find('input[name="amount"]').val();
        let csrftoken = form.find('input[name="csrfmiddlewaretoken"]').val();
        $.ajax({
            url: '',
            method: 'POST',
            data: {'product_pk': itemId, 'amount':amount, 'csrfmiddlewaretoken': csrftoken},
        });
    });
    $('.remove_one_to_cart').submit(function(event) {
        event.preventDefault();
        let form = $(this);
        let itemId = form.find('input[name="item"]').val();
        let amount = form.find('input[name="amount"]').val();
        let name = form.find('input[name="name"]').val();
        let csrftoken = form.find('input[name="csrfmiddlewaretoken"]').val();
        $.ajax({
            url: '/cart/',
            method: 'POST',
            data: {'item': itemId, 'amount':amount,'name': name , 'csrfmiddlewaretoken': csrftoken},
        });
    });
    $('.add_one_to_cart').submit(function(event) {
        event.preventDefault();
        let form = $(this);
        let itemId = form.find('input[name="item"]').val();
        let amount = form.find('input[name="amount"]').val();
        let name = form.find('input[name="name"]').val();
        let csrftoken = form.find('input[name="csrfmiddlewaretoken"]').val();
        $.ajax({
            url: '/cart/',
            method: 'POST',
            data: {'item': itemId, 'amount':amount,'name': name , 'csrfmiddlewaretoken': csrftoken},
        });
    });
    $('.delet_from_cart').submit(function(event) {
        event.preventDefault();
        let form = $(this);
        let itemId = form.find('input[name="item"]').val();
        let amount = form.find('input[name="amount"]').val();
        let name = form.find('input[name="name"]').val();
        let csrftoken = form.find('input[name="csrfmiddlewaretoken"]').val();
        $.ajax({
            url: '/cart/',
            method: 'POST',
            data: {'item': itemId, 'amount':amount,'name': name , 'csrfmiddlewaretoken': csrftoken},
        });
    });
});