# calculator_module.py

import tkinter as tk
from tkinter import messagebox # BMI 결과 메시지 박스를 위해 임포트


class Calculator:
    """
    기본 사칙연산을 수행하는 계산기 클래스.
    """
    def __init__(self, root):
        self.root = root
        self.expression = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right", bd=5, relief=tk.SUNKEN)
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 생성
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=']
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                if char == '=':
                    btn = tk.Button(
                        frame,
                        text=char,
                        font=("Arial", 18),
                        command=self.calculate,
                        bg="#FFA500", fg="white" # 주황색
                    )
                elif char == 'C':
                    btn = tk.Button(
                        frame,
                        text=char,
                        font=("Arial", 18),
                        command=self.clear_entry,
                        bg="#FF6347", fg="white" # 빨간색
                    )
                else:
                    btn = tk.Button(
                        frame,
                        text=char,
                        font=("Arial", 18),
                        command=lambda ch=char: self.on_click(ch)
                    )
                btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)

    def update_entry(self, value):
        """계산기 디스플레이(Entry 위젯)를 업데이트합니다."""
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, value)

    def on_click(self, char):
        """숫자 및 연산자 버튼 클릭을 처리합니다."""
        self.expression += str(char)
        self.update_entry(self.expression)

    def clear_entry(self):
        """현재 입력된 수식을 지웁니다 ('C' 버튼)."""
        self.expression = ""
        self.update_entry(self.expression)

    def calculate(self):
        """'=' 버튼 클릭 시 계산을 수행합니다."""
        try:
            self.expression = str(eval(self.expression))
        except ZeroDivisionError:
            self.expression = "0으로 나눌 수 없습니다"
        except SyntaxError:
            self.expression = "잘못된 수식"
        except Exception:
            self.expression = "에러"
        finally:
            self.update_entry(self.expression)


class BMICalculator:
    """
    키와 몸무게를 입력받아 BMI 지수를 계산하고 결과를 표시하는 클래스.
    """
    def __init__(self, master):
        self.master = master
        self.master.title("BMI 계산기")
        self.master.geometry("300x250")
        self.master.resizable(False, False)

        # 키 입력 프레임
        height_frame = tk.Frame(self.master, padx=10, pady=10)
        height_frame.pack(fill="x")
        tk.Label(height_frame, text="키 (cm):", font=("Arial", 14)).pack(side="left", padx=5)
        self.height_entry = tk.Entry(height_frame, font=("Arial", 14), width=10, bd=2, relief=tk.GROOVE)
        self.height_entry.pack(side="right", expand=True, fill="x", padx=5)

        # 몸무게 입력 프레임
        weight_frame = tk.Frame(self.master, padx=10, pady=10)
        weight_frame.pack(fill="x")
        tk.Label(weight_frame, text="몸무게 (kg):", font=("Arial", 14)).pack(side="left", padx=5)
        self.weight_entry = tk.Entry(weight_frame, font=("Arial", 14), width=10, bd=2, relief=tk.GROOVE)
        self.weight_entry.pack(side="right", expand=True, fill="x", padx=5)

        # 계산 버튼
        calc_button = tk.Button(
            self.master,
            text="BMI 계산",
            font=("Arial", 16, "bold"),
            command=self.calculate_bmi,
            bg="#4CAF50", fg="white", # 녹색 버튼
            activebackground="#45A049",
            pady=10
        )
        calc_button.pack(pady=20)

    def calculate_bmi(self):
        """
        입력된 키와 몸무게를 사용하여 BMI 지수를 계산하고 결과 메시지를 표시합니다.
        """
        try:
            height_cm = float(self.height_entry.get())
            weight_kg = float(self.weight_entry.get())

            if height_cm <= 0 or weight_kg <= 0:
                messagebox.showerror("입력 오류", "키와 몸무게는 0보다 커야 합니다.")
                return

            # 키를 미터 단위로 변환
            height_m = height_cm / 100

            # BMI 계산: 몸무게(kg) / (키(m) * 키(m))
            bmi = weight_kg / (height_m ** 2)
            
            # BMI 결과 판정
            if bmi < 18.5:
                category = "저체중"
            elif 18.5 <= bmi < 23:
                category = "정상"
            elif 23 <= bmi < 25:
                category = "과체중"
            elif 25 <= bmi < 30:
                category = "비만"
            else:
                category = "고도 비만"

            result_message = (
                f"BMI 지수: {bmi:.2f}\n"
                f"판정: {category}"
            )
            messagebox.showinfo("BMI 결과", result_message)

        except ValueError:
            messagebox.showerror("입력 오류", "키와 몸무게를 숫자로 정확히 입력해주세요.")
        except Exception as e:
            messagebox.showerror("오류", f"알 수 없는 오류가 발생했습니다: {e}")


