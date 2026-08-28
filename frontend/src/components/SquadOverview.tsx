import { Users } from "lucide-react";
import type { Colaborador } from "../types";
import RiskBadge, { riskLevelFromScenario } from "./RiskBadge";

interface SquadOverviewProps {
  colaboradores: Colaborador[];
  selecionadoId: string;
  onSelecionar: (id: string) => void;
}

export default function SquadOverview({ colaboradores, selecionadoId, onSelecionar }: SquadOverviewProps) {
  return (
    <section>
      <h3 className="section-title" style={{ display: "flex", alignItems: "center", gap: 8 }}>
        <Users size={18} className="icon-inline" /> Panorama da Squad (Visão Geral de Risco)
      </h3>
      <div className="squad-grid">
        {colaboradores.map((c) => {
          const perfilResumido = c.solides_profiler.perfil_predominante.split("/")[0].trim();
          return (
            <button
              key={c.id}
              className={`squad-card${c.id === selecionadoId ? " active" : ""}`}
              onClick={() => onSelecionar(c.id)}
            >
              <div className="squad-card-top">
                <span className="squad-card-name">{c.nome}</span>
                <RiskBadge level={riskLevelFromScenario(c.cenario_esperado)} />
              </div>
              <div className="squad-card-role">{c.cargo}</div>
              <div className="squad-card-meta">
                <span>
                  <b>Perfil:</b> {perfilResumido}
                </span>
                <span>
                  <b>Reuniões:</b> {c.jira_telemetria.horas_reuniao_semana}h
                </span>
              </div>
            </button>
          );
        })}
      </div>
    </section>
  );
}
