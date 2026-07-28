# Scalability Calculation

## Given

Incoming traffic = 15,000 requests/second

Container capacity = 500 requests/second

Safety margin = 30%

---

## Step 1

Minimum containers required:

15000 / 500 = 30 containers

---

## Step 2

Add a 30% safety margin:

30 × 1.30 = 39 containers

---

## Final Result

Required containers = **39**

This deployment can safely handle 15,000 requests per second while providing additional capacity for traffic spikes and failover.
