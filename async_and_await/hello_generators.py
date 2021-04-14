def main():
    result = eager_range(10)
    print(result)

    gen_result = lazy_range(10)
    print(next(gen_result))
    print(next(gen_result), '\n')

    jump_result = jump_range(10)
    print(next(jump_result))
    print(jump_result.send(2))
    print(jump_result.send(-1))
    print(next(jump_result))
    print(next(jump_result))
    print(jump_result.send(10))
    print(jump_result.send(-10))


def eager_range(up_to):
    sequence = []
    index = 0
    while index < up_to:
        sequence.append(index)
        index += 1
    return sequence


def lazy_range(up_to):
    index = 0
    while index < up_to:
        yield index
        index += 1


def jump_range(up_to):
    index = 0
    saved_jump = 1
    while -up_to < index < up_to:
        jump = yield index
        if jump:
            saved_jump = jump
        index += saved_jump


if __name__ == '__main__':
    main()
