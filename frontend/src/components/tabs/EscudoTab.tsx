import type { Colaborador, Diagnostico } from "../../types";

interface EscudoTabProps {
  colab: Colaborador;
  diag: Diagnostico;
  ativado: boolean;
  onAtivar: () => void;
  onRestaurar: () => void;
}

export default function EscudoTab({ colab, diag, ativado, onAtivar, onRestaurar }: EscudoTabProps) {
  const primeiroNome = colab.nome.split(" ")[0];

  return (
    <div>
      <div className="shield-banner">
        <h4>🛡️ Intervenção Prescritiva Autônoma do Cuida AI</h4>
        <div className="shield-text">
          <b>Ação do Sistema:</b> {diag.acao_autonoma_prescritiva}
        </div>

        <div className="shield-section-label">Sincronizações Autônomas Programadas no Ecossistema Corporativo:</div>
        <div className="shield-action-grid">
          <div className="shield-action-item">
            <b>🔒 Jira Software</b>
            <br />
            Congelamento de novos cards e rebalanceamento de backlog.
          </div>
          <div className="shield-action-item">
            <b>📅 Google Calendar</b>
            <br />
            Bloqueio automático de 4h diárias de "Foco Total Protegido".
          </div>
          <div className="shield-action-item">
            <b>🎯 Qulture.Rocks</b>
            <br />
            Pauta de 1-on-1 injetada na agenda do gestor com alertas de PDI.
          </div>
          <div className="shield-action-item">
            <b>👥 BP / Gestão de Pessoas</b>
            <br />
            Notificação preditiva para blindagem de retenção de talentos.
          </div>
        </div>
      </div>

      <div className="shield-controls">
        <div>
          {!ativado ? (
            <button className="btn btn-primary btn-block" onClick={onAtivar}>
              🚀 Executar Blindagem Operacional Agora
            </button>
          ) : (
            <>
              <button className="btn btn-block" disabled>
                ✅ Blindagem Ativa e Monitorando
              </button>
              <button className="btn btn-block" style={{ marginTop: 10 }} onClick={onRestaurar}>
                Restaurar Parâmetros Padrão
              </button>
            </>
          )}
        </div>

        <div>
          {ativado ? (
            <div className="alert-box alert-success">
              🎉 <b>Protocolo de Blindagem Operacional Executado com Sucesso para {primeiroNome}!</b>
              <ul>
                <li>
                  <b>Jira:</b> Cards congelados e dependências redistribuídas no time.
                </li>
                <li>
                  <b>Calendar:</b> 16 horas de foco reservadas para os próximos 4 dias úteis.
                </li>
                <li>
                  <b>Qulture.Rocks:</b> Pauta de 1-on-1 sincronizada na sessão do líder com prioridade máxima.
                </li>
              </ul>
            </div>
          ) : (
            <div className="alert-box alert-info">
              ℹ️ <b>Modo de Prontidão:</b> Clique no botão ao lado para acionar a intervenção nos conectores
              corporativos integrados.
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
