"""  Contains the payment helpers """

import random
import string

from ..models.constants import APPROVED, PENDING
from ..models.ticket import Ticket


def create_ticket(passenger, flight, payment_log):
    """ Creates a new ticket

    Parameters
    ----------

    passenger: Passenger
        Passenger object.

    flight: Flight
        Flight object.

    payment_log: PaymentLog
        PaymentLog object.

    Returns
    -------

    ticket: Ticket
        Ticket object.

    """
    ticket = Ticket.objects.create(
        passenger=passenger,
        flight=flight,
        seat=flight.get_available_seat(),
        code_booking=generate_alphanumeric_code(),
        status=APPROVED,
        payment_log=payment_log
    )
    return ticket

def generate_alphanumeric_code():
    """ Generates a booking code that doesnt exist
        in another pending or approved ticket
    """
    characters = string.ascii_letters + string.digits
    existing_booking_codes = set(
        Ticket.objects.filter(
            status=APPROVED
            ).values_list('code_booking', flat=True)
    )
    while True:
        code = ''.join(random.choice(characters) for _ in range(6))
        if code not in existing_booking_codes:
            existing_booking_codes.add(code)
            return code
