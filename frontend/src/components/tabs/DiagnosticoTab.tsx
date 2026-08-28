import type { Diagnostico } from "../../types";
import RiskBadge, { riskLevelFromScore } from "../RiskBadge";

const RISK_LABELS = {
  critico: "🔴 Risco Crítico de Burnout",
  alerta: "🟡 Alerta Moderado",
  estavel: "🟢 Estável / Saudável",
};

const RISK_COLORS = {
  critico: "var(--color-danger)",
  alerta: "var(--color-warning)",
  estavel: "var(--color-success)",
};

export default function DiagnosticoTab({ diag }: { diag: Diagnostico }) {
  const level = riskLevelFromScore(diag.score_risco);
  const riskColor = RISK_COLORS[level];

  return (
    <div className="grid-2">
      <div>
        <div className="card" style={{ borderTop: `4px solid ${riskColor}`, marginBottom: 16 }}>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
            <span style={{ fontWeight: 700, fontSize: "1.1rem" }}>Termômetro de Sobrecarga</span>
            <RiskBadge level={level} label={RISK_LABELS[level]} />
          </div>
          <div className="diagnostic-score">
            <span className="value" style={{ color: riskColor }}>
              {diag.score_risco}
            </span>
            <span className="max">/ 100</span>
            <span className="status">
              Status: <b style={{ color: "var(--color-text)" }}>{diag.status}</b>
            </span>
          </div>
          <div className="progress-track">
            <div className="progress-fill" style={{ width: `${diag.score_risco}%`, background: riskColor }} />
          </div>
        </div>

        <div className="info-box info-box-brand" style={{ marginBottom: 14 }}>
          <div className="info-box-label" style={{ color: "var(--color-brand-strong)" }}>
            📋 Síntese da Triangulação
          </div>
          {diag.resumo_analise}
        </div>

        <div className="info-box" style={{ background: "#f0fdf4", borderLeft: "4px solid var(--color-qulture)", color: "#065f46" }}>
          <div className="info-box-label" style={{ color: "#065f46" }}>
            🧠 Impacto no Perfil Solides Profiler
          </div>
          {diag.impacto_perfil_solides}
        </div>
      </div>

      <div>
        <div className="card" style={{ marginBottom: 16 }}>
          <h4 style={{ margin: 0 }}>⚠️ Fatores Causais &amp; Gatilhos Mapeados</h4>
        </div>

        {diag.gatilhos_detectados.map((gatilho, i) => (
          <div key={i} className={`trigger-item ${diag.score_risco >= 40 ? "alert" : "ok"}`}>
            <span>{diag.score_risco >= 40 ? "⚠️" : "✅"}</span>
            <span>{gatilho}</span>
          </div>
        ))}

        <div className="action-box">
          <div className="info-box-label" style={{ color: "var(--color-brand-strong)" }}>
            ⚡ Ação Prescritiva Imediata Sugerida
          </div>
          <div style={{ fontSize: "0.9rem", fontWeight: 600, color: "#064e3b" }}>
            {diag.acao_autonoma_prescritiva}
          </div>
        </div>
      </div>
    </div>
  );
}
