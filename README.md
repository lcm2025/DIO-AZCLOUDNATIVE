<h1 align="center">🌥️ Projeto Azure Cloud Native</h1>

<p align="center">
  <strong>Scripts e automações para trabalhar com recursos na nuvem usando o Microsoft Azure.</strong><br>
  Desenvolvido como parte do curso <em>DIO - Cloud Native</em>.
</p>

---

## 📁 Estrutura do Projeto

```bash
📦 DIO-AZCLOUDNATIVE/
├── main.py               # Script principal em Python
├── requirements.txt      # Dependências do projeto
├── infos.txt             # Informações auxiliares (ignorado pelo Git)
├── .env                  # Variáveis de ambiente (ignorado pelo Git)
└── README.md             # Este arquivo

🚀 Primeiros Passos
<h3 align="center">☁️ Configuração do Ambiente no Azure</h3> <p align="center"> Abaixo estão os passos iniciais para configurar os recursos no <strong>Microsoft Azure</strong> e rodar o projeto localmente. </p>

🔧 Etapas no Portal Azure
✅ Criação do Resource Group (LAB001) no 🌐 Portal Azure
✅ Criação do Azure SQL Server e Banco de Dados SQL
✅ Criação do Azure Blob Storage vinculado ao mesmo Resource Group

🐍 Desenvolvimento em Python (VS Code)
Criação do script main.py para conectar-se ao banco e ao blob storage

Utilização de variáveis de ambiente no .env para proteger credenciais

Organização dos pacotes no requirements.txt

💻 Executando o Projeto Localmente

# 1. Clone o repositório
git clone https://github.com/lcm2025/DIO-AZCLOUDNATIVE.git
cd DIO-AZCLOUDNATIVE

# 2. Crie e configure seu arquivo .env
cp .env.example .env
# Edite o arquivo com suas chaves do Azure

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Execute o script principal
python main.py

🛡️ Segurança
⚠️ Nunca envie seu arquivo .env ou infos.txt para o repositório público.
Eles devem conter apenas dados locais e sensíveis, como senhas e tokens.
Use sempre o .gitignore para protegê-los.

👨‍💻 Autor
Feito com 💙 por Luciano de Castro
🔗 LinkedIn: (https://www.linkedin.com/in/luciano-de-castro-b216803a/)

