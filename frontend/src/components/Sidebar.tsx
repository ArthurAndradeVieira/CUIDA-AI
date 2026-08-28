import { Bot, Brain, Circle, Dna, Plug, Target, User, Zap } from "lucide-react";
import type { Colaborador } from "../types";
import logo from "../assets/logo.png";

interface SidebarProps {
  colaboradores: Colaborador[];
  selecionado: Colaborador;
  onSelecionar: (id: string) => void;
  onRecalcular: () => void;
  carregando: boolean;
}

const CONECTORES = [
  { Icon: Brain, nome: "Solides Profiler", status: "Ativo" },
  { Icon: Zap, nome: "Jira & Calendar", status: "Sincronizado" },
  { Icon: Target, nome: "Qulture.Rocks", status: "Conectado" },
  { Icon: Bot, nome: "Gemini 2.5 Flash", status: "Online" },
];

export default function Sidebar({
  colaboradores,
  selecionado,
  onSelecionar,
  onRecalcular,
  carregando,
}: SidebarProps) {
  return (
    <aside className="sidebar">
      <div className="sidebar-brand">
        <img src={logo} alt="Cuida AI" />
        <div>
          <h1>Cuida AI</h1>
          <span>Inovathon 2026</span>
        </div>
      </div>
      <p className="sidebar-caption">Triangulação de Solides + Jira + Qulture.Rocks</p>

      <hr />

      <div>
        <div className="sidebar-section-title">
          <User size={14} className="icon-inline" /> Seleção de Colaborador
        </div>
        <select
          className="select-input"
          value={selecionado.id}
          onChange={(e) => onSelecionar(e.target.value)}
        >
          {colaboradores.map((c) => (
            <option key={c.id} value={c.id}>
              {c.nome}
            </option>
          ))}
        </select>

        <div className="sidebar-profile-card" style={{ marginTop: 10 }}>
          <div className="sidebar-label">Cargo &amp; Squad</div>
          <div className="role">{selecionado.cargo}</div>
          <div className="squad">{selecionado.time}</div>
          <div className="sidebar-label">Perfil Comportamental</div>
          <span className="badge-pill" style={{ marginTop: 4 }}>
            <Dna size={13} className="icon-inline" /> {selecionado.solides_profiler.perfil_predominante}
          </span>
        </div>
      </div>

      <hr />

      <div>
        <div className="sidebar-section-title">
          <Plug size={14} className="icon-inline" /> Conectores Ativos
        </div>
        <div className="connector-list">
          {CONECTORES.map((c) => (
            <div className="connector-row" key={c.nome}>
              <span style={{ display: "inline-flex", alignItems: "center", gap: 6 }}>
                <c.Icon size={14} className="icon-inline" /> <b>{c.nome}</b>
              </span>
              <span className="connector-status">
                <Circle size={8} fill="currentColor" stroke="none" className="icon-inline" /> {c.status}
              </span>
            </div>
          ))}
        </div>
      </div>

      <hr />

      <button
        className="btn btn-primary btn-block"
        onClick={onRecalcular}
        disabled={carregando}
        style={{ display: "flex", alignItems: "center", justifyContent: "center", gap: 8 }}
      >
        <Zap size={16} className="icon-inline" />
        {carregando ? "Analisando..." : "Recalcular Diagnóstico com IA"}
      </button>
    </aside>
  );
}
