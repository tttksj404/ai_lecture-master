---
title: RAG 구현 & LangGraph
tags: [rag, langgraph, retriever, embeddings, multi-agent]
created: 2026-04-02
---

# RAG 구현 & LangGraph

## 핵심 키워드
- RAG 파이프라인
- 임베딩 / 벡터스토어 / Retriever
- StateGraph / Agent Workflow
- ReAct / Multi-Agent 패턴

## 학습 흐름
1. 문서 임베딩 + 벡터스토어 구축
2. Retriever 기반 검색 품질 점검
3. RAG 생성 파이프라인 구성
4. LangGraph StateGraph로 워크플로우 확장

## 힌트 파일 (실습 + 과제)
- [실습-힌트 RAG](../03_rag_langgraph/(실습-힌트)%204-1_RAG_기반_Customer_Service_AI_에이전트_개발.ipynb)
- [실습-힌트 ReAct](../03_rag_langgraph/(실습-힌트)%204-2(1)_ReAct_기반_Agent_서비스_개발.ipynb)
- [실습-힌트 Multi-Agent](../03_rag_langgraph/(실습-힌트)%204-2(2)_Multi-Agent_대표_패턴_학습.ipynb)
- [과제-힌트 RAG](../03_rag_langgraph/(과제-힌트)%204-1_RAG_기반_Customer_Service_AI_에이전트_개발.ipynb)
- [과제-힌트 ReAct](../03_rag_langgraph/(과제-힌트)%204-2(1)_ReAct_기반_Agent_서비스_개발.ipynb)
- [과제-힌트 Multi-Agent](../03_rag_langgraph/(과제-힌트)%204-2(2)_Multi-Agent_대표_패턴_학습.ipynb)
- [day10_README](../03_rag_langgraph/day10_README.md)
- [day11_README](../03_rag_langgraph/day11_README.md)

## 실습 TODO
- [ ] Retriever `k`값 바꿔 응답 근거 품질 비교
- [ ] `# [문제였던 부분 반영]` 코드셀 재작성
- [ ] StateGraph 노드/엣지 흐름도 직접 그려보기

## 관련 노트
- [[00_학습_대시보드]]
- [[01_EDA와_선형회귀]]
- [[02_데이터_생성_합성_프롬프팅]]
