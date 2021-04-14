function main()
    doubles = [2 * n for n in 1:20]
    push!(doubles, 50)

    checkout_one = Dict()
    for n in doubles
        checkout_one[n] = 1
    end

    score_one = Dict()
    for n in 1:20
        score_one[n] = get(score_one, n, 0) + 1
        score_one[2 * n] = get(score_one, 2 * n, 0) + 1
        score_one[3 * n] = get(score_one, 3 * n, 0) + 1
    end
    score_one[25] = 1
    score_one[50] = 1

    checkout_two = Dict()
    for n in 1:50
        for m in 1:60
            checkout_two[n + m] = get(checkout_two, n + m, 0) + get(checkout_one, n, 0) * get(score_one, m, 0)
        end
    end

    score_two = Dict()
    for n in 1:60
        for m in 1:n
            if n == m
                score_two[n + m] = get(score_two, n + m, 0) + 0.5 * get(score_one, n, 0) * (get(score_one, m, 0) + 1)
            else
                score_two[n + m] = get(score_two, n + m, 0) + get(score_one, n, 0) * get(score_one, m, 0)
            end
        end
    end
            
    checkout_three = Dict()
    for n in 1:50
        for m in 1:120
            checkout_three[n + m] = get(checkout_three, n + m, 0) + get(checkout_one, n, 0) * get(score_two, m, 0)
        end
    end
        
    count = 0
    for n in 1:99
        count += get(checkout_one, n, 0)
        count += get(checkout_two, n, 0)
        count += get(checkout_three, n, 0)
    end

    println(Int(count))
end

main()
