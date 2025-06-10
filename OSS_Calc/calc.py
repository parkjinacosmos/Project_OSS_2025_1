# calculator_module.py

import tkinter as tk
import math # 팩토리얼, 순열, 조합 계산을 위해 math 모듈 임포트


class Calculator:
    """
    Tkinter 기반의 공학 계산기 클래스.
    기본 사칙연산 외에 팩토리얼, 순열, 조합 기능을 제공합니다.
    """
    def __init__(self, root):
        self.root = root
        self.root.title("공학 계산기") # 계산기 제목 변경
        self.root.geometry("350x550") # 버튼 추가를 위해 창 크기 증가
        self.root.resizable(False, False) # 창 크기 조절 비활성화 (UI 일관성 유지)

        self.expression = "" # 현재 입력된 수식 또는 숫자
        self.n_val = None  # 순열(P) 및 조합(C) 연산 시 첫 번째 숫자 (n)를 저장
        self.pending_stat_op = None  # 대기 중인 통계 연산 ('P' 또는 'C')

        # === 입력창 설정 ===
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right", bd=5, relief=tk.SUNKEN)
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # === 버튼 레이아웃 정의 ===
        # 새로운 통계 기능 버튼들이 추가되었습니다.
        buttons = [
            ['(', ')', 'C', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=', '!'], # '!'는 팩토리얼 (fact)
            ['P', 'C'] # 순열 (Permutation) 및 조합 (Combination)
        ]

        # === 버튼 생성 및 배치 ===
        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                if char == '=':
                    # '=' 버튼은 계산을 담당하는 calculate 메서드에 연결
                    btn = tk.Button(
                        frame,
                        text=char,
                        font=("Arial", 18),
                        command=self.calculate,
                        bg="#FFA500", fg="white", # 주황색 배경, 흰색 글씨
                        activebackground="#FF8C00"
                    )
                elif char == 'C':
                    # 'C' (Clear) 버튼은 clear_entry 메서드에 연결
                    btn = tk.Button(
                        frame,
                        text=char,
                        font=("Arial", 18),
                        command=self.clear_entry,
                        bg="#FF6347", fg="white", # 빨간색 배경, 흰색 글씨
                        activebackground="#E74C3C"
                    )
                elif char in ['!', 'P', 'C']:
                    # 팩토리얼, 순열, 조합 버튼은 on_stat_click 메서드에 연결
                    btn = tk.Button(
                        frame,
                        text=char,
                        font=("Arial", 18),
                        command=lambda ch=char: self.on_stat_click(ch),
                        bg="#ADD8E6", # 연한 파란색 배경
                        activebackground="#87CEEB"
                    )
                else:
                    # 숫자 및 일반 연산자 버튼은 on_click 메서드에 연결
                    btn = tk.Button(
                        frame,
                        text=char,
                        font=("Arial", 18),
                        command=lambda ch=char: self.on_click(ch),
                        bg="#E0E0E0", # 회색 배경
                        activebackground="#C0C0C0"
                    )
                btn.pack(side="left", expand=True, fill="both", padx=2, pady=2) # 버튼 간 간격 추가

    def update_entry(self, value):
        """
        계산기 디스플레이(Entry 위젯)를 업데이트합니다.
        """
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, value)

    def on_click(self, char):
        """
        숫자 및 일반 사칙연산 버튼 클릭을 처리합니다.
        새로운 숫자나 연산자가 입력되면 대기 중인 통계 연산을 초기화합니다.
        """
        # P, C 연산 대기 중일 때 일반 숫자/연산자 입력 시 초기화
        if self.pending_stat_op and char.isdigit():
            # 'r' 값을 입력하는 상황에서 숫자를 입력하면 기존 expression 초기화
            self.expression = ""
            self.pending_stat_op = None # r 값을 입력하기 시작했으므로 대기 상태 해제
        elif self.pending_stat_op and not char.isdigit():
            # 'r' 값을 입력하는 상황에서 숫자가 아닌 다른 것을 입력하면 에러 처리
            self.expression = "에러: 'r'값 입력 필요"
            self.update_entry(self.expression)
            self.n_val = None
            self.pending_stat_op = None
            return

        self.expression += str(char)
        self.update_entry(self.expression)

    def clear_entry(self):
        """
        현재 입력된 수식을 지우고, 대기 중인 모든 통계 연산 상태를 초기화합니다.
        'C' 버튼에 연결됩니다.
        """
        self.expression = ""
        self.n_val = None
        self.pending_stat_op = None
        self.update_entry(self.expression)

    def calculate_factorial(self, num_str: str) -> str:
        """
        주어진 문자열 숫자의 팩토리얼을 계산합니다.
        음수나 정수가 아닌 경우 에러를 반환합니다.
        """
        try:
            num = int(float(num_str)) # 소수점 입력 시 정수 부분만 사용
            if float(num_str) != num:
                raise ValueError("팩토리얼은 정수에 대해서만 유효합니다.")
            if num < 0:
                raise ValueError("음수에 대한 팩토리얼은 정의되지 않습니다.")
            return str(math.factorial(num))
        except ValueError as e:
            return "에러: " + str(e)
        except OverflowError:
            return "에러: 숫자 너무 큼"
        except Exception:
            return "에러"

    def calculate_permutation(self, n: int, r: int) -> str:
        """
        순열 P(n, r)을 계산합니다. (n! / (n-r)!)
        n >= r >= 0 조건을 만족해야 합니다.
        """
        try:
            if r < 0 or n < 0 or r > n:
                raise ValueError("n >= r >= 0 이어야 합니다.")
            return str(math.factorial(n) // math.factorial(n - r))
        except ValueError as e:
            return "에러: " + str(e)
        except OverflowError:
            return "에러: 숫자 너무 큼"
        except Exception:
            return "에러"

    def calculate_combination(self, n: int, r: int) -> str:
        """
        조합 C(n, r)을 계산합니다. (n! / (r! * (n-r)!))
        n >= r >= 0 조건을 만족해야 합니다.
        """
        try:
            if r < 0 or n < 0 or r > n:
                raise ValueError("n >= r >= 0 이어야 합니다.")
            # Python 3.8 이상에서는 math.comb() 사용 가능 (더 효율적)
            if hasattr(math, 'comb'):
                return str(math.comb(n, r))
            else:
                return str(math.factorial(n) // (math.factorial(r) * math.factorial(n - r)))
        except ValueError as e:
            return "에러: " + str(e)
        except OverflowError:
            return "에러: 숫자 너무 큼"
        except Exception:
            return "에러"

    def on_stat_click(self, char: str):
        """
        통계 함수 버튼(!, P, C) 클릭을 처리합니다.
        """
        current_expression = self.expression

        if char == '!': # 팩토리얼 연산
            # 현재 입력창의 값에 대해 팩토리얼을 즉시 계산
            if current_expression and current_expression.replace('.', '').isdigit():
                result = self.calculate_factorial(current_expression)
                self.expression = result
                self.update_entry(self.expression)
                self.n_val = None
                self.pending_stat_op = None
            else:
                self.expression = "에러: 유효하지 않은 입력"
                self.update_entry(self.expression)
                self.n_val = None
                self.pending_stat_op = None

        elif char == 'P' or char == 'C': # 순열 또는 조합 연산
            # 첫 번째 숫자 (n)를 입력창에서 가져오고, 대기 상태 설정
            if current_expression and current_expression.replace('.', '').isdigit():
                self.n_val = int(float(current_expression)) # n은 정수여야 함
                self.pending_stat_op = char
                self.expression = "" # 'r' 값을 입력받기 위해 입력창 초기화
                self.update_entry(f"{self.n_val}{char} r?") # r 값 입력 대기 메시지
            else:
                self.expression = "에러: 'n'값 입력 필요"
                self.update_entry(self.expression)
                self.n_val = None
                self.pending_stat_op = None

    def calculate(self):
        """
        '=' 버튼 클릭 시 최종 계산을 수행합니다.
        대기 중인 통계 연산이 있는지 먼저 확인하고 처리합니다.
        """
        if self.pending_stat_op: # 순열(P) 또는 조합(C) 연산 처리
            if self.expression and self.expression.replace('.', '').isdigit() and self.n_val is not None:
                r_val = int(float(self.expression)) # r은 정수여야 함
                if self.pending_stat_op == 'P':
                    result = self.calculate_permutation(self.n_val, r_val)
                elif self.pending_stat_op == 'C':
                    result = self.calculate_combination(self.n_val, r_val)
                self.expression = result
                self.n_val = None
                self.pending_stat_op = None
                self.update_entry(self.expression)
            else:
                self.expression = "에러: 'r'값 입력 오류"
                self.update_entry(self.expression)
                self.n_val = None
                self.pending_stat_op = None
        else: # 일반 사칙연산 처리 (기존 코드와 유사)
            try:
                # 보안상의 이유로 eval() 사용 시 주의해야 하지만,
                # 본 계산기는 로컬 환경에서 사용되는 단순 계산기로 간주합니다.
                self.expression = str(eval(self.expression))
            except ZeroDivisionError:
                self.expression = "0으로 나눌 수 없습니다"
            except SyntaxError:
                self.expression = "잘못된 수식"
            except Exception:
                self.expression = "에러"
            finally:
                self.update_entry(self.expression)
                self.n_val = None # 연산 후 n_val 초기화
                self.pending_stat_op = None # 연산 후 pending_stat_op 초기화
