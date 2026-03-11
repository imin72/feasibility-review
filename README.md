# 사업성 분석 앱 설계 초안

이 저장소는 다음 4단계 입력 흐름으로 **사업성 분석 결과를 자동 산출**하는 앱의 MVP 설계를 담고 있습니다.

1. 예상매출
2. 투자비용(CAPEX)
3. 운영비용(OPEX)
4. 사업성 분석

사용자가 모든 수치를 직접 입력하지 않도록,
**업종/분야/서비스 표준코드 + 공공/레퍼런스 데이터 + 지역 보정계수**를 결합해 기본값을 자동 제안하고,
사용자는 필요한 항목만 보정하는 방식을 전제로 합니다.

## 문서 구성

- `docs/app-blueprint.md`: 전체 제품 구조, 입력 UX, 분석지표, 신뢰도 설계
- `docs/data-model.md`: 표준코드/레퍼런스/보정계수 데이터 모델
- `prototype/feasibility_calculator.py`: 4단계 입력값을 받아 핵심 지표를 계산하는 간단한 프로토타입
- `prototype/sample_input.json`: 프로토타입 실행용 샘플 입력
- `docs/execution-plan.md`: 앞으로의 작업 스케줄(8주) 및 우선순위 백로그

## 빠른 실행

```bash
python3 prototype/feasibility_calculator.py prototype/sample_input.json
```

출력 예시:
- 연도별 영업이익
- 누적영업이익
- BEP(손익분기점) 매출
- 단순회수기간
- NPV / IRR

