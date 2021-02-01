def solution(fst_int, scd_int):
    try:
        fst_int = int(fst_int)
        scd_int = int(scd_int)
        if fst_int >= scd_int:
            answer = "first integer(A) should be less than second integer(B)..."
            count = ""
            return answer, count
        else:
            count = []
            answer = "--> "
            for i in range(fst_int, scd_int + 1):
                answer += f"{str(i)} "
                count.append(i)
            count = f"Count of integers --> {str(len(count))}"
            return answer, count
    except ValueError:
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
