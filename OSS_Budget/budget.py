# budget.py

import datetime
from expense import Expense # expense.py에서 Expense 클래스를 임포트


class Budget:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category: str, description: str, amount: int):
        """새로운 지출 항목을 추가합니다."""
        today = datetime.date.today().isoformat() # 'YYYY-MM-DD' 형식
        expense = Expense(today, category, description, amount)
        self.expenses.append(expense)
        print("✅ 지출이 성공적으로 추가되었습니다.\n")

    def list_expenses(self):
        """현재까지 추가된 모든 지출 목록을 출력합니다."""
        if not self.expenses:
            print("ℹ️ 지출 내역이 없습니다.\n")
            return
        print("\n--- 전체 지출 목록 ---")
        for idx, e in enumerate(self.expenses, 1):
            print(f"{idx}. {e}")
        print("---------------------\n")

    def total_spent(self):
        """현재까지의 총 지출 금액을 계산하여 출력합니다."""
        total = sum(e.amount for e in self.expenses)
        print(f"💰 총 지출: {total:,}원\n") # 천단위 콤마 추가

    def get_monthly_total(self, year: int, month: int):
        """
        지정된 연월의 총 지출 금액을 계산하여 출력합니다.
        """
        monthly_total = 0
        found_expenses = False
        for expense in self.expenses:
            # Expense 객체의 date 속성 (예: '2023-11-15')에서 연월 추출
            expense_date = datetime.datetime.strptime(expense.date, "%Y-%m-%d").date()
            if expense_date.year == year and expense_date.month == month:
                monthly_total += expense.amount
                found_expenses = True
        
        if not found_expenses:
            print(f"ℹ️ {year}년 {month:02d}월의 지출 내역이 없습니다.\n")
        else:
            print(f"🗓️ {year}년 {month:02d}월 총 지출: {monthly_total:,}원\n") # 천단위 콤마 추가
