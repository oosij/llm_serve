# llm_serve
![녹화4](https://github.com/user-attachments/assets/785d2dd3-ea55-4e44-aebf-366adfbc9e44)

개발 환경 :
Docker 기반 서버 (LLM 서빙 및 sLLM 연구 개발)
기본 OS: Rocky Linux 8.1
GPU: NVIDIA RTX A6000 x2
Docker OS: Ubuntu 22.04 LTS
Python: 3.12.4
(동일한 설정으로 두 대의 서버 구성)

RAG 연구 및 개발 서버
기본 OS: Windows 10
GPU: NVIDIA GeForce RTX 2080 Ti x4
Python: 3.10.6
 
주요 기술 및 수행 업무 : 

LLM 서빙 및 연구개발 환경 구축
- Docker 기반 서버 환경에서 대형 언어 모델(Gemma 2-27b-it)의 실시간 API 서빙 환경 구축 및 관리
- Streamlit 기반 대시보드를 구현하여 팀원 간의 협업을 지원하며, 상호작용 기록 및 에러 로깅 기능 포함

RAG 성능 개선 및 연구
- pre-retrieval에서 다양한 검색 최적화 기법(Multi-Query, Query Transformation, HyDE)과 post-retrieval(bge-reranker-base)을 활용하여 검색 정확도 및 응답성 향상 연구
- PDF 내 테이블 데이터를 마크다운 형식으로 변환하는 문서 파서(Llamaparse), 벡터 데이터베이스(Qdrant/ChromaDB) 활용

sLLM 추론 및 최적화
- Chain-of-Thought(CoT) 기반의 논리적 추론을 지원하는 sLLM 모델 파인튜닝 및 연구 환경 구축.

개선 사항 : 
- RAG와 CoT 기반 기술을 통한 성능 개선 진행 중, 검색 정확도와 응답성을 높이기 위한 실험 지속
