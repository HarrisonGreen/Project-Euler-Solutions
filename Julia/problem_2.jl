function fibonacci_sum(limit)
    sequence = [1, 2]; total = 0
    while sequence[end] <= limit
        if iseven(sequence[end])
            total += sequence[end]
        end
        push!(sequence, sequence[end] + sequence[end-1])
    end
    println(total)
end

fibonacci_sum(4000000)
