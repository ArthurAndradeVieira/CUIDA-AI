# 🛡️ PulseGuard AI — Documentação Técnica & Arquitetura

> **Inovathon 2026**  
> **Tema:** Ousadia em Inteligência Artificial para Gestão Ativa e Blindagem de Pessoas  
> **Pilar Central:** OUSADIA (Predição, Prescrição e Ação Autônoma)

---

## 1. Visão Geral do Produto

O **PulseGuard AI** é o primeiro agente prescritivo de sustentabilidade humana e blindagem operacional corporativa. Em vez de operar sob o modelo tradicional e reativo de RH — que descobre a estafa apenas no pedido de demissão ou na licença médica —, a solução conecta a telemetria diária de trabalho ao perfil comportamental e ao sentimento do colaborador para **antever o esgotamento e intervir diretamente no fluxo de trabalho**.

---

## 2. Coleta de Dados e Pipeline de Triangulação

O diferencial analítico do projeto baseia-se na **Triangulação Semântico-Operacional**, correlacionando três fontes de dados complementares:

### 2.1. Fontes de Dados Mapeadas

1. **Jira / Trello & Calendars (Telemetria Quantitativa):**
   * *Métricas coletadas:* Horas semanais gastas em reuniões, volume de cards atrasados vs. em aberto, frequência de trocas de contexto e percentual de commits/atividades fora do horário comercial.
   * *Papel no Modelo:* Mensura a sobrecarga cognitiva direta e a erosão do tempo de foco.

2. **Qulture.Rocks (Sentimento e Governança de Pessoas):**
   * *Métricas coletadas:* Notas de eNPS, feedbacks não estruturados de pesquisas de pulso, status de evolução do PDI (Plano de Desenvolvimento Individual) e histórico textual de 1-on-1s.
   * *Papel no Modelo:* Fornece a camada semântica e qualitativa, revelando desmotivação, frustração silenciosa ou isolamento.

3. **Solides Profiler (Perfil Comportamental):**
   * *Métricas coletadas:* Perfil dominante (*Analista*, *Planejador*, *Comunicador*, *Executor*), nível de exigência pessoal e índice de energia atual.
   * *Papel no Modelo:* Define a **sensibilidade individual** à carga operacional. Uma rotina com 30h de reuniões afeta drasticamente um *Analista* (que exige blocos ininterruptos de foco), enquanto o mesmo volume pode ser sustentável para um *Comunicador*.

---

## 3. Arquitetura da Inteligência Artificial

O processamento é realizado por um modelo fundacional avançado via engenharia de prompt estruturada com saída estrita garantida:

* **Modelo:** `gemini-2.5-flash`
* **Modo de Saída:** JSON Schema estruturado via `Pydantic` (`DiagnosticoPulseGuard`).
* **Lógica Prescritiva:**
  1. O motor cruza a carga horária com o perfil comportamental para diagnosticar incompatibilidades da rotina.
  2. Gera pautas de 1-on-1 personalizadas com perguntas calibradas à linguagem do liderado.
  3. Formula uma ação autônoma no ecossistema (bloqueio de cards, proteção de calendário).
* **Mecanismo de Resiliência (Zero Downtime):** O módulo `engine.py` inclui um sistema de *fallback* determinístico integrado. Caso haja oscilação de rede ou esgotamento de quota de API durante o pitch ao vivo, a demonstração continua operando perfeitamente.

---

## 4. Escolhas Técnicas e Ferramentas

| Ferramenta / Tecnologia | Função no Projeto | Justificativa Técnica |
| :--- | :--- | :--- |
| **Python 3.10+** | Backend e Orquestração | Linguagem padrão para pipelines de IA com ecossistema maduro de manipulação de dados e SDKs. |
| **Google GenAI SDK** | Motor de Inferência LLM | Baixa latência, suporte a system instructions complexas e tipagem estrita com schemas JSON. |
| **Pydantic** | Validação de Dados | Garante que o retorno da IA seja sempre consistente, sem risco de quebra de renderização no frontend. |
| **Streamlit** | Interface do Usuário (UI) | Prototipagem ágil e reativa em Python puro, permitindo montar dashboards executivos com gráficos e métricas em minutos. |
| **JSON Estruturado** | Armazenamento Sintético | Simula bancos de dados corporativos NoSQL sem dependências pesadas de infraestrutura externa no dia do evento. |

---

## 5. Como Executar o Protótipo

### Pré-requisitos
* Python 3.10 ou superior
* Gerenciador de pacotes `pip`

### Instalação

```bash
# 1. Instalar as dependências do projeto
pip install streamlit google-genai pydantic

# 2. (Opcional) Configurar a chave de API da Gemini
# Linux/Mac:
export GEMINI_API_KEY="sua_chave_aqui"
# Windows (PowerShell):
$env:GEMINI_API_KEY="sua_chave_aqui"

# 3. Executar o dashboard interativo
streamlit run app.py