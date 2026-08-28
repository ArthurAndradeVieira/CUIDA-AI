import json
import os
from google import genai
from google.genai import types
from pydantic import BaseModel, Field


class DiagnosticoPulseGuard(BaseModel):
    score_risco: int = Field(
        description="Pontuação de risco de sobrecarga de 0 a 100", ge=0, le=100
    )
    status: str = Field(
        description="Estável, Alerta Moderado ou Risco Crítico de Burnout"
    )
    resumo_analise: str = Field(
        description="Resumo executivo em 2 frases correlacionando Perfil Comportamental (Solides), Atividades (Jira) e Gestão (Qulture.Rocks)"
    )
    impacto_perfil_solides: str = Field(
        description="Como a rotina operacional atual está colidindo ou harmonizando com o perfil comportamental do colaborador"
    )
    gatilhos_detectados: list[str] = Field(
        description="Lista de 3 a 4 fatores causais objetivos"
    )
    pauta_1on1_sugerida: list[str] = Field(
        description="3 perguntas empáticas e estratégicas calibradas para o perfil comportamental do liderado"
    )
    acao_autonoma_prescritiva: str = Field(
        description="Ação prática e autônoma que o sistema executa no ecossistema de trabalho"
    )


SYSTEM_PROMPT = """
Você é o motor preditivo e prescritivo do PulseGuard AI, integrado ao Inovathon 2026.
Sua missão é realizar uma triangulação profunda entre 3 fontes de dados corporativos:
1. Solides Profiler: Perfil comportamental (Analista, Planejador, Comunicador, Executor), nível de energia e vulnerabilidades.
2. Jira / Ferramentas de Atividades: Telemetria de reuniões, cards atrasados, horas extras e trocas de contexto.
3. Qulture.Rocks: Histórico de 1-on-1s, evolução do PDI, avaliações de desempenho e eNPS.

Diretrizes:
- Ousadia e Prescrição: Não seja um assistente passivo; interprete como a carga de trabalho agride o perfil comportamental do profissional.
- Calibração de 1-on-1: As perguntas para o gestor devem respeitar a linguagem comportamental do liderado (ex: perguntas mais estruturadas e reflexivas para Analistas; perguntas mais objetivas e de destravamento para Comunicadores).
- Resposta estrita em formato JSON com o schema fornecido.
"""


def analisar_colaborador(dados_colaborador: dict) -> dict:
    """Processa a triangulação (Jira + Qulture.Rocks + Solides) e retorna o diagnóstico estruturado."""
    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        return _mock_diagnostico_seguranca(dados_colaborador)

    client = genai.Client(api_key=api_key)

    prompt = f"Analise a seguinte estrutura integrada de colaborador e emita o diagnóstico completo:\n\n{json.dumps(dados_colaborador, indent=2, ensure_ascii=False)}"

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                response_mime_type="application/json",
                response_schema=DiagnosticoPulseGuard,
                temperature=0.2,
            ),
        )
        return json.loads(response.text)
    except Exception as e:
        print(f"Aviso: Erro na chamada da API ({e}). Usando fallback local...")
        return _mock_diagnostico_seguranca(dados_colaborador)


def _mock_diagnostico_seguranca(colab: dict) -> dict:
    """Garante resposta instantânea caso ocorra oscilação durante o Pitch."""
    if colab.get("id") == "colab_01":
        return {
            "score_risco": 92,
            "status": "Risco Crítico de Burnout",
            "resumo_analise": "Lucas (Perfil Analista) está submetido a 31.5h de reuniões e 28 trocas de contexto semanais, gerando frustração profunda pela incapacidade de foco técnico e estagnação do PDI na Qulture.Rocks.",
            "impacto_perfil_solides": "Incompatibilidade Crítica: Perfis Analistas necessitam de blocos ininterruptos de concentração. A rotina fragmentada drena sua energia com maior velocidade que em outros perfis.",
            "gatilhos_detectados": [
                "Colisão de Perfil: Analista operando com 28 trocas de contexto/semana",
                "31.5h em reuniões (Jira/Calendar) bloqueando a produção de código",
                "PDI na Qulture.Rocks paralisado há 60 dias por falta de tempo",
                "38% de trabalho fora de horário compensando o tempo perdido em reuniões",
            ],
            "pauta_1on1_sugerida": [
                "Lucas, seu perfil rende melhor com foco contínuo, mas você teve mais de 30h de reuniões nesta semana. Quais dessas agendas podemos cortar da sua rotina a partir de amanhã?",
                "Como a paralisação do seu PDI na Qulture.Rocks está impactando sua motivação técnica de longo prazo no time?",
                "Se estruturarmos dois dias de 'Foco Total' (Zero Reuniões) por semana, quais entregas críticas você priorizaria refatorar?",
            ],
            "acao_autonoma_prescritiva": "Ativação do Escudo Operacional: Congelamento imediato de novos cards no Jira, proteção de blocos de foco de 4h/dia no calendário e notificação ao RH sobre risco de desligamento voluntário iminente.",
        }
    elif colab.get("id") == "colab_02":
        return {
            "score_risco": 50,
            "status": "Alerta Moderado",
            "resumo_analise": "Mariana (Perfil Comunicadora/Executora) lida bem com reuniões, mas o acúmulo de dependências externas não resolvidas começa a comprimir seus prazos de fechamento de trimestre.",
            "impacto_perfil_solides": "Alinhamento Parcial: Sua facilidade de comunicação absorve a rotina de alinhamentos, mas o perfil executor gera ansiedade diante de bloqueios operacionais externos.",
            "gatilhos_detectados": [
                "24h de reuniões/semana gerando acúmulo de cards operacionais",
                "Dependências externas travando entregas da sprint",
                "Queda de energia no Solides Profiler de Alta para Média",
            ],
            "pauta_1on1_sugerida": [
                "Mariana, quais impedimentos de aprovação externa eu devo intervir diretamente hoje para liberar sua squad?",
                "Como podemos rebalancear as entregas do trimestre para garantir a conclusão do seu PDI na Qulture.Rocks?",
                "Você sente que a quantidade de reuniões atuais está agregando valor estratégico ou virando apenas reporte?",
            ],
            "acao_autonoma_prescritiva": "Nudge Prescritivo: Alerta automático à coordenação para destravamento de dependências no Jira e sugestão de delegação de 2 frentes de alinhamento.",
        }
    else:
        return {
            "score_risco": 10,
            "status": "Estável",
            "resumo_analise": "Rodrigo (Planejador/Analista) atua em cadência equilibrada, com previsibilidade operacional no Jira, metas de PDI ativas na Qulture.Rocks e energia alta preservada.",
            "impacto_perfil_solides": "Sinergia Alta: O ambiente atual oferece a previsibilidade e o tempo de planejamento estruturado essenciais para a alta performance de perfis planejadores.",
            "gatilhos_detectados": [
                "Baixa fragmentação de contexto (apenas 4 trocas/semana)",
                "PDI na Qulture.Rocks avançado em 85%",
                "Zero cards atrasados e eNPS sustentado em 9",
            ],
            "pauta_1on1_sugerida": [
                "Seu ritmo atual de entregas e PDI está excelente. Você gostaria de mentorar um dev júnior na squad?",
                "Como podemos aproveitar sua estabilidade de entregas para você desenhar a nova arquitetura do pipeline?",
                "O que do seu modelo de planejamento semanal podemos compartilhar com os outros times?",
            ],
            "acao_autonoma_prescritiva": "Registro de Sustentabilidade: Indicadores saudáveis confirmados; dados enviados para composição do benchmark de retenção do time.",
        }


if __name__ == "__main__":
    with open("data.json", "r", encoding="utf-8") as f:
        dados = json.load(f)

    print("Testando motor integrado com Colaborador 01...")
    resultado = analisar_colaborador(dados["colaboradores"][0])
    print(json.dumps(resultado, indent=2, ensure_ascii=False))