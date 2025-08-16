# Suite E2E Testing

## 📋 Sobre o Projeto

Este projeto implementa um suite pessoal com front-end em Streamlit para testes end-to-end automatizados usando Selenium e Pytest.

![Python](https://img.shields.io/badge/python-v3.11+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28.1-ff6b6b.svg)
![Selenium](https://img.shields.io/badge/Selenium-4.14.0-43B02A.svg)
![Pytest](https://img.shields.io/badge/Pytest-7.4.0-6DB33F.svg)

**🔗 [🚀 Acesse o Dashboard Online](https://suiteste2.streamlit.app/)** 

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://suiteste2.streamlit.app/)

</div>

---
## 🚀 Estrutura do Projeto

```
portfolio_e2e/
├── app/                    # Aplicação Streamlit
│   ├── main.py            # Arquivo principal
│   ├── pages/             # Páginas da aplicação
│   └── utils/             # Utilitários
├── tests/                 # Testes automatizados
│   ├── test_e2e/         # Testes end-to-end
│   └── fixtures/         # Dados de teste
└── requirements.txt       # Dependências
```

## 🔧 Instalação

1. Clone o repositório
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## ▶️ Como Executar

### Executar a aplicação:
```bash
cd app
streamlit run main.py
```

### Executar os testes:
```bash
pytest tests/ -v
```

### Executar testes específicos:
```bash
# Testes de navegação
pytest tests/test_e2e/test_navigation.py -v

# Testes de responsividade
pytest tests/test_e2e/test_responsiveness.py -v

# Gerar relatório HTML
pytest tests/ --html=reports/report.html
```

## 🧪 Tipos de Teste

- **Navegação**: Testa navegação entre páginas
- **Portfolio**: Testa funcionalidades do portfolio
- **Contato**: Testa formulário de contato
- **Responsividade**: Testa layout em diferentes dispositivos

## 📱 Responsividade

O portfolio é testado nas seguintes resoluções:
- Desktop: 1920x1080
- Laptop: 1366x768
- Tablet: 768x1024
- Mobile: 375x667

## 🛠️ Tecnologias

- **Frontend**: Streamlit
- **Testes**: Pytest + Selenium
- **Browser**: Chrome (headless)
- **Relatórios**: pytest-html

## 📊 Relatórios

Os relatórios de teste são gerados em HTML e salvos na pasta `reports/`.

## Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT.

## **Contato**

[![Website](https://img.shields.io/badge/Website-4c1d95?style=for-the-badge&logo=firefox&logoColor=a855f7)](https://www.nilorocha.tech)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/nilo-rocha-/)
[![Email](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:nilo.roch4@gmail.com)

---

---

#
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%">


![Footer](https://capsule-render.vercel.app/api?type=waving&color=FF6B6B&height=100&section=footer&text=Thanks%20for%20exploring%20the%20insights&fontSize=16&fontColor=ffffff&animation=twinkling)

</div>

---
