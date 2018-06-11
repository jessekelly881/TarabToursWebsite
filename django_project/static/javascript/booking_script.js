var name
var email, emails_match
var phone, phones_match

var payment_method = 'credit'
var tour;
var agreed = false;
var num_people = 1;
var total_cost = 0

$(document).ready(function(){

  function updateSubmitBtn() {
    if (agreed && tour && emails_match) {$("#submit_btn").removeClass("disabled")}
    else{$("#submit_btn").addClass("disabled")}
  }

  function checkEmail() {
    emails_match = ($("#id_email").val() == $("#id_confirm_email").val())
    if(emails_match){
      $(".emails_dont_match").hide()
      $("#confirm_email").hide()
    }
    else{
      $(".emails_dont_match").show()
      $("#confirm_email").show()
    }
  }

  function checkPhoneNumber() {
    phones_match = ($("#id_phone").val() == $("#id_confirm_phone").val())
    if(phones_match){
      $(".phone_numbers_dont_match").hide()
      $("#confirm_phone").hide()
    }
    else{
      $(".phone_numbers_dont_match").show()
      $("#confirm_phone").show()
    }
  }

  //Check Input Text
  $("#id_name").on('input',function () {
    name = $(this).val()
    $("#please_name").hide()
  })

  $("#id_email, #id_confirm_email").on('input',function () {
    email = $(this).val()
    $("#please_email").hide()
    checkEmail()
    updateSubmitBtn()
  })
  $("#id_phone,#id_confirm_phone").on('input',function () {
    phone = $(this).val()
    $("#please_phone").hide()
    checkPhoneNumber()
    updateSubmitBtn()
  })

  //Agree Button
  $("#agree_btn").click(function () {
    if(this.checked){
      $("#terms_text").hide(500)
      $("#agree_btn_label").text("Agreed")
      $("#please_agree").hide()
      agreed = true
      updateSubmitBtn()
    }
    else {
      $("#terms_text").show(500)
      $("#agree_btn_label").text("I Agree")
      $("#please_agree").show()
      agreed = false
      updateSubmitBtn()
    }
  })

  function updateCost() {
    if(tour){
      total_cost = (parseFloat(tour.attr("tour_cost")) * num_people).toFixed(2)
      $("#total_cost").text(`Total Cost: $${total_cost}`)
    }
    else {
      total_cost = 0
      $("#total_cost").text("")
    }
  }

  $(".tour_select_btn").click(function () {
    var block = $(this).parent().parent().parent()
    $("blockquote").not(block).hide()
    $(this).hide() //hide Button
    $(".change_tour_btn").show()
    $("#please_select_tour").hide()
    $("#select_tour_label").hide(); $("#tour_selected_label").show() //Toggle label
    tour = block
    updateSubmitBtn()
    updateCost()
  })

  $(".change_tour_btn").click(function () {
    $("blockquote").show()
    $(".tour_select_btn").show() //Show all buttons
    $(".change_tour_btn").hide()
    $("#please_select_tour").show()
    $("#select_tour_label").show(); $("#tour_selected_label").hide() //Toggle label
    tour = undefined
    updateSubmitBtn()
    updateCost()
  })

  $(".payment_radio_btn").click(function () {
    payment_method = $(this).attr("payment_code")
  })

  //On submit
  $("#submit_btn").click(function () {

    var handler = StripeCheckout.configure({
      //Test key: pk_test_jV8nSSQ2M0FkjIhxHHUBFDPh
      //Live key: pk_live_dS8Z6RKPDNvCEoS0Me9lgFij
      key: 'pk_test_jV8nSSQ2M0FkjIhxHHUBFDPh',
      image: 'https://stripe.com/img/documentation/checkout/marketplace.png',
      locale: 'auto',
    });

    if (payment_method == 'credit') {
      handler.open({
        name: tour.attr("tour_name"),
        description: tour.attr("tour_date") + " " + tour.attr("tour_time"),
        amount: total_cost.toString().replace(".",""),
        //currency: "gbp"
        email: email
      });

      $("#booking_form").submit()
    }
    /* //Not functional
    if (payment_method == 'paypal') {
        $('#paypal_form').submit()
    }
    */

  $("#num_people_selector").change(function () {
    num_people = parseInt($(this).find(":selected").val())
    updateCost()
  })

})

});
