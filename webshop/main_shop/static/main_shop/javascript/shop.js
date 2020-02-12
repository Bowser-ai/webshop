const $ = jQuery;
const CART_BUTTON_SELECTOR = '[data-role="add-to-cart"]';
const $add_to_cart_button = $(CART_BUTTON_SELECTOR);
const DATA_PRODUCT_SELECTOR = 'data-product-id';
const CART_SELECTOR = '[data-role="cart"]';
const URL = '/shop/ajax/';

$add_to_cart_button.click(event =>{
  const $this_button = $(event.target);
  const product_id = $this_button.attr(DATA_PRODUCT_SELECTOR);
  const csrf = document.cookie;
  const csrf_token_cookie = csrf.substring('csrftoken='.length);

  $.ajaxSetup({
    headers : { 'X-CSRFToken' : csrf_token_cookie }
  });

  $.ajax({
    url : URL,
    type : 'POST',
    data : {
      product_id
    },
    success : data => {
      const $success = $('<h4>',{
        class : 'item-added-success text-center',
        style : 'color : green;display : none',
        text : 'Item has been added to the cart',
      });

      setTimeout(() => {
        $success.toggle('fast', () => {
          $success.empty();
        });
      },800);

      $this_button.after($success);
      $success.toggle('fast');

      const $cart = $(CART_SELECTOR);
      const amount = data.amount;
      $cart.text(`Cart(${amount})`);
    }
  });
});
