file=open("m.txt","w")
file.write("""1. Admin Portal
Manage users (customers, delivery agents, etc.)
Add, update, and delete courier details
Assign couriers to delivery agents
Track and update the status of shipments
View reports on deliveries and pending shipments
Manage payments and transactions
2. Customer Portal
Register and log in
Request courier pickup
Track shipment status (shipped, in transit, delivered)
View order history
Make payments (if applicable)
Provide feedback or complaints
3. Delivery Agent Portal
View assigned courier deliveries
Update delivery status (picked up, in transit, delivered)
Mark unsuccessful deliveries and provide reasons
View payment details (if agents are paid per delivery)
4. Support/Staff Portal (Optional)
Handle customer complaints and support requests
Assist in lost or delayed shipments
Communicate between customers and delivery agents
5. Payment & Accounting Portal (Optional)
Manage payments from customers
Generate invoices and receipts
Track earnings and commissions for delivery agents""")
file.close()