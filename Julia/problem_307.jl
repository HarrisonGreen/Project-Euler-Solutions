function calculate_prob(n::Int, k::Int)
    p = [1.0]

    for x in 2:k
        new_p = [(1 + (1 - x)/n) * p[1]]
        for y in 1:Int(floor((x - 1)/2))
            push!(new_p, (x + 1 - (2 * y))/n * p[y] + (1 + (1 - x + y)/n) * p[y + 1])
        end

        if x % 2 == 0
            push!(new_p, 1/n * p[end])
        end

        p = new_p
    end

    println(1 - sum(p))
end

function main()
    chips = 1000000
    defects = 20000
    calculate_prob(chips, defects)
end

main()
