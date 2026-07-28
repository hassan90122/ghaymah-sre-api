# Ghaymah CLI Integration

## Install the CLI

```bash
curl -fsSL https://ghaymah.systems/install.sh | bash
```

---

## Login

```bash
ghaymah login
```

---

## Verify Login

```bash
ghaymah whoami
```

---

## Build Docker Image

```bash
docker build -t ghaymah-sre-api .
```

---

## Push Image

```bash
docker push registry.ghaymah.systems/<username>/ghaymah-sre-api:latest
```

---

## Deploy

```bash
ghaymah deploy \
--image registry.ghaymah.systems/<username>/ghaymah-sre-api:latest
```

---

## Check Deployment

```bash
ghaymah apps list
```
