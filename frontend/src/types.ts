export interface SolidesProfiler {
  perfil_predominante: string;
  caracteristicas_chave: string;
  nivel_exigencia_pessoal: string;
  energia_atual: string;
}

export interface JiraTelemetria {
  horas_reuniao_semana: number;
  cards_em_aberto: number;
  cards_atrasados: number;
  mudancas_de_contexto_semana: number;
  commits_fora_do_horario_pct: number;
  dias_consecutivos_sem_folga: number;
}

export interface QultureRocks {
  enps_recente: number;
  pdi_status: string;
  ultima_avaliacao_desempenho: string;
  resumo_ultimo_pulso: string;
  historico_1on1s: string[];
}

export interface Colaborador {
  id: string;
  nome: string;
  cargo: string;
  time: string;
  foto_url?: string;
  solides_profiler: SolidesProfiler;
  jira_telemetria: JiraTelemetria;
  qulture_rocks: QultureRocks;
  cenario_esperado: string;
}

export interface Diagnostico {
  score_risco: number;
  status: string;
  resumo_analise: string;
  impacto_perfil_solides: string;
  gatilhos_detectados: string[];
  pauta_1on1_sugerida: string[];
  acao_autonoma_prescritiva: string;
}
