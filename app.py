import base64
import json
import streamlit as st
from engine import analisar_colaborador

def carregar_logo_b64():
    try:
        with open("assets/logo.jpg", "rb") as f:
            return f"data:image/jpeg;base64,{base64.b64encode(f.read()).decode('utf-8')}"
    except Exception:
        return "https://img.icons8.com/fluency/96/shield.png"

LOGO_DATA_URI = carregar_logo_b64()

st.set_page_config(
    page_title="Cuida AI — Gestão Ativa & Sustentabilidade Humana",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

def render_html(html_code: str):
    """Remove ALL leading whitespace from each line to prevent Streamlit <pre><code> blocks."""
    lines = html_code.strip().splitlines()
    clean_lines = [line.lstrip() for line in lines]
    st.markdown('\n'.join(clean_lines), unsafe_allow_html=True)


# ==============================================================================
# DESIGN SYSTEM: ESTILO SOLIDES + QULTURE.ROCKS (MODERNO, RESPONSIVO & ALTO CONTRASTE)
# ==============================================================================
render_html(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
}

/* Header e App Bar */
.app-header {
    background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #312e81 100%);
    border: 1px solid #334155;
    border-radius: 16px;
    padding: 24px 28px;
    color: #ffffff;
    margin-bottom: 22px;
    box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.3);
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 16px;
}
.app-header h1 {
    margin: 0;
    font-size: 1.75rem;
    font-weight: 800;
    letter-spacing: -0.02em;
    color: #ffffff !important;
    display: flex;
    align-items: center;
    gap: 12px;
}
.app-header p {
    margin: 4px 0 0 0;
    color: #cbd5e1;
    font-size: 0.95rem;
}
.badge-pill {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 5px 12px;
    border-radius: 9999px;
    font-size: 0.8rem;
    font-weight: 600;
    letter-spacing: 0.02em;
}
.pill-inovathon {
    background: rgba(99, 102, 241, 0.25);
    color: #c7d2fe;
    border: 1px solid rgba(165, 180, 252, 0.4);
}

/* Hero Card do Colaborador */
.colab-hero-card {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 16px;
    padding: 20px 24px;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.2);
    margin-bottom: 22px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 18px;
}
.colab-profile-left {
    display: flex;
    align-items: center;
    gap: 18px;
}
.colab-avatar {
    width: 62px;
    height: 62px;
    border-radius: 50%;
    background: #0f172a;
    border: 2px solid #818cf8;
    object-fit: cover;
}
.colab-info h2 {
    margin: 0;
    font-size: 1.35rem;
    font-weight: 700;
    color: #f8fafc !important;
}
.colab-info p {
    margin: 2px 0 0 0;
    color: #94a3b8;
    font-size: 0.9rem;
}
.colab-hero-stats {
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
}
.hero-stat-box {
    background: #0f172a;
    border: 1px solid #334155;
    border-radius: 10px;
    padding: 10px 16px;
    text-align: center;
    min-width: 110px;
}
.hero-stat-title {
    font-size: 0.72rem;
    text-transform: uppercase;
    color: #94a3b8;
    font-weight: 600;
    letter-spacing: 0.04em;
}
.hero-stat-value {
    font-size: 1.1rem;
    font-weight: 700;
    margin-top: 3px;
}

/* Cards Temáticos (Solides / Qulture / Jira) */
.card-solides {
    background: #1e293b;
    border: 1px solid #334155;
    border-top: 4px solid #8b5cf6;
    border-radius: 14px;
    padding: 18px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    height: 100%;
}
.card-solides h3 {
    color: #c4b5fd !important;
    font-size: 1.1rem;
    font-weight: 700;
    margin: 0 0 14px 0;
    display: flex;
    align-items: center;
    gap: 8px;
}

.card-jira {
    background: #1e293b;
    border: 1px solid #334155;
    border-top: 4px solid #0284c7;
    border-radius: 14px;
    padding: 18px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    height: 100%;
}
.card-jira h3 {
    color: #38bdf8 !important;
    font-size: 1.1rem;
    font-weight: 700;
    margin: 0 0 14px 0;
    display: flex;
    align-items: center;
    gap: 8px;
}

.card-qulture {
    background: #1e293b;
    border: 1px solid #334155;
    border-top: 4px solid #10b981;
    border-radius: 14px;
    padding: 18px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    height: 100%;
}
.card-qulture h3 {
    color: #34d399 !important;
    font-size: 1.1rem;
    font-weight: 700;
    margin: 0 0 14px 0;
    display: flex;
    align-items: center;
    gap: 8px;
}

/* Linhas de Métricas Internas */
.metric-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 9px 0;
    border-bottom: 1px solid #334155;
    font-size: 0.88rem;
}
.metric-row:last-child {
    border-bottom: none;
}
.metric-label {
    color: #94a3b8;
    font-weight: 500;
}
.metric-val {
    color: #f8fafc;
    font-weight: 700;
}

/* Badges de Perfil e Risco */
.badge-analista { background: #3b0764; color: #d8b4fe; border: 1px solid #a855f7; }
.badge-planejador { background: #082f49; color: #7dd3fc; border: 1px solid #0284c7; }
.badge-comunicador { background: #451a03; color: #fde68a; border: 1px solid #d97706; }
.badge-executor { background: #4c0519; color: #fecdd3; border: 1px solid #e11d48; }

.badge-risco-critico {
    background: rgba(239, 68, 68, 0.2);
    color: #f87171;
    border: 1px solid #ef4444;
    font-weight: 700;
    padding: 4px 10px;
    border-radius: 6px;
}
.badge-risco-alerta {
    background: rgba(245, 158, 11, 0.2);
    color: #fbbf24;
    border: 1px solid #f59e0b;
    font-weight: 700;
    padding: 4px 10px;
    border-radius: 6px;
}
.badge-risco-estavel {
    background: rgba(16, 185, 129, 0.2);
    color: #34d399;
    border: 1px solid #10b981;
    font-weight: 700;
    padding: 4px 10px;
    border-radius: 6px;
}

/* Caixa Executiva de Diagnóstico */
.executive-card {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 14px;
    padding: 22px;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.2);
    margin-bottom: 20px;
}
.executive-summary-box {
    background: #0f172a;
    border-left: 4px solid #818cf8;
    border-radius: 0 10px 10px 0;
    padding: 14px 18px;
    margin: 14px 0;
    font-size: 0.95rem;
    line-height: 1.5;
    color: #e2e8f0;
}
.profile-impact-box {
    background: #2e1065;
    border-left: 4px solid #a855f7;
    border-radius: 0 10px 10px 0;
    padding: 14px 18px;
    margin: 14px 0;
    font-size: 0.92rem;
    line-height: 1.5;
    color: #e9d5ff;
}

/* Gatilhos / Triggers */
.trigger-item {
    background: #450a0a;
    border: 1px solid #7f1d1d;
    border-left: 4px solid #ef4444;
    border-radius: 8px;
    padding: 11px 14px;
    margin-bottom: 8px;
    font-size: 0.88rem;
    color: #fecaca;
    display: flex;
    align-items: center;
    gap: 10px;
}
.trigger-item-ok {
    background: #052e16;
    border: 1px solid #14532d;
    border-left: 4px solid #22c55e;
    border-radius: 8px;
    padding: 11px 14px;
    margin-bottom: 8px;
    font-size: 0.88rem;
    color: #bbf7d0;
    display: flex;
    align-items: center;
    gap: 10px;
}

/* Pauta 1-on-1 Card */
.one-on-one-question {
    background: #0f172a;
    border: 1px solid #334155;
    border-left: 4px solid #10b981;
    border-radius: 10px;
    padding: 14px 16px;
    margin-bottom: 12px;
}
.one-on-one-num {
    font-weight: 700;
    color: #34d399;
    font-size: 0.82rem;
    text-transform: uppercase;
    margin-bottom: 4px;
}
.one-on-one-text {
    font-size: 0.94rem;
    color: #f8fafc;
    font-weight: 500;
}

/* Timeline de 1-on-1s */
.timeline-item {
    border-left: 2px solid #475569;
    padding-left: 16px;
    padding-bottom: 14px;
    position: relative;
}
.timeline-item::before {
    content: '';
    position: absolute;
    left: -6px;
    top: 2px;
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background-color: #818cf8;
    border: 2px solid #0f172a;
}
.timeline-date {
    font-size: 0.75rem;
    font-weight: 700;
    color: #94a3b8;
    text-transform: uppercase;
}
.timeline-content {
    font-size: 0.88rem;
    color: #cbd5e1;
    margin-top: 3px;
}

/* Escudo Operacional / Prescritivo */
.shield-banner {
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
    border: 1px solid #334155;
    border-radius: 14px;
    padding: 22px;
    color: #f8fafc;
    margin-top: 10px;
}
.shield-banner h4 {
    color: #38bdf8 !important;
    margin: 0 0 10px 0;
    font-size: 1.15rem;
    display: flex;
    align-items: center;
    gap: 8px;
}
.shield-text {
    font-size: 0.94rem;
    line-height: 1.5;
    color: #cbd5e1;
    margin-bottom: 16px;
}
.shield-action-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 12px;
    margin-top: 14px;
}
.shield-action-item {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 8px;
    padding: 12px;
    font-size: 0.85rem;
    color: #e2e8f0;
}

/* Pulso Quote Box */
.pulse-quote-box {
    background: #064e3b;
    border: 1px solid #059669;
    border-radius: 10px;
    padding: 12px 16px;
    font-style: italic;
    color: #a7f3d0;
    font-size: 0.88rem;
    margin-top: 8px;
}
</style>
"""
)

# ==============================================================================
# CARREGAMENTO DE DADOS
# ==============================================================================
@st.cache_data
def carregar_dados():
    with open("data.json", "r", encoding="utf-8") as f:
        return json.load(f)

dados = carregar_dados()
colaboradores = dados["colaboradores"]

# ==============================================================================
# BARRA LATERAL (SIDEBAR): GESTÃO DE SQUAD E CONEXÕES
# ==============================================================================
sidebar_logo = """
<div style="display:flex; align-items:center; gap:12px; margin-bottom:12px;">
<img src="https://img.icons8.com/fluency/96/shield.png" width="44"/>
<div>
<h3 style="margin:0; font-size:1.15rem; font-weight:800; color:#f8fafc;">Cuida AI</h3>
<span style="font-size:0.75rem; color:#94a3b8; font-weight:600;">Inovathon 2026</span>
</div>
</div>
""".strip()
st.sidebar.markdown(sidebar_logo, unsafe_allow_html=True)

st.sidebar.caption("Triangulação de Solides + Jira + Qulture.Rocks")
st.sidebar.markdown("---")

# Seletor de Colaborador na Barra Lateral
st.sidebar.markdown("#### 👤 Seleção de Colaborador")
nomes = [c["nome"] for c in colaboradores]

if "nome_selecionado" not in st.session_state:
    st.session_state["nome_selecionado"] = nomes[0]

nome_escolhido = st.sidebar.selectbox(
    "Colaborador Ativo:",
    nomes,
    index=nomes.index(st.session_state["nome_selecionado"]),
    key="select_colab_sidebar",
)
st.session_state["nome_selecionado"] = nome_escolhido
colab = next(c for c in colaboradores if c["nome"] == nome_escolhido)

# Perfil Rápido do Colaborador na Sidebar
sidebar_perfil = f"""
<div style="background:#1e293b; border:1px solid #334155; border-radius:10px; padding:12px; margin-top:8px;">
<div style="font-size:0.75rem; color:#94a3b8; font-weight:600; text-transform:uppercase;">CARGO & SQUAD</div>
<div style="font-weight:700; color:#f8fafc; font-size:0.88rem; margin-top:2px;">{colab['cargo']}</div>
<div style="font-size:0.8rem; color:#cbd5e1; margin-bottom:8px;">{colab['time']}</div>
<div style="font-size:0.75rem; color:#94a3b8; font-weight:600; text-transform:uppercase;">PERFIL COMPORTAMENTAL</div>
<div style="display:inline-block; margin-top:4px; font-weight:700; font-size:0.8rem; padding:3px 8px; border-radius:6px; background:#3b0764; color:#d8b4fe; border:1px solid #a855f7;">
🧬 {colab['solides_profiler']['perfil_predominante']}
</div>
</div>
""".strip()
st.sidebar.markdown(sidebar_perfil, unsafe_allow_html=True)

st.sidebar.markdown("---")

# Status dos Conectores de Dados
st.sidebar.markdown("#### 🔌 Conectores Ativos")
sidebar_conectores = """
<div style="display:flex; flex-direction:column; gap:6px; font-size:0.82rem;">
<div style="display:flex; align-items:center; justify-content:space-between; background:#1e293b; border:1px solid #334155; padding:6px 10px; border-radius:6px;">
<span style="color:#e2e8f0;">🧠 <b>Solides Profiler</b></span>
<span style="color:#34d399; font-weight:700;">🟢 Ativo</span>
</div>
<div style="display:flex; align-items:center; justify-content:space-between; background:#1e293b; border:1px solid #334155; padding:6px 10px; border-radius:6px;">
<span style="color:#e2e8f0;">⚡ <b>Jira & Calendar</b></span>
<span style="color:#34d399; font-weight:700;">🟢 Sincronizado</span>
</div>
<div style="display:flex; align-items:center; justify-content:space-between; background:#1e293b; border:1px solid #334155; padding:6px 10px; border-radius:6px;">
<span style="color:#e2e8f0;">🎯 <b>Qulture.Rocks</b></span>
<span style="color:#34d399; font-weight:700;">🟢 Conectado</span>
</div>
<div style="display:flex; align-items:center; justify-content:space-between; background:#1e293b; border:1px solid #334155; padding:6px 10px; border-radius:6px;">
<span style="color:#e2e8f0;">🤖 <b>Gemini 2.5 Flash</b></span>
<span style="color:#34d399; font-weight:700;">🟢 Online</span>
</div>
</div>
""".strip()
st.sidebar.markdown(sidebar_conectores, unsafe_allow_html=True)

st.sidebar.markdown("---")
botao_analisar = st.sidebar.button(
    "⚡ Recalcular Diagnóstico com IA",
    type="primary",
    use_container_width=True,
)

# ==============================================================================
# HEADER PRINCIPAL DA PLATAFORMA
# ==============================================================================
render_html(
    """
<div class="app-header">
    <div>
        <h1>🛡️ Cuida AI <span class="badge-pill pill-inovathon">Inovathon 2026</span></h1>
        <p>Plataforma Preditiva e Prescritiva de Blindagem Operacional e Sustentabilidade Humana</p>
    </div>
    <div style="display: flex; gap: 10px; align-items: center;">
        <span style="font-size:0.85rem; background:rgba(255,255,255,0.08); padding:8px 14px; border-radius:8px; border:1px solid rgba(255,255,255,0.15); color:#cbd5e1;">
            📡 <b>Triangulação:</b> Solides &bull; Jira &bull; Qulture.Rocks
        </span>
    </div>
</div>
"""
)

# ==============================================================================
# SQUAD OVERVIEW (PANORAMA DA EQUIPE — ESTILO SOLIDES / QULTURE.ROCKS)
# ==============================================================================
st.markdown("### 👥 Panorama da Squad (Visão Geral de Risco)")

col_cards = st.columns(len(colaboradores))
for idx, c in enumerate(colaboradores):
    is_active = (c["nome"] == colab["nome"])
    border_style = "2px solid #818cf8" if is_active else "1px solid #334155"
    bg_style = "#1e1b4b" if is_active else "#1e293b"
    
    if "Crítico" in c["cenario_esperado"]:
        r_badge = '<span class="badge-risco-critico">🔴 Risco Crítico</span>'
    elif "Alerta" in c["cenario_esperado"]:
        r_badge = '<span class="badge-risco-alerta">🟡 Alerta Moderado</span>'
    else:
        r_badge = '<span class="badge-risco-estavel">🟢 Estável</span>'
    
    with col_cards[idx]:
        render_html(
            f"""
<div style="background:{bg_style}; border:{border_style}; border-radius:12px; padding:14px; min-height:130px;">
    <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:6px;">
        <span style="font-weight:700; font-size:0.95rem; color:#f8fafc;">{c['nome']}</span>
        {r_badge}
    </div>
    <div style="font-size:0.8rem; color:#94a3b8; margin-bottom:8px;">{c['cargo']}</div>
    <div style="display:flex; justify-content:space-between; align-items:center; font-size:0.78rem; color:#cbd5e1; background:#0f172a; padding:6px 10px; border-radius:6px;">
        <span><b>Perfil:</b> {c['solides_profiler']['perfil_predominante'].split('/')[0].strip()}</span>
        <span><b>Reuniões:</b> {c['jira_telemetria']['horas_reuniao_semana']}h</span>
    </div>
</div>
"""
        )
        if st.button(f"Ver {c['nome'].split()[0]}", key=f"btn_sel_{c['id']}", use_container_width=True):
            st.session_state["nome_selecionado"] = c["nome"]
            st.rerun()

st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)

# ==============================================================================
# HERO SECTION DO COLABORADOR EM FOCO
# ==============================================================================
avatar_url = colab.get(
    "foto_url",
    f"https://api.dicebear.com/7.x/avataaars/svg?seed={colab['nome'].replace(' ', '')}",
)

render_html(
    f"""
<div class="colab-hero-card">
    <div class="colab-profile-left">
        <img src="{avatar_url}" class="colab-avatar" alt="{colab['nome']}"/>
        <div class="colab-info">
            <h2>{colab['nome']}</h2>
            <p><b>{colab['cargo']}</b> &bull; Squad: <span style="color:#818cf8; font-weight:600;">{colab['time']}</span></p>
            <div style="margin-top:6px; display:flex; gap:8px; flex-wrap:wrap;">
                <span class="badge-pill badge-analista">🧠 Solides: {colab['solides_profiler']['perfil_predominante']}</span>
                <span class="badge-pill" style="background:#0f172a; color:#cbd5e1; border:1px solid #475569;">🎯 PDI: {colab['qulture_rocks']['pdi_status'].split('(')[0].split('por')[0].strip()}</span>
            </div>
        </div>
    </div>
    <div class="colab-hero-stats">
        <div class="hero-stat-box">
            <div class="hero-stat-title">Reuniões / Sem</div>
            <div class="hero-stat-value" style="color: {'#f87171' if colab['jira_telemetria']['horas_reuniao_semana'] > 25 else '#38bdf8'};">
                {colab['jira_telemetria']['horas_reuniao_semana']}h
            </div>
        </div>
        <div class="hero-stat-box">
            <div class="hero-stat-title">Trocas Contexto</div>
            <div class="hero-stat-value" style="color: {'#f87171' if colab['jira_telemetria']['mudancas_de_contexto_semana'] > 20 else '#cbd5e1'};">
                {colab['jira_telemetria']['mudancas_de_contexto_semana']}/sem
            </div>
        </div>
        <div class="hero-stat-box">
            <div class="hero-stat-title">eNPS Recente</div>
            <div class="hero-stat-value" style="color: {'#f87171' if colab['qulture_rocks']['enps_recente'] < 6 else '#34d399'};">
                {colab['qulture_rocks']['enps_recente']}/10
            </div>
        </div>
        <div class="hero-stat-box">
            <div class="hero-stat-title">Energia Solides</div>
            <div class="hero-stat-value" style="color: {'#f87171' if 'Baixa' in colab['solides_profiler']['energia_atual'] else '#34d399'};">
                {colab['solides_profiler']['energia_atual'].split('(')[0].strip()}
            </div>
        </div>
    </div>
</div>
"""
)

# ==============================================================================
# MOTOR DE INFERÊNCIA DA IA (PROCESSAMENTO COM CACHE INTELIGENTE)
# ==============================================================================
if (
    "diagnostico_atual" not in st.session_state
    or st.session_state.get("colab_id") != colab["id"]
    or botao_analisar
):
    with st.spinner("🧠 Cuida AI correlacionando Solides + Jira + Qulture.Rocks..."):
        diag = analisar_colaborador(colab)
        st.session_state["diagnostico_atual"] = diag
        st.session_state["colab_id"] = colab["id"]
        st.session_state["escudo_ativado"] = False
else:
    diag = st.session_state["diagnostico_atual"]

score = diag["score_risco"]
if score >= 70:
    risk_color = "#ef4444"
    risk_bg = "rgba(239, 68, 68, 0.2)"
    risk_label = "🔴 Risco Crítico de Burnout"
elif score >= 40:
    risk_color = "#f59e0b"
    risk_bg = "rgba(245, 158, 11, 0.2)"
    risk_label = "🟡 Alerta Moderado"
else:
    risk_color = "#10b981"
    risk_bg = "rgba(16, 185, 129, 0.2)"
    risk_label = "🟢 Estável / Saudável"

# ==============================================================================
# NAVEGAÇÃO POR ABAS (SIMPLICIDADE & EFICIÊNCIA NA ORGANIZAÇÃO)
# ==============================================================================
tab_diag, tab_fontes, tab_1on1, tab_escudo = st.tabs([
    "🎯 Diagnóstico Prescritivo & IA",
    "🧬 Triangulação de Dados (Solides + Jira + Qulture)",
    "💬 Pauta de 1-on-1 & PDI",
    "🛡️ Escudo Operacional & Ação Autônoma",
])

# ------------------------------------------------------------------------------
# ABA 1: DIAGNÓSTICO PRESCRITIVO & IA
# ------------------------------------------------------------------------------
with tab_diag:
    col_d1, col_d2 = st.columns([1.15, 1.25])

    with col_d1:
        render_html(
            f"""
<div class="executive-card" style="border-top: 4px solid {risk_color};">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:12px;">
        <span style="font-weight:700; font-size:1.1rem; color:#f8fafc;">Termômetro de Sobrecarga</span>
        <span style="background:{risk_bg}; color:{risk_color}; font-weight:700; padding:4px 10px; border-radius:6px; font-size:0.85rem; border:1px solid {risk_color};">
            {risk_label}
        </span>
    </div>
    <div style="display:flex; align-items:baseline; gap:8px; margin: 10px 0 6px 0;">
        <span style="font-size:2.8rem; font-weight:800; color:{risk_color}; line-height:1;">{score}</span>
        <span style="font-size:1.2rem; color:#94a3b8; font-weight:600;">/ 100</span>
        <span style="margin-left:auto; font-size:0.85rem; color:#cbd5e1;">Status: <b>{diag['status']}</b></span>
    </div>
</div>
"""
        )
        st.progress(score / 100)
        
        render_html(
            f"""
<div class="executive-summary-box">
    <div style="font-weight:700; color:#818cf8; margin-bottom:4px; font-size:0.8rem; text-transform:uppercase;">
        📋 Síntese da Triangulação
    </div>
    {diag['resumo_analise']}
</div>

<div class="profile-impact-box">
    <div style="font-weight:700; color:#d8b4fe; margin-bottom:4px; font-size:0.8rem; text-transform:uppercase;">
        🧠 Impacto no Perfil Solides Profiler
    </div>
    {diag.get('impacto_perfil_solides', 'Rotina analisada em conformidade.')}
</div>
"""
        )

    with col_d2:
        render_html(
            """
<div class="executive-card">
    <h4 style="margin:0 0 14px 0; font-size:1.05rem; font-weight:700; color:#f8fafc;">
        ⚠️ Fatores Causais & Gatilhos Mapeados
    </h4>
</div>
"""
        )
        
        for gatilho in diag["gatilhos_detectados"]:
            if score >= 40:
                render_html(
                    f"""
<div class="trigger-item">
    <span>⚠️</span>
    <span>{gatilho}</span>
</div>
"""
                )
            else:
                render_html(
                    f"""
<div class="trigger-item-ok">
    <span>✅</span>
    <span>{gatilho}</span>
</div>
"""
                )
        
        render_html(
            f"""
<div style="margin-top:14px; padding:14px; background:#0f172a; border:1px solid #334155; border-radius:10px;">
    <div style="font-size:0.75rem; font-weight:700; color:#38bdf8; text-transform:uppercase; margin-bottom:6px;">
        ⚡ Ação Prescritiva Imediata Sugerida
    </div>
    <div style="font-size:0.9rem; color:#f8fafc; font-weight:500;">
        {diag['acao_autonoma_prescritiva']}
    </div>
</div>
"""
        )

# ------------------------------------------------------------------------------
# ABA 2: TRIANGULAÇÃO DE DADOS (SOLIDES + JIRA + QULTURE.ROCKS)
# ------------------------------------------------------------------------------
with tab_fontes:
    col_s, col_j, col_q = st.columns(3)

    # 1. SOLIDES PROFILER
    with col_s:
        energia_txt = colab['solides_profiler']['energia_atual']
        energia_val = 0.25 if 'Baixa' in energia_txt else (0.6 if 'Média' in energia_txt else 0.95)
        render_html(
            f"""
<div class="card-solides">
    <h3>🧠 Solides Profiler</h3>
    
    <div class="metric-row">
        <span class="metric-label">Perfil Predominante</span>
        <span class="metric-val" style="color:#c4b5fd;">{colab['solides_profiler']['perfil_predominante']}</span>
    </div>
    <div class="metric-row">
        <span class="metric-label">Nível de Exigência</span>
        <span class="metric-val">{colab['solides_profiler']['nivel_exigencia_pessoal']}</span>
    </div>
    <div class="metric-row">
        <span class="metric-label">Energia Atual</span>
        <span class="metric-val" style="color: {'#f87171' if 'Baixa' in energia_txt else '#34d399'};">
            {energia_txt}
        </span>
    </div>
    
    <div style="margin: 14px 0 6px 0; font-size:0.75rem; font-weight:600; color:#94a3b8; text-transform:uppercase;">Nível de Reserva de Energia:</div>
</div>
"""
        )
        st.progress(energia_val)
        render_html(
            f"""
<div style="margin-top:10px; padding:12px; background:#0f172a; border:1px solid #334155; border-radius:8px; font-size:0.82rem; color:#e9d5ff; line-height:1.4;">
    <b>Vulnerabilidade / Estilo:</b><br>{colab['solides_profiler']['caracteristicas_chave']}
</div>
"""
        )

    # 2. JIRA & TELEMETRIA OPERACIONAL
    with col_j:
        hrs_reuniao = colab['jira_telemetria']['horas_reuniao_semana']
        pct_horas = min(hrs_reuniao / 40.0, 1.0)
        render_html(
            f"""
<div class="card-jira">
    <h3>⚡ Jira & Telemetria</h3>
    
    <div class="metric-row">
        <span class="metric-label">Reuniões / Semana</span>
        <span class="metric-val" style="color: {'#f87171' if hrs_reuniao > 25 else '#38bdf8'};">{hrs_reuniao}h</span>
    </div>
    <div class="metric-row">
        <span class="metric-label">Cards Atrasados vs Abertos</span>
        <span class="metric-val">{colab['jira_telemetria']['cards_atrasados']} / {colab['jira_telemetria']['cards_em_aberto']}</span>
    </div>
    <div class="metric-row">
        <span class="metric-label">Trocas de Contexto</span>
        <span class="metric-val">{colab['jira_telemetria']['mudancas_de_contexto_semana']} / sem</span>
    </div>
    <div class="metric-row">
        <span class="metric-label">Atividade Fora do Horário</span>
        <span class="metric-val" style="color: {'#f87171' if colab['jira_telemetria']['commits_fora_do_horario_pct'] > 20 else '#cbd5e1'};">
            {colab['jira_telemetria']['commits_fora_do_horario_pct']}%
        </span>
    </div>
    
    <div style="margin: 14px 0 6px 0; font-size:0.75rem; font-weight:600; color:#94a3b8; text-transform:uppercase;">Consumo da Jornada em Reuniões:</div>
</div>
"""
        )
        st.progress(pct_horas)
        render_html(
            f"""
<div style="margin-top:10px; padding:12px; background:#0f172a; border:1px solid #334155; border-radius:8px; font-size:0.82rem; color:#7dd3fc; line-height:1.4;">
    <b>Dias Consecutivos Sem Folga:</b> {colab['jira_telemetria'].get('dias_consecutivos_sem_folga', 0)} dias
</div>
"""
        )

    # 3. QULTURE.ROCKS (GOVERNANÇA & SENTIMENTO)
    with col_q:
        pdi_txt = colab['qulture_rocks']['pdi_status']
        pdi_val = 0.15 if 'Paralisado' in pdi_txt else (0.65 if '65%' in pdi_txt else 0.85)
        render_html(
            f"""
<div class="card-qulture">
    <h3>🎯 Qulture.Rocks</h3>
    
    <div class="metric-row">
        <span class="metric-label">eNPS Recente</span>
        <span class="metric-val" style="color: {'#f87171' if colab['qulture_rocks']['enps_recente'] < 6 else '#34d399'};">
            {colab['qulture_rocks']['enps_recente']} / 10
        </span>
    </div>
    <div class="metric-row">
        <span class="metric-label">Desempenho Geral</span>
        <span class="metric-val" style="font-size:0.82rem;">{colab['qulture_rocks']['ultima_avaliacao_desempenho'].split(',')[0]}</span>
    </div>
    
    <div style="margin: 14px 0 6px 0; font-size:0.75rem; font-weight:600; color:#94a3b8; text-transform:uppercase;">Evolução do PDI:</div>
</div>
"""
        )
        st.progress(pdi_val)
        render_html(
            f"""
<div style="font-size:0.8rem; color:#94a3b8; margin: 6px 0 8px 0;"><b>Status PDI:</b> {pdi_txt}</div>
<div class="pulse-quote-box">
    <b>Último Pulso:</b><br>"{colab['qulture_rocks']['resumo_ultimo_pulso']}"
</div>
"""
        )

# ------------------------------------------------------------------------------
# ABA 3: PAUTA DE 1-ON-1 & PDI (QULTURE.ROCKS READY)
# ------------------------------------------------------------------------------
with tab_1on1:
    col_1on1_esq, col_1on1_dir = st.columns([1.3, 1])

    with col_1on1_esq:
        render_html(
            """
<div class="executive-card">
    <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:12px;">
        <h3 style="margin:0; font-size:1.15rem; font-weight:700; color:#f8fafc;">
            📋 Pauta Calibrada para o Próximo 1-on-1
        </h3>
        <span class="badge-pill" style="background:#064e3b; color:#a7f3d0; border:1px solid #059669;">
            Solides Profiler Calibrated
        </span>
    </div>
    <p style="color:#94a3b8; font-size:0.88rem; margin-top:0;">
        Perguntas estratégicas formuladas pelo modelo para destravar gargalos reais sem causar atrito comportamental:
    </p>
</div>
"""
        )

        for i, pergunta in enumerate(diag["pauta_1on1_sugerida"], start=1):
            render_html(
                f"""
<div class="one-on-one-question">
    <div class="one-on-one-num">Tópico Estratégico {i}</div>
    <div class="one-on-one-text">{pergunta}</div>
</div>
"""
            )

        # Dica personalizada de acordo com o perfil
        perfil_liderado = colab['solides_profiler']['perfil_predominante']
        if 'Analista' in perfil_liderado:
            dica_gestor = "Perfis <b>Analistas</b> valorizam compromissos claros de corte de interrupções e tempo protegido para entrega técnica com excelência. Evite perguntas genéricas; valide ações objetivas e prazos realistas."
        elif 'Comunicador' in perfil_liderado:
            dica_gestor = "Perfis <b>Comunicadores</b> valorizam escuta ativa, reconhecimento interpessoal e destravamento de barreiras com stakeholders. Ajude a filtrar o excesso de compromissos assumidos."
        elif 'Planejador' in perfil_liderado:
            dica_gestor = "Perfis <b>Planejadores</b> valorizam estabilidade, previsibilidade de escopo e ritmo constante. Evite mudanças bruscas de prioridade sem aviso prévio."
        else:
            dica_gestor = "Perfis <b>Executores</b> valorizam autonomia, metas agressivas e velocidade. Foque em destravar dependências que impeçam o avanço imediato."

        render_html(
            f"""
<div style="background:#0f172a; border:1px solid #334155; border-radius:8px; padding:12px; font-size:0.85rem; color:#cbd5e1; margin-top:12px;">
    💡 <b>Guia do Gestor:</b> {dica_gestor}
</div>
"""
        )

    with col_1on1_dir:
        render_html(
            """
<div class="executive-card">
    <h3 style="margin:0 0 14px 0; font-size:1.1rem; font-weight:700; color:#f8fafc;">
        ⏳ Histórico Recente de 1-on-1s (Qulture.Rocks)
    </h3>
</div>
"""
        )

        for nota in colab["qulture_rocks"]["historico_1on1s"]:
            partes = nota.split(":", 1)
            sem = partes[0].strip() if len(partes) > 1 else "Registro"
            txt = partes[1].strip() if len(partes) > 1 else nota
            render_html(
                f"""
<div class="timeline-item">
    <div class="timeline-date">{sem}</div>
    <div class="timeline-content">{txt}</div>
</div>
"""
            )

# ------------------------------------------------------------------------------
# ABA 4: ESCUDO OPERACIONAL & AÇÃO AUTÔNOMA (OUSADIA INOVATHON)
# ------------------------------------------------------------------------------
with tab_escudo:
    render_html(
        f"""
<div class="shield-banner">
    <h4>🛡️ Intervenção Prescritiva Autônoma do PulseGuard</h4>
    <div class="shield-text">
        <b>Ação do Sistema:</b> {diag['acao_autonoma_prescritiva']}
    </div>
    
    <div style="font-size:0.8rem; font-weight:700; color:#94a3b8; text-transform:uppercase; margin-top:16px;">
        Sincronizações Autônomas Programadas no Ecossistema Corporativo:
    </div>
    <div class="shield-action-grid">
        <div class="shield-action-item">
            <b>🔒 Jira Software</b><br>Congelamento de novos cards e rebalanceamento de backlog.
        </div>
        <div class="shield-action-item">
            <b>📅 Google Calendar</b><br>Bloqueio automático de 4h diárias de "Foco Total Protegido".
        </div>
        <div class="shield-action-item">
            <b>🎯 Qulture.Rocks</b><br>Pauta de 1-on-1 injetada na agenda do gestor com alertas de PDI.
        </div>
        <div class="shield-action-item">
            <b>👥 BP / Gestão de Pessoas</b><br>Notificação preditiva para blindagem de retenção de talentos.
        </div>
    </div>
</div>
"""
    )

    st.write("")
    col_btn, col_msg = st.columns([1, 1.8])

    with col_btn:
        if not st.session_state.get("escudo_ativado"):
            if st.button(
                "🚀 Executar Blindagem Operacional Agora",
                type="primary",
                use_container_width=True,
            ):
                st.session_state["escudo_ativado"] = True
                st.rerun()
        else:
            st.button(
                "✅ Blindagem Ativa e Monitorando",
                disabled=True,
                use_container_width=True,
            )
            if st.button("Restaurar Parâmetros Padrão", use_container_width=True):
                st.session_state["escudo_ativado"] = False
                st.rerun()

    with col_msg:
        if st.session_state.get("escudo_ativado"):
            st.success(
                f"🎉 **Protocolo de Blindagem Operacional Executado com Sucesso para {colab['nome'].split()[0]}!**\n\n"
                "• **Jira:** Cards congelados e dependências redistribuídas no time.\n"
                "• **Calendar:** 16 horas de foco reservadas para os próximos 4 dias úteis.\n"
                "• **Qulture.Rocks:** Pauta de 1-on-1 sincronizada na sessão do líder com prioridade máxima."
            )
        else:
            st.info(
                "ℹ️ **Modo de Prontidão:** Clique no botão ao lado para acionar a intervenção nos conectores corporativos integrados."
            )

# ==============================================================================
# FOOTER INOVATHON
# ==============================================================================
st.markdown("---")
render_html(
    """
<div style="display:flex; justify-content:space-between; align-items:center; font-size:0.8rem; color:#94a3b8; padding:8px 0;">
    <span>Cuida AI &bull; Inovathon 2026 &bull; Pilar Ousadia em Inteligência Artificial</span>
    <span>Solides Profiler &bull; Jira Software &bull; Qulture.Rocks Integrados</span>
</div>
"""
)