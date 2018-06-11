from twilio.rest import Client
import stripe
from models import Person

twilio_account_sid = "ACb489d01e6ef6c2deede2b02013a68249"
twilio_auth_token = "d4d48170b26549b9dee9d54868d317a1"
twilio_client = Client(twilio_account_sid, twilio_auth_token)

twilio_from_number = "+16147217379"
twilio_to_number = "+5215549036350"


def sendBookingNotification(form_data):
    sms_body = 'New Booking!\n' + 'Name: ' + form_data['name'] + '\nPhone Number: ' + form_data['phone'] + '\nEmail Address: ' + form_data['email']+ '\nPayment Type: ' + form_data['payment_type']
    twilio_client.messages.create(
        to=twilio_to_number,
        from_=twilio_from_number,
        body=sms_body)


def registerBooking(form_data):
    Person.objects.create(form_data['name'], form_data['email'], form_data['phone'])


#Returns success(bool), context{}
def handleBooking(request_obj):
    form_data = {}
    form_data['name'] = request_obj.POST['name']
    form_data['email'] = request_obj.POST['email']
    form_data['phone'] = request_obj.POST['phone']
    form_data['payment_type'] = request_obj.POST['payment_type']
    registerBooking(form_data)
    #sendBookingNotification(form_data)

    return (True, 123456)
