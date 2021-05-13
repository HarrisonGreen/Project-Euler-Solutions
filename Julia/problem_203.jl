using Primes

function squarefree_sum(rows)
    numbers = Set(binomial(n, k) for n in 1:rows for k in 0:Int(floor(n/2)))

    limit = Int(floor(sqrt(maximum(numbers))))
    squares = primes(limit).^2

    println(sum(square_check(num, squares) for num in numbers))
end

function square_check(num, squares)
    for square in squares
        if num % square == 0
            return 0
        end

        if square > num
            return num
        end
    end

    return num
end

squarefree_sum(50)
