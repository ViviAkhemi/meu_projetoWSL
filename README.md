##### ⚠️ Nota importante

Este repositório tem como objetivo fornecer recursos educacionais.  
Por favor, utilize-o de forma responsável e respeitando as limitações de uso para fins não comerciais.


# 🔐 MVP_SecurePlay

Plataforma gamificada para treinamento em **segurança da informação** voltada a colaboradores corporativos, com foco em níveis **Leigo** e **Iniciante**. Criado com Django (backend) e Vue.js (frontend), usando Docker e PostgreSQL.

---

## 🚀 Funcionalidades (MVP)

- ✅ Desafios para usuários leigos e iniciantes
- ✅ Sistema de pontuação e badges
- ✅ Interface web com Vue.js
- ✅ Backend com API REST em Django
- ✅ Banco de dados PostgreSQL (em container)
- ✅ Docker Compose para fácil execução local

---

## 📦 Tecnologias Usadas

- **Backend:** Python 3.11, Django, Django REST Framework, Djoser (auth)
- **Frontend:** Vue.js 3, Vue Router
- **Banco de Dados:** PostgreSQL
- **DevOps:** Docker, Docker Compose

---

## 🧰 Como Rodar o Projeto (local)

### Pré-requisitos

Instale:
- [Python 3.11+](https://www.python.org/)
- [Node.js 18+](https://nodejs.org/)
- [Docker](https://www.docker.com/)
- [Git](https://git-scm.com/)

---

### 1. Clone este repositório

```bash
git clone https://github.com/ViviAkhemi/mvpsecureplay.git
cd mvpsecureplay

docker-compose up --build

Backend rodando em: http://localhost:8000

Frontend rodando em: http://localhost:8080

mvpsecureplay/
├── backend/
│   ├── core/           # Projeto Django
│   ├── users/          # Autenticação e perfis
│   ├── lessons/        # Conteúdos gamificados
│   ├── progress/       # Progresso e badges
├── frontend/
│   └── mvpsecure-ui/   # Projeto Vue.js
├── docker-compose.yml
├── README.md


