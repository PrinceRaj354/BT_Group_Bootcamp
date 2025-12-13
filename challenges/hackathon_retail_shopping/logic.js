function calculateInvoice(subtotal) {
    let discount = subtotal > 1000 ? subtotal * 0.10 : 0;
    let surcharge = subtotal < 500 ? 50 : 0;
    let tax = (subtotal - discount) * 0.05;

    return {
        discount,
        surcharge,
        tax,
        finalAmount: subtotal - discount + tax + surcharge
    };
}

module.exports = { calculateInvoice };
