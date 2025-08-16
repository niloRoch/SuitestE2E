# Portfolio E2E Testing

## 📋 Sobre o Projeto

Este projeto implementa um portfolio pessoal usando Streamlit com testes end-to-end automatizados usando Selenium e Pytest.

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

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT.
