import { ClipboardList, History, Lightbulb } from "lucide-react";
import type { Colaborador, Diagnostico } from "../../types";

function dicaGestor(perfil: string) {
  if (perfil.includes("Analista")) {
    return (
      <>
        Perfis <b>Analistas</b> valorizam compromissos claros de corte de interrupções e tempo protegido para
        entrega técnica com excelência. Evite perguntas genéricas; valide ações objetivas e prazos realistas.
      </>
    );
  }
  if (perfil.includes("Comunicador")) {
    return (
      <>
        Perfis <b>Comunicadores</b> valorizam escuta ativa, reconhecimento interpessoal e destravamento de
        barreiras com stakeholders. Ajude a filtrar o excesso de compromissos assumidos.
      </>
    );
  }
  if (perfil.includes("Planejador")) {
    return (
      <>
        Perfis <b>Planejadores</b> valorizam estabilidade, previsibilidade de escopo e ritmo constante. Evite
        mudanças bruscas de prioridade sem aviso prévio.
      </>
    );
  }
  return (
    <>
      Perfis <b>Executores</b> valorizam autonomia, metas agressivas e velocidade. Foque em destravar
      dependências que impeçam o avanço imediato.
    </>
  );
}

export default function OneOnOneTab({ colab, diag }: { colab: Colaborador; diag: Diagnostico }) {
  return (
    <div className="grid-2-alt">
      <div>
        <div className="card" style={{ marginBottom: 16 }}>
          <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between" }}>
            <h3 style={{ margin: 0, display: "flex", alignItems: "center", gap: 8 }}>
              <ClipboardList size={18} className="icon-inline" /> Pauta Calibrada para o Próximo 1-on-1
            </h3>
            <span className="badge-pill">Solides Profiler Calibrated</span>
          </div>
          <p style={{ color: "var(--color-text-soft)", fontSize: "0.88rem", marginTop: 8, marginBottom: 0 }}>
            Perguntas estratégicas formuladas pelo modelo para destravar gargalos reais sem causar atrito
            comportamental:
          </p>
        </div>

        {diag.pauta_1on1_sugerida.map((pergunta, i) => (
          <div key={i} className="one-on-one-question">
            <div className="one-on-one-num">Tópico Estratégico {i + 1}</div>
            <div className="one-on-one-text">{pergunta}</div>
          </div>
        ))}

        <div className="manager-tip" style={{ display: "flex", gap: 8 }}>
          <Lightbulb size={16} className="icon-inline" style={{ marginTop: 2 }} />
          <span>
            <b>Guia do Gestor:</b> {dicaGestor(colab.solides_profiler.perfil_predominante)}
          </span>
        </div>
      </div>

      <div>
        <div className="card" style={{ marginBottom: 16 }}>
          <h3 style={{ margin: 0, display: "flex", alignItems: "center", gap: 8 }}>
            <History size={18} className="icon-inline" /> Histórico Recente de 1-on-1s (Qulture.Rocks)
          </h3>
        </div>

        {colab.qulture_rocks.historico_1on1s.map((nota, i) => {
          const [primeira, ...resto] = nota.split(":");
          const temSeparador = resto.length > 0;
          const sem = temSeparador ? primeira.trim() : "Registro";
          const txt = temSeparador ? resto.join(":").trim() : nota;
          return (
            <div key={i} className="timeline-item">
              <div className="timeline-date">{sem}</div>
              <div className="timeline-content">{txt}</div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
