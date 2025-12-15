SERVICES = [
    "General Consultation",
    "Blood Test",
    "Covid Test",
    "X-Ray",
    "CT Scan",
    "MRI",
]

COSTS = [500, 300, 800, 1500, 4000, 7000]
GST_RATE = 0.18


# Level 1: Patient details
def store_patient_details(name, age, gender, contact):
    return {
        "name": name,
        "age": age,
        "gender": gender,
        "contact": contact,
    }


# Level 2: Service selection
def select_services(indices):
    return [SERVICES[i - 1] for i in indices]


# Level 3: Fetch service costs
def fetch_service_costs(selected_services):
    costs = []
    for service in selected_services:
        index = SERVICES.index(service)
        costs.append(COSTS[index])
    return costs


# Level 4: Calculate subtotal
def calculate_subtotal(costs):
    return sum(costs)


# Level 5: Apply GST
def apply_gst(subtotal):
    gst = subtotal * GST_RATE
    return gst, subtotal + gst


# Level 6: Generate invoice
def generate_invoice(patient, services, costs, subtotal, gst, grand_total):
    return {
        "patient": patient,
        "services": list(zip(services, costs)),
        "subtotal": subtotal,
        "gst": gst,
        "grand_total": grand_total,
    }
