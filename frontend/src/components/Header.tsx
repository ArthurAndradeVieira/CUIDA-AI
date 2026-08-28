import logo from "../assets/logo.png";

export default function Header() {
  return (
    <header className="app-header">
      <div className="app-header-left">
        <img src={logo} alt="Cuida AI" />
        <div>
          <h1>
            Cuida AI <span className="badge-pill">Inovathon 2026</span>
          </h1>
          <p>Plataforma Preditiva e Prescritiva de Blindagem Operacional e Sustentabilidade Humana</p>
        </div>
      </div>
      <span className="header-tag">📡 Triangulação: Solides • Jira • Qulture.Rocks</span>
    </header>
  );
}
