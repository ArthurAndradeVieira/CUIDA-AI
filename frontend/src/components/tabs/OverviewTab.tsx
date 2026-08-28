import { AlertOctagon, AlertTriangle, CheckCircle2, Clock, Smile, Users } from "lucide-react";
import type { Colaborador } from "../../types";
import { riskLevelFromScenario } from "../RiskBadge";

const REUNIAO_LIMIAR = 25;
const ENPS_LIMIAR = 6;
const REUNIAO_ESCALA_MAX = 40;

const RISCO_META = {
  critico: { label: "Risco Crítico", color: "var(--status-critical)", Icon: AlertOctagon },
  alerta: { label: "Alerta Moderado", color: "var(--status-warning)", Icon: AlertTriangle },
  estavel: { label: "Estável", color: "var(--status-good)", Icon: CheckCircle2 },
} as const;

function media(valores: number[]) {
  return valores.reduce((soma, v) => soma + v, 0) / valores.length;
}

export default function OverviewTab({ colaboradores }: { colaboradores: Colaborador[] }) {
  const niveis = colaboradores.map((c) => riskLevelFromScenario(c.cenario_esperado));
  const contagem = {
    critico: niveis.filter((n) => n === "critico").length,
    alerta: niveis.filter((n) => n === "alerta").length,
    estavel: niveis.filter((n) => n === "estavel").length,
  };
  const total = colaboradores.length;
  const emRisco = contagem.critico + contagem.alerta;
  const mediaReunioes = media(colaboradores.map((c) => c.jira_telemetria.horas_reuniao_semana));
  const mediaEnps = media(colaboradores.map((c) => c.qulture_rocks.enps_recente));

  return (
    <div className="overview-grid">
      <section>
        <h3 className="section-title">Resumo do Time</h3>
        <div className="kpi-row">
          <div className="kpi-tile">
            <div className="kpi-icon">
              <Users size={18} />
            </div>
            <div>
              <div className="kpi-label">Colaboradores</div>
              <div className="kpi-value">{total}</div>
            </div>
          </div>
          <div className="kpi-tile">
            <div className="kpi-icon">
              <Clock size={18} />
            </div>
            <div>
              <div className="kpi-label">Reuniões médias / sem</div>
              <div className="kpi-value">{mediaReunioes.toFixed(1)}h</div>
            </div>
          </div>
          <div className="kpi-tile">
            <div className="kpi-icon">
              <Smile size={18} />
            </div>
            <div>
              <div className="kpi-label">eNPS médio</div>
              <div className="kpi-value">{mediaEnps.toFixed(1)}/10</div>
            </div>
          </div>
          <div className="kpi-tile">
            <div className="kpi-icon critical">
              <AlertTriangle size={18} />
            </div>
            <div>
              <div className="kpi-label">Em risco (alerta + crítico)</div>
              <div className="kpi-value">
                {emRisco} de {total}
              </div>
            </div>
          </div>
        </div>
      </section>

      <section className="card">
        <h3 className="card-title" style={{ margin: 0 }}>
          Distribuição de Risco da Squad
        </h3>
        <p className="card-subtitle">Com base no cenário mapeado para cada colaborador</p>

        <div className="stacked-bar" title={`${contagem.critico} crítico · ${contagem.alerta} alerta · ${contagem.estavel} estável`}>
          {(["critico", "alerta", "estavel"] as const).map((nivel) =>
            contagem[nivel] > 0 ? (
              <div
                key={nivel}
                className="stacked-bar-segment"
                style={{ width: `${(contagem[nivel] / total) * 100}%`, background: RISCO_META[nivel].color }}
              />
            ) : null
          )}
        </div>

        <div className="stacked-bar-legend">
          {(["critico", "alerta", "estavel"] as const).map((nivel) => {
            const meta = RISCO_META[nivel];
            return (
              <span className="legend-item" key={nivel}>
                <meta.Icon size={14} className="icon-inline" style={{ color: meta.color }} />
                {meta.label}: <b style={{ color: "var(--color-text)" }}>{contagem[nivel]}</b>
              </span>
            );
          })}
        </div>
      </section>

      <section className="card">
        <h3 className="card-title" style={{ margin: 0 }}>
          Reuniões por Colaborador
        </h3>
        <p className="card-subtitle">Horas semanais em reunião (referência: {REUNIAO_ESCALA_MAX}h/semana)</p>

        <div className="bar-list">
          {colaboradores.map((c) => {
            const horas = c.jira_telemetria.horas_reuniao_semana;
            const acimaDoLimiar = horas > REUNIAO_LIMIAR;
            const pct = Math.min((horas / REUNIAO_ESCALA_MAX) * 100, 100);
            return (
              <div className="bar-list-row" key={c.id} title={`${c.nome}: ${horas}h de reunião por semana`}>
                <span className="bar-list-label">{c.nome.split(" ")[0]}</span>
                <div className="bar-list-track">
                  <div className="bar-list-fill" style={{ width: `${pct}%` }} />
                </div>
                <span className="bar-list-value">{horas}h</span>
                {acimaDoLimiar && (
                  <span className="bar-list-flag">
                    <AlertTriangle size={13} className="icon-inline" /> acima do recomendado
                  </span>
                )}
              </div>
            );
          })}
        </div>
      </section>

      <section className="card">
        <h3 className="card-title" style={{ margin: 0 }}>
          eNPS por Colaborador
        </h3>
        <p className="card-subtitle">Nota recente de sentimento (escala 0–10)</p>

        <div className="bar-list">
          {colaboradores.map((c) => {
            const enps = c.qulture_rocks.enps_recente;
            const abaixoDoIdeal = enps < ENPS_LIMIAR;
            const pct = (enps / 10) * 100;
            return (
              <div className="bar-list-row" key={c.id} title={`${c.nome}: eNPS ${enps}/10`}>
                <span className="bar-list-label">{c.nome.split(" ")[0]}</span>
                <div className="bar-list-track">
                  <div className="bar-list-fill" style={{ width: `${pct}%` }} />
                </div>
                <span className="bar-list-value">{enps}/10</span>
                {abaixoDoIdeal && (
                  <span className="bar-list-flag">
                    <AlertTriangle size={13} className="icon-inline" /> abaixo do ideal
                  </span>
                )}
              </div>
            );
          })}
        </div>
      </section>
    </div>
  );
}
