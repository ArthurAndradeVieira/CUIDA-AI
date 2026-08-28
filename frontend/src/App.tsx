import { useEffect, useState } from "react";
import { LayoutDashboard, MessageSquare, Radar, Shield, Stethoscope } from "lucide-react";
import { fetchColaboradores, fetchDiagnostico } from "./api";
import type { Colaborador, Diagnostico } from "./types";
import Sidebar from "./components/Sidebar";
import Header from "./components/Header";
import SquadOverview from "./components/SquadOverview";
import ColabHero from "./components/ColabHero";
import OverviewTab from "./components/tabs/OverviewTab";
import DiagnosticoTab from "./components/tabs/DiagnosticoTab";
import TriangulacaoTab from "./components/tabs/TriangulacaoTab";
import OneOnOneTab from "./components/tabs/OneOnOneTab";
import EscudoTab from "./components/tabs/EscudoTab";

const TABS = [
  { key: "visao-geral", label: "Visão Geral do Time", Icon: LayoutDashboard },
  { key: "diagnostico", label: "Diagnóstico Prescritivo & IA", Icon: Stethoscope },
  { key: "fontes", label: "Triangulação de Dados", Icon: Radar },
  { key: "1on1", label: "Pauta de 1-on-1 & PDI", Icon: MessageSquare },
  { key: "escudo", label: "Escudo Operacional & Ação Autônoma", Icon: Shield },
] as const;

type TabKey = (typeof TABS)[number]["key"];

export default function App() {
  const [colaboradores, setColaboradores] = useState<Colaborador[]>([]);
  const [selecionadoId, setSelecionadoId] = useState<string | null>(null);
  const [diag, setDiag] = useState<Diagnostico | null>(null);
  const [carregandoDiag, setCarregandoDiag] = useState(false);
  const [escudoAtivado, setEscudoAtivado] = useState(false);
  const [tabAtiva, setTabAtiva] = useState<TabKey>("visao-geral");
  const [erro, setErro] = useState<string | null>(null);

  useEffect(() => {
    fetchColaboradores()
      .then((lista) => {
        setColaboradores(lista);
        setSelecionadoId(lista[0]?.id ?? null);
      })
      .catch(() => setErro("Não foi possível carregar os colaboradores. Verifique se a API está rodando."));
  }, []);

  useEffect(() => {
    if (selecionadoId) carregarDiagnostico(selecionadoId);
  }, [selecionadoId]);

  function carregarDiagnostico(id: string) {
    setCarregandoDiag(true);
    setErro(null);
    fetchDiagnostico(id)
      .then((resultado) => {
        setDiag(resultado);
        setEscudoAtivado(false);
      })
      .catch(() => setErro("Não foi possível gerar o diagnóstico. Verifique se a API está rodando."))
      .finally(() => setCarregandoDiag(false));
  }

  const colab = colaboradores.find((c) => c.id === selecionadoId);

  if (erro) {
    return <div className="loading-state">{erro}</div>;
  }

  if (!colab) {
    return <div className="loading-state">Carregando Cuida AI...</div>;
  }

  return (
    <div className="app-shell">
      <Sidebar
        colaboradores={colaboradores}
        selecionado={colab}
        onSelecionar={setSelecionadoId}
        onRecalcular={() => selecionadoId && carregarDiagnostico(selecionadoId)}
        carregando={carregandoDiag}
      />

      <main className="app-main">
        <Header />
        <SquadOverview colaboradores={colaboradores} selecionadoId={colab.id} onSelecionar={setSelecionadoId} />
        <ColabHero colab={colab} />

        <nav className="tabs-nav">
          {TABS.map((tab) => (
            <button
              key={tab.key}
              className={`tab-btn${tabAtiva === tab.key ? " active" : ""}`}
              onClick={() => setTabAtiva(tab.key)}
            >
              <tab.Icon size={15} className="icon-inline" /> {tab.label}
            </button>
          ))}
        </nav>

        {tabAtiva === "visao-geral" && <OverviewTab colaboradores={colaboradores} />}

        {tabAtiva !== "visao-geral" &&
          (carregandoDiag || !diag ? (
            <div className="loading-state">Cuida AI correlacionando Solides + Jira + Qulture.Rocks...</div>
          ) : (
            <>
              {tabAtiva === "diagnostico" && <DiagnosticoTab diag={diag} />}
              {tabAtiva === "fontes" && <TriangulacaoTab colab={colab} />}
              {tabAtiva === "1on1" && <OneOnOneTab colab={colab} diag={diag} />}
              {tabAtiva === "escudo" && (
                <EscudoTab
                  colab={colab}
                  diag={diag}
                  ativado={escudoAtivado}
                  onAtivar={() => setEscudoAtivado(true)}
                  onRestaurar={() => setEscudoAtivado(false)}
                />
              )}
            </>
          ))}

        <footer className="app-footer">
          <span>Cuida AI • Inovathon 2026 • Pilar Ousadia em Inteligência Artificial</span>
          <span>Solides Profiler • Jira Software • Qulture.Rocks Integrados</span>
        </footer>
      </main>
    </div>
  );
}
