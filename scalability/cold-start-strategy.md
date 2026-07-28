# Cold Start Strategy for New Containers

## Overview

A cold start occurs when the platform launches a new container because application traffic has increased and additional capacity is required.

## Strategy

### 1. Keep Warm Instances

Maintain a small number of idle containers (2–3 replicas) that are always running and ready to receive traffic immediately.

---

### 2. Horizontal Auto Scaling

Automatically create additional containers when one or more of the following conditions are met:

- CPU usage exceeds 70%
- Memory usage exceeds 75%
- Request rate increases significantly
- Response time exceeds the defined threshold

---

### 3. Fast Container Startup

Reduce container startup time by:

- Using lightweight Docker images
- Installing only required packages
- Minimizing application initialization
- Preloading configuration files

---

### 4. Health Checks

A new container should not receive production traffic until it successfully passes:

- Readiness Probe
- Health Check

This ensures users are only routed to healthy containers.

---

### 5. Rolling Updates

Deploy new application versions gradually to avoid downtime.

Example:

Old Version
██████████

↓

New Version
██░░░░░░░░

↓

████░░░░░

↓

██████████

This strategy guarantees continuous service availability during deployments.
