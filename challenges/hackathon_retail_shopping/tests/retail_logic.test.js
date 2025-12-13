const { calculateInvoice } = require("../logic");

test("applies discount for subtotal > 1000", () => {
    const result = calculateInvoice(2000);
    expect(result.discount).toBe(200);
});

test("applies surcharge for subtotal < 500", () => {
    const result = calculateInvoice(300);
    expect(result.surcharge).toBe(50);
});

test("calculates tax correctly", () => {
    const result = calculateInvoice(1000);
    expect(result.tax).toBe(50);
});
