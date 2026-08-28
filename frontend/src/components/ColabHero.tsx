import type { Colaborador } from "../types";

function statColor(alert: boolean) {
  return alert ? "var(--color-danger)" : "var(--color-brand-strong)";
}

export default function ColabHero({ colab }: { colab: Colaborador }) {
  const avatarUrl =
    colab.foto_url ??
    `https://api.dicebear.com/7.x/avataaars/svg?seed=${encodeURIComponent(colab.nome.replace(" ", ""))}`;

  const { jira_telemetria: jira, qulture_rocks: qulture, solides_profiler: solides } = colab;
  const pdiResumo = qulture.pdi_status.split("(")[0].split("por")[0].trim();

  return (
    <div className="colab-hero">
      <div className="colab-hero-left">
        <img src={avatarUrl} className="colab-avatar" alt={colab.nome} />
        <div className="colab-info">
          <h2>{colab.nome}</h2>
          <p>
            <b>{colab.cargo}</b> • Squad: <span style={{ color: "var(--color-brand)", fontWeight: 600 }}>{colab.time}</span>
          </p>
          <div className="colab-badges">
            <span className="badge-pill">🧠 Solides: {solides.perfil_predominante}</span>
            <span className="badge-pill badge-neutral">🎯 PDI: {pdiResumo}</span>
          </div>
        </div>
      </div>

      <div className="colab-hero-stats">
        <div className="hero-stat-box">
          <div className="hero-stat-title">Reuniões / Sem</div>
          <div className="hero-stat-value" style={{ color: statColor(jira.horas_reuniao_semana > 25) }}>
            {jira.horas_reuniao_semana}h
          </div>
        </div>
        <div className="hero-stat-box">
          <div className="hero-stat-title">Trocas Contexto</div>
          <div className="hero-stat-value" style={{ color: statColor(jira.mudancas_de_contexto_semana > 20) }}>
            {jira.mudancas_de_contexto_semana}/sem
          </div>
        </div>
        <div className="hero-stat-box">
          <div className="hero-stat-title">eNPS Recente</div>
          <div className="hero-stat-value" style={{ color: statColor(qulture.enps_recente < 6) }}>
            {qulture.enps_recente}/10
          </div>
        </div>
        <div className="hero-stat-box">
          <div className="hero-stat-title">Energia Solides</div>
          <div className="hero-stat-value" style={{ color: statColor(solides.energia_atual.includes("Baixa")) }}>
            {solides.energia_atual.split("(")[0].trim()}
          </div>
        </div>
      </div>
    </div>
  );
}
