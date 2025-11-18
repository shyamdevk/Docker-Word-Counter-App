
# 📘 Docker Word Counter App 

A multi-container Docker application that counts words from user input using:

* **Frontend** → accepts input
* **Redis** → message queue
* **Worker** → background processor
* **PostgreSQL** → stores results
* **Result Frontend** → displays stored results

This project demonstrates Docker networking, multi-service communication, and container orchestration.

---

# 🚀 **1. Project Architecture**

![Screenshot](https://github.com/shyamdevk/docker-word-counter-app/blob/images/archi.png)


* **Frontend** sends text to **Redis queue**
* **Worker** reads from Redis, counts words, stores result in **PostgreSQL**
* **Result Frontend** displays saved results

Communication happens through a custom Docker bridge network.

---

# 🗂️ **2. Project Structure**

```
Docker-word-counter-app/
│── frontend/          # Python Flask input frontend
│── worker/            # Python worker
│── result-frontend/   # Python Flask output frontend
│── README.md          # Documentation
```

---

# 📊 **3. Code Composition by Language**

| Language / File Type | Usage (%) | Description                     |
| -------------------- | --------- | ------------------------------- |
| **Python**           | **75%**   | Flask apps, worker logic        |
| **Dockerfile**       | **15%**   | Building container images       |
| **HTML/CSS**         | **5%**    | Frontend templates              |
| **Shell / Config**   | **5%**    | Container commands, env configs |

> These percentages are approximate based on the repository contents.

---

# 🛠 **4. Requirements**

* Docker
* Git
* Stable internet connection
* Basic understanding of containers and networking

---

# 🌐 **5. Create a Custom Docker Bridge Network**

All containers will communicate over a custom LAN-like network:

```bash
docker network create app-net
```

Verify:

```bash
docker network ls
```

---

# 🐳 **6. Run Redis Container (Queue Service)**

```bash
docker run -d --name redis --network app-net redis
```

Verify:

```bash
docker logs redis
```

---

# 🐘 **7. Run PostgreSQL Container (Database)**

```bash
docker run -d --name db \
  --network app-net \
  -e POSTGRES_USER=user \
  -e POSTGRES_PASSWORD=pass \
  -e POSTGRES_DB=wordcount \
  -v pgdata:/var/lib/postgresql/data \
  postgres
```

Check if running:

```bash
docker ps --filter name=db
```

---

# 🗄️ **8. Create Database Table**

After Postgres finishes initializing:

```bash
docker exec -it db psql -U user -d wordcount \
  -c "CREATE TABLE IF NOT EXISTS results (
        id SERIAL PRIMARY KEY,
        text TEXT,
        word_count INT
      );"
```

Verify table:

```bash
docker exec -it db psql -U user -d wordcount -c "\dt"
```

---

# 🏗️ **9. Build Docker Images**

From project root:

```bash
docker build -t wordcount-frontend ./frontend
docker build -t wordcount-worker ./worker
docker build -t wordcount-result-frontend ./result-frontend
```

Verify images:

```bash
docker images | grep wordcount
```

---

# ▶️ **10. Run the App Containers**

### **Frontend (input page)**

```bash
docker run -d --name frontend -p 5000:5000 --network app-net wordcount-frontend
```

### **Worker (background processor)**

```bash
docker run -d --name worker --network app-net wordcount-worker
```

### **Result Frontend (output page)**

```bash
docker run -d --name result-frontend -p 7000:5000 --network app-net wordcount-result-frontend
```

---

# 🔎 **11. Verify All Containers Are Running**

```bash
docker ps
```

You should see:

* redis
* db
* frontend
* worker
* result-frontend

---

# 🌍 **12. Test the App**

### Enter text:

```
http://localhost:5000
```
![Screenshot](https://github.com/shyamdevk/docker-word-counter-app/blob/images/1.png)
![Screenshot](https://github.com/shyamdevk/docker-word-counter-app/blob/images/2.png)
### View results:

```
http://localhost:7000
```

---
![Screenshot](https://github.com/shyamdevk/docker-word-counter-app/blob/images/3.png)
# 🧪 **13. Connectivity Testing (Optional)**

Start a debug container:

```bash
docker run --rm -it --network app-net alpine sh
```

Inside:

```bash
ping redis
ping db
ping frontend
```

---

# 🛠️ **14. Useful Docker Network Commands**

| Command                                       | Description              |
| --------------------------------------------- | ------------------------ |
| `docker network ls`                           | List all networks        |
| `docker network inspect app-net`              | Inspect network details  |
| `docker network connect app-net container`    | Add container to network |
| `docker network disconnect app-net container` | Remove container         |
| `docker network rm app-net`                   | Delete the network       |

---

# ⚠️ **15. Troubleshooting**

### ❗Frontend cannot connect to Redis

Check network:

```bash
docker inspect frontend | grep app-net
```

### ❗Worker cannot connect to DB

Check logs:

```bash
docker logs worker
```

### ❗Postgres "permission denied"

Reset volume:

```bash
docker rm -f db
docker volume rm pgdata
```

---

# 🧹 **16. Cleanup Commands**

Stop all containers:

```bash
docker stop frontend worker result-frontend redis db
```

Remove them:

```bash
docker rm frontend worker result-frontend redis db
```

Delete network:

```bash
docker network rm app-net
```

---

# 📦 **17. (Optional) docker-compose Version**

If you want, I can generate a **fully working docker-compose.yml** that runs the entire project with **one command**.

---

# 🎉 **18. Summary**

This project teaches:

* Docker bridge networking
* Multi-container communication
* Redis queue processing
* PostgreSQL CRUD
* Flask microservices
* Container image building
* Debugging Docker networks

---


