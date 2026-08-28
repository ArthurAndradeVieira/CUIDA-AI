import { AlertOctagon, AlertTriangle, CheckCircle2 } from "lucide-react";
import type { ReactNode } from "react";

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

const ICONS: Record<RiskLevel, typeof AlertOctagon> = {
  critico: AlertOctagon,
  alerta: AlertTriangle,
  estavel: CheckCircle2,
};

const LABELS: Record<RiskLevel, string> = {
  critico: "Risco Crítico",
  alerta: "Alerta Moderado",
  estavel: "Estável",
};

export default function RiskBadge({ level, label }: { level: RiskLevel; label?: ReactNode }) {
  const Icon = ICONS[level];
  return (
    <span className={`badge-risco badge-risco-${level}`}>
      <Icon size={14} className="icon-inline" />
      {label ?? LABELS[level]}
    </span>
  );
}
