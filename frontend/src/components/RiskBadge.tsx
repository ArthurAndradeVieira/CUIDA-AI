export type RiskLevel = "critico" | "alerta" | "estavel";

export function riskLevelFromScenario(cenarioEsperado: string): RiskLevel {
  if (cenarioEsperado.includes("Crítico")) return "critico";
  if (cenarioEsperado.includes("Alerta")) return "alerta";
  return "estavel";
}

export function riskLevelFromScore(score: number): RiskLevel {
  if (score >= 70) return "critico";
  if (score >= 40) return "alerta";
  return "estavel";
}

const LABELS: Record<RiskLevel, string> = {
  critico: "🔴 Risco Crítico",
  alerta: "🟡 Alerta Moderado",
  estavel: "🟢 Estável",
};

export default function RiskBadge({ level, label }: { level: RiskLevel; label?: string }) {
  return <span className={`badge-risco badge-risco-${level}`}>{label ?? LABELS[level]}</span>;
}
