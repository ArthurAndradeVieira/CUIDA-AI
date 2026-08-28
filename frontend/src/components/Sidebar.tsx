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
  { icone: "🧠", nome: "Solides Profiler", status: "🟢 Ativo" },
  { icone: "⚡", nome: "Jira & Calendar", status: "🟢 Sincronizado" },
  { icone: "🎯", nome: "Qulture.Rocks", status: "🟢 Conectado" },
  { icone: "🤖", nome: "Gemini 2.5 Flash", status: "🟢 Online" },
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
        <div className="sidebar-section-title">👤 Seleção de Colaborador</div>
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
          <span className="badge-pill" style={{ marginTop: 4, display: "inline-block" }}>
            🧬 {selecionado.solides_profiler.perfil_predominante}
          </span>
        </div>
      </div>

      <hr />

      <div>
        <div className="sidebar-section-title">🔌 Conectores Ativos</div>
        <div className="connector-list">
          {CONECTORES.map((c) => (
            <div className="connector-row" key={c.nome}>
              <span>
                {c.icone} <b>{c.nome}</b>
              </span>
              <span className="connector-status">{c.status}</span>
            </div>
          ))}
        </div>
      </div>

      <hr />

      <button
        className="btn btn-primary btn-block"
        onClick={onRecalcular}
        disabled={carregando}
      >
        ⚡ {carregando ? "Analisando..." : "Recalcular Diagnóstico com IA"}
      </button>
    </aside>
  );
}
