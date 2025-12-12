let items = [];

function addItem() {
    const name = document.getElementById("itemName").value.trim();
    const price = Number(document.getElementById("price").value);
    const qty = Number(document.getElementById("quantity").value);

    if (!name || price <= 0 || qty <= 0) {
        alert("Please enter valid item details");
        return;
    }

    let itemTotal = price * qty;
    let itemDiscount = 0;

    if (qty >= 5) {
        itemDiscount = itemTotal * 0.05;
    }

    itemTotal -= itemDiscount;

    items.push({ name, price, qty, itemTotal, itemDiscount });

    renderInvoice();
}

function renderInvoice() {
    const tbody = document.getElementById("invoiceBody");
    tbody.innerHTML = "";

    items.forEach(item => {
        tbody.innerHTML += `
            <tr>
                <td>${item.name}</td>
                <td>${item.price}</td>
                <td>${item.qty}</td>
                <td>${item.itemTotal.toFixed(2)}</td>
            </tr>
        `;
    });

    applyRules();
}

function applyRules() {
    let subtotal = 0;
    let totalItemDiscount = 0;

    items.forEach(item => {
        subtotal += item.itemTotal;
        totalItemDiscount += item.itemDiscount;
    });

    let billDiscount = subtotal > 1000 ? subtotal * 0.10 : 0;
    let surcharge = subtotal < 500 ? 50 : 0;
    let tax = (subtotal - billDiscount) * 0.05;

    let finalAmount = subtotal - billDiscount + tax + surcharge;

    document.getElementById("summary").innerHTML = `
        Subtotal: ₹${subtotal.toFixed(2)}<br>
        Quantity Discount: ₹${totalItemDiscount.toFixed(2)}<br>
        Bill Discount (10% if > ₹1000): ₹${billDiscount.toFixed(2)}<br>
        Tax (5%): ₹${tax.toFixed(2)}<br>
        Surcharge (₹50 if < ₹500): ₹${surcharge.toFixed(2)}<br>
        <hr>
        <strong>Final Amount Payable: ₹${finalAmount.toFixed(2)}</strong>
    `;
}
