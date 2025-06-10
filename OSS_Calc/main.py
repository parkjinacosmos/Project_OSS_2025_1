# main.py

import tkinter as tk
from calculator_module import Calculator, BMICalculator # 두 클래스 모두 임포트


def open_bmi_calculator():
    """
    새로운 Toplevel 창을 열어 BMI 계산기를 실행합니다.
    """
    bmi_window = tk.Toplevel()
    BMICalculator(bmi_window)
    # 부모 창이 닫혀도 BMI 창이 계속 열려있도록 하지 않으려면 아래 주석 해제
    # bmi_window.transient(root)
    # bmi_window.grab_set() # BMI 창이 열려있는 동안 메인 창 조작 불가능 (모달)
    # root.wait_window(bmi_window) # BMI 창이 닫힐 때까지 메인 창 대기


if __name__ == "__main__":
    root = tk.Tk()
    root.title("다기능 계산기") # 메인 계산기 제목 변경
    root.geometry("320x500") # 창 크기 조정
    root.resizable(False, False)

    # 기본 계산기 인스턴스 생성 및 배치
    calc = Calculator(root)

    # BMI 계산기 버튼 추가
    bmi_button_frame = tk.Frame(root, pady=10)
    bmi_button_frame.pack(fill="x")
    bmi_btn = tk.Button(
        bmi_button_frame,
        text="BMI 계산기 열기",
        font=("Arial", 14),
        command=open_bmi_calculator,
        bg="#1E90FF", fg="white", # 파란색 버튼
        activebackground="#007BFF"
    )
    bmi_btn.pack(expand=True, fill="x", padx=10)

    root.mainloop()