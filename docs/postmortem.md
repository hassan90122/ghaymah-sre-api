# Incident Postmortem: Repeated OOMKilled Causing Application Downtime

## Incident Summary

**Incident Title:** Repeated OOMKilled Causing Application Downtime

**Date:** July 28, 2026

**Duration:** 45 Minutes

**Severity:** High

**Affected Service:** Ghaymah SRE API

### Impact

- The application was unavailable for approximately 45 minutes.
- Users experienced failed requests and service interruptions.
- Multiple container restarts occurred due to repeated OOMKilled events.

---

# Timeline

| Time | Event |
|------|-------|
| 10:00 | Application deployed successfully |
| 10:08 | Memory usage started increasing rapidly |
| 10:12 | First OOMKilled event occurred |
| 10:13 - 10:40 | Container repeatedly restarted due to memory exhaustion |
| 10:20 | Monitoring system generated alerts |
| 10:25 | SRE team started investigation |
| 10:35 | Memory leak identified |
| 10:42 | Memory limit increased and deployment restarted |
| 10:45 | Service fully recovered |

---

# Root Cause Analysis

The application experienced a memory leak that continuously increased memory consumption.

Once the container exceeded its configured memory limit, Kubernetes terminated it with an **OOMKilled** event.

Because the underlying issue was not resolved immediately, the container repeatedly restarted, causing approximately 45 minutes of service downtime.

---

# Recommendations

## Immediate Actions

- Increase the container memory limit.
- Restart the deployment after applying the fix.
- Monitor memory usage during recovery.

## Long-Term Improvements

- Configure Horizontal Pod Autoscaler (HPA).
- Set appropriate CPU and memory requests and limits.
- Enable memory utilization alerts.
- Monitor container restart counts.
- Perform load testing before production deployments.
- Regularly profile the application to detect memory leaks.

---

# Auto-Scaling Policy

## Objective

Automatically scale the application based on workload to maintain availability and reduce the risk of resource exhaustion.

| Configuration | Value |
|--------------|-------|
| Minimum Replicas | 2 |
| Maximum Replicas | 10 |
| CPU Target | 70% |
| Memory Target | 75% |
| Scale Up | Add 1–2 replicas after 2 minutes above threshold |
| Scale Down | Remove 1 replica after 10 minutes of low utilization |

## Scale-Up Rules

Trigger scaling when:

- CPU usage exceeds 70%.
- Memory usage exceeds 75%.
- Traffic increases significantly.

Action:

- Create additional application replicas.
- Distribute requests using the load balancer.

## Scale-Down Rules

Trigger scaling when:

- CPU remains below 30%.
- Memory remains below 40%.
- Low traffic continues for at least 10 minutes.

Action:

- Gradually remove unused replicas while keeping at least two running.

---

# Early Detection Using Monitoring

## Monitoring Metrics

### Memory Usage

Monitor:

- Container memory usage
- Memory utilization percentage
- Available memory

**Alert Rule**

```
Memory usage > 80% for 5 minutes
```

### OOMKilled Events

Monitor:

- Number of OOMKilled events
- Container restart count

**Alert Rule**

```
Restart count > 3 within 10 minutes
```

### Container Health

Monitor:

- /health endpoint
- Readiness probe
- Liveness probe
- Pod status

Alert if:

- Health endpoint returns a non-200 status.
- Pods enter CrashLoopBackOff or Pending state.

### Application Performance

Monitor:

- HTTP response time
- Request rate
- Error rate (5xx)
- Active requests

---

# Monitoring Dashboard

The dashboard should display:

- Application Status
- CPU Usage
- Memory Usage
- Response Time
- Total Requests
- Container Restarts
- OOMKilled Events
- Running Replicas

---

# Alert Workflow

1. Prometheus collects application and container metrics.
2. Alertmanager evaluates alert rules.
3. Notifications are sent to the SRE team (Email, Slack, or Microsoft Teams).
4. Engineers investigate the issue using Grafana dashboards and application logs.
5. If auto-scaling is enabled, additional replicas are created automatically while the issue is being investigated.

---

# Conclusion

The outage was caused by excessive memory consumption that resulted in repeated OOMKilled events and continuous container restarts.

Implementing proactive monitoring, alerting, resource limits, and auto-scaling policies will significantly reduce the likelihood and impact of similar incidents in the future.
