def solution(fst_int, scd_int):
    if fst_int.isdigit() and scd_int.isdigit():
        fst_int = int(fst_int)
        scd_int = int(scd_int)
        if fst_int >= scd_int:
            answer = "first integer(A) should be less than second integer(B)..."
            count = ""
        else:
            answer = []
            for i in range(fst_int, scd_int + 1):
                answer.append(i)
            count = len(answer)
    else:
        answer = "Wrong data!"
        count = ""
    return answer, count


def main():
    first_integer = input("Enter first integer --> ")
    second_integer = input("enter second integer --> ")

    answer, count = solution(first_integer, second_integer)

    return answer, count


if __name__ == "__main__":
    print(main())
