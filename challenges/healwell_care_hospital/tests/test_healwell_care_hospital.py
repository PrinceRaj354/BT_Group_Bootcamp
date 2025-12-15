from challenges.healwell_care_hospital.healwell_care_hospital import (
    store_patient_details,
    select_services,
    fetch_service_costs,
    calculate_subtotal,
    apply_gst,
    generate_invoice,
)


def test_complete_healwell_hospital_flow():
    patient = store_patient_details(
        "Arjun Kumar", 35, "Male", "9876543210"
    )

    services = select_services([1, 4])
    assert services == ["General Consultation", "X-Ray"]

    costs = fetch_service_costs(services)
    assert costs == [500, 1500]

    subtotal = calculate_subtotal(costs)
    assert subtotal == 2000

    gst, grand_total = apply_gst(subtotal)
    assert gst == 360
    assert grand_total == 2360

    invoice = generate_invoice(
        patient, services, costs, subtotal, gst, grand_total
    )

    assert invoice["patient"]["name"] == "Arjun Kumar"
    assert invoice["subtotal"] == 2000
    assert invoice["grand_total"] == 2360
