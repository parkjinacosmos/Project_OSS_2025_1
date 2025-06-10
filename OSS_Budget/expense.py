# expense.py

class Expense:
    """
    하나의 지출 항목을 나타내는 클래스.
    날짜, 카테고리, 설명, 금액 정보를 저장합니다.
    """
    def __init__(self, date: str, category: str, description: str, amount: int):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount

    def __str__(self) -> str:
        """지출 정보를 보기 좋게 문자열로 반환합니다."""
        return f"[{self.date}] {self.category} - {self.description}: {self.amount:,}원"

    def __repr__(self) -> str:
        """객체를 재현할 수 있는 문자열 형태로 반환합니다."""
        return f"Expense(date='{self.date}', category='{self.category}', description='{self.description}', amount={self.amount})"