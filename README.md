# DKU-Open-SW-Development

Python, Ruff, pytest와 GitHub Actions를 이용한 주문 계산 및 CI/CD 실습입니다. 실습 내용 파악을 위해 본 파일을 남겼습니다.

Python 3.14.x가 아닌 3.13.2를 사용합니다. 프로젝트 루트에서 실행하세요.

## 실습 내용

- **GitHub Actions 기초:** 이벤트, 변수와 컨텍스트, 조건문, 작업 상태 및 출력, 문자열·해시 함수, 이슈 생성과 댓글 작성 워크플로 실습
- **Level 1:** 주문 금액 계산과 정상·경계·예외 테스트
- **Level 2:** 할인 및 배송비 계산, 경계값과 할인율 예외 테스트, `parametrize`
- **Level 3:** CSV 매출 집계, `tmp_path`와 fixture를 이용한 파일 테스트, 커버리지 측정
- **Level 4:** FastAPI 주문 생성·조회 API와 `TestClient` 테스트, 운영체제별 CI 테스트
- **Level 5:** CSV 기반 정적 보고서 생성과 GitHub Pages 배포, 테스트 실패 시 배포 차단 확인

## GitHub Actions

- [Python CI](.github/workflows/ci.yml): Ruff 검사와 Ubuntu·Windows 테스트를 실행하고 커버리지 XML을 artifact로 저장합니다.
- [OrderLab CI-CD](.github/workflows/ci-cd.yml): `main` 대상 PR과 push에서 품질 검사를 실행합니다. `main` push에서 검사가 성공하면 보고서를 GitHub Pages에 배포합니다.

- 실행 결과와 커버리지 파일은 저장소의 **Actions** 탭에서 확인할 수 있습니다.

- **GitHub Pages는 다른 저장소에서 별도의 사이트가 배포되고 있어, 실습 보고서가 정상적으로 표시되는 것을 확인한 뒤 배포를 중지했습니다.**
