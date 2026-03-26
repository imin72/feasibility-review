# 데이터 모델 (MVP)

## 1. taxonomy_master
업종/분야/서비스종류 표준코드

| 컬럼 | 타입 | 설명 |
|---|---|---|
| code | string | 표준코드 (예: EV.BATT.TEST) |
| industry | string | 업종 |
| domain | string | 분야 |
| service_type | string | 서비스 종류 |
| unit | string | 과금 단위(건/월/시간 등) |

## 2. reference_metrics
자동 추천을 위한 기준값 테이블

| 컬럼 | 타입 | 설명 |
|---|---|---|
| code | string | taxonomy_master.code |
| region_code | string | 지역코드 |
| metric_name | string | avg_unit_price, labor_cost_index 등 |
| value | number | 값 |
| source | string | 출처 |
| confidence | number | 0~1 |
| effective_date | date | 기준일 |

## 3. capex_templates
투자비용 템플릿

| 컬럼 | 타입 | 설명 |
|---|---|---|
| code | string | 업종 표준코드 |
| item | string | 장비/시설/개발비/보증금 |
| min_value | number | 최소 |
| max_value | number | 최대 |
| depreciable | boolean | 감가상각 대상 여부 |

## 4. opex_templates
운영비용 템플릿

| 컬럼 | 타입 | 설명 |
|---|---|---|
| code | string | 업종 표준코드 |
| item | string | 인건비/임차료/전기료/유지보수비 등 |
| calc_type | string | fixed / variable_rate |
| default_value | number | 기본값 |
| escalation_rate | number | 연 상승률 |

## 5. analysis_projects
프로젝트 헤더

| 컬럼 | 타입 | 설명 |
|---|---|---|
| project_id | string | 프로젝트 ID |
| project_name | string | 프로젝트명 |
| code | string | 업종 표준코드 |
| region_code | string | 지역 |
| scenario | string | conservative/base/optimistic |
| created_at | datetime | 생성시각 |

## 6. analysis_inputs
사용자 입력·보정 내역

| 컬럼 | 타입 | 설명 |
|---|---|---|
| project_id | string | 프로젝트 ID |
| step | int | 1~4 |
| field_name | string | 입력항목 |
| input_value | number/string | 사용자값 |
| default_value | number/string | 자동값 |
| source | string | 값의 출처 |

## 7. analysis_results
산출 결과

| 컬럼 | 타입 | 설명 |
|---|---|---|
| project_id | string | 프로젝트 ID |
| year | int | 연도 |
| revenue | number | 매출 |
| capex | number | 투자비용 |
| opex | number | 운영비용 |
| operating_profit | number | 영업이익 |
| operating_margin | number | 영업이익률 |
| cumulative_profit | number | 누적영업이익 |

