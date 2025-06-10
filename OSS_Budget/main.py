# main.py

from budget import Budget # budget.py에서 Budget 클래스를 임포트
import datetime # 연월 유효성 검사를 위해 임포트


def main():
    """가계부 프로그램의 메인 실행 함수."""
    budget = Budget()

    while True:
        print("==== 간단 가계부 ====")
        print("1. 지출 추가")
        print("2. 지출 목록 보기")
        print("3. 전체 총 지출 보기")
        print("4. 월별 총 지출 보기") # 새로운 메뉴 추가
        print("5. 종료")
        choice = input("원하는 메뉴 번호를 입력하세요 > ")

        if choice == "1":
            category = input("카테고리 (예: 식비, 교통, 통신): ")
            description = input("설명: ")
            try:
                amount = int(input("금액(원): "))
                if amount <= 0:
                    print("❌ 금액은 0보다 커야 합니다. 다시 입력해주세요.\n")
                    continue
                budget.add_expense(category, description, amount)
            except ValueError:
                print("❌ 잘못된 금액 형식입니다. 숫자를 입력해주세요.\n")
            except Exception as e:
                print(f"❌ 오류 발생: {e}\n")

        elif choice == "2":
            budget.list_expenses()

        elif choice == "3":
            budget.total_spent()

        elif choice == "4": # 월별 총 지출 보기 기능
            try:
                year_input = input("조회할 연도를 입력하세요 (예: 2023): ")
                month_input = input("조회할 월을 입력하세요 (1~12): ")

                year = int(year_input)
                month = int(month_input)

                if not (1 <= month <= 12):
                    print("❌ 월은 1에서 12 사이의 숫자여야 합니다. 다시 입력해주세요.\n")
                    continue

                # 올바른 연도인지 기본적인 검사 (예: 미래 연도 방지)
                current_year = datetime.date.today().year
                if year < 2000 or year > current_year + 5: # 임의의 범위
                     print("❌ 올바른 연도를 입력해주세요 (예: 2000년부터 현재+5년).\n")
                     continue

                budget.get_monthly_total(year, month)

            except ValueError:
                print("❌ 연도 또는 월 입력이 잘못되었습니다. 숫자를 입력해주세요.\n")
            except Exception as e:
                print(f"❌ 오류 발생: {e}\n")

        elif choice == "5": # 종료 메뉴 번호 변경
            print("👋 가계부 프로그램을 종료합니다. 이용해주셔서 감사합니다!")
            break

        else:
            print("❓ 잘못된 메뉴 선택입니다. 1에서 5 사이의 숫자를 입력해주세요.\n")


if __name__ == "__main__":
    main()