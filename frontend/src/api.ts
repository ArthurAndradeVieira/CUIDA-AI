import type { Colaborador, Diagnostico } from "./types";

const API_BASE = "http://localhost:8000/api";

export async function fetchColaboradores(): Promise<Colaborador[]> {
  const res = await fetch(`${API_BASE}/colaboradores`);
  if (!res.ok) throw new Error("Falha ao carregar colaboradores");
  return res.json();
}

export async function fetchDiagnostico(colabId: string): Promise<Diagnostico> {
  const res = await fetch(`${API_BASE}/colaboradores/${colabId}/diagnostico`, {
    method: "POST",
  });
  if (!res.ok) throw new Error("Falha ao gerar diagnóstico");
  return res.json();
}
