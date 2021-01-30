def solution(integer):
    try:
        integer = int(integer)
        counter = 1
        sum_cubes = 0
        while counter <= integer:
            sum_cubes += counter ** 3
            counter += 1
            answer = "--> " + str(sum_cubes)
        return answer
    except ValueError:
        answer = "Wrong data"
        return answer


def main():
    integer = input("Enter integer --> ")
    sum_cubes = solution(integer)
    return sum_cubes


if __name__ == "__main__":
    print(main())
