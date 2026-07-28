# Using Ghaymah Block Storage for Stateful Workloads

## Overview

Ghaymah Block Storage provides persistent storage that remains available even if containers are restarted, replaced, or rescheduled.

It is designed for applications that must preserve data.

## Common Stateful Workloads

- PostgreSQL
- MySQL
- MongoDB
- Elasticsearch
- Jenkins
- GitLab
- File Storage
- Application Uploads

---

## Benefits

### Persistent Data

Data remains available after:

- Container restart
- Node failure
- Deployment updates

---

### High Performance

Block Storage provides low-latency, high-performance storage suitable for databases and transactional workloads.

---

### Easy Scaling

Storage volumes can be expanded without recreating the application.

---

### Reliability

Storage is independent of containers, reducing the risk of data loss and improving application resilience.

---

## Example Architecture

Application Container
        |
        |
Persistent Volume
        |
        |
Ghaymah Block Storage
        |
        |
 PostgreSQL Database
