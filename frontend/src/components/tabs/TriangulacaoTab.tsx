import type { Colaborador } from "../../types";

function energiaValor(texto: string) {
  if (texto.includes("Baixa")) return 25;
  if (texto.includes("Média")) return 60;
  return 95;
}

function pdiValor(status: string) {
  if (status.includes("Paralisado")) return 15;
  if (status.includes("65%")) return 65;
  return 85;
}

export default function TriangulacaoTab({ colab }: { colab: Colaborador }) {
  const { solides_profiler: solides, jira_telemetria: jira, qulture_rocks: qulture } = colab;
  const energiaPct = energiaValor(solides.energia_atual);
  const horasPct = Math.min((jira.horas_reuniao_semana / 40) * 100, 100);
  const pdiPct = pdiValor(qulture.pdi_status);

  return (
    <div className="grid-3">
      <div className="card card-accent-solides">
        <h3>🧠 Solides Profiler</h3>
        <div className="metric-row">
          <span className="metric-label">Perfil Predominante</span>
          <span className="metric-val" style={{ color: "var(--color-brand-strong)" }}>
            {solides.perfil_predominante}
          </span>
        </div>
        <div className="metric-row">
          <span className="metric-label">Nível de Exigência</span>
          <span className="metric-val">{solides.nivel_exigencia_pessoal}</span>
        </div>
        <div className="metric-row">
          <span className="metric-label">Energia Atual</span>
          <span
            className="metric-val"
            style={{ color: solides.energia_atual.includes("Baixa") ? "var(--color-danger)" : "var(--color-brand)" }}
          >
            {solides.energia_atual}
          </span>
        </div>
        <div className="progress-caption">Nível de Reserva de Energia:</div>
        <div className="progress-track">
          <div className="progress-fill" style={{ width: `${energiaPct}%` }} />
        </div>
        <div className="info-box info-box-brand" style={{ marginTop: 12 }}>
          <b>Vulnerabilidade / Estilo:</b>
          <br />
          {solides.caracteristicas_chave}
        </div>
      </div>

      <div className="card card-accent-jira">
        <h3>⚡ Jira &amp; Telemetria</h3>
        <div className="metric-row">
          <span className="metric-label">Reuniões / Semana</span>
          <span className="metric-val" style={{ color: jira.horas_reuniao_semana > 25 ? "var(--color-danger)" : "var(--color-jira)" }}>
            {jira.horas_reuniao_semana}h
          </span>
        </div>
        <div className="metric-row">
          <span className="metric-label">Cards Atrasados vs Abertos</span>
          <span className="metric-val">
            {jira.cards_atrasados} / {jira.cards_em_aberto}
          </span>
        </div>
        <div className="metric-row">
          <span className="metric-label">Trocas de Contexto</span>
          <span className="metric-val">{jira.mudancas_de_contexto_semana} / sem</span>
        </div>
        <div className="metric-row">
          <span className="metric-label">Atividade Fora do Horário</span>
          <span className="metric-val" style={{ color: jira.commits_fora_do_horario_pct > 20 ? "var(--color-danger)" : "var(--color-text)" }}>
            {jira.commits_fora_do_horario_pct}%
          </span>
        </div>
        <div className="progress-caption">Consumo da Jornada em Reuniões:</div>
        <div className="progress-track">
          <div className="progress-fill" style={{ width: `${horasPct}%`, background: "var(--color-jira)" }} />
        </div>
        <div className="info-box info-box-jira" style={{ marginTop: 12 }}>
          <b>Dias Consecutivos Sem Folga:</b> {jira.dias_consecutivos_sem_folga} dias
        </div>
      </div>

      <div className="card card-accent-qulture">
        <h3>🎯 Qulture.Rocks</h3>
        <div className="metric-row">
          <span className="metric-label">eNPS Recente</span>
          <span className="metric-val" style={{ color: qulture.enps_recente < 6 ? "var(--color-danger)" : "var(--color-brand)" }}>
            {qulture.enps_recente} / 10
          </span>
        </div>
        <div className="metric-row">
          <span className="metric-label">Desempenho Geral</span>
          <span className="metric-val" style={{ fontSize: "0.82rem" }}>
            {qulture.ultima_avaliacao_desempenho.split(",")[0]}
          </span>
        </div>
        <div className="progress-caption">Evolução do PDI:</div>
        <div className="progress-track">
          <div className="progress-fill" style={{ width: `${pdiPct}%`, background: "var(--color-qulture)" }} />
        </div>
        <div style={{ fontSize: "0.8rem", color: "var(--color-text-soft)", margin: "10px 0 8px" }}>
          <b>Status PDI:</b> {qulture.pdi_status}
        </div>
        <div className="info-box info-box-quote">
          <b>Último Pulso:</b>
          <br />"{qulture.resumo_ultimo_pulso}"
        </div>
      </div>
    </div>
  );
}
