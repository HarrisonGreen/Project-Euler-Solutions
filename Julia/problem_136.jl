function count_solns(lim)
    counts = Dict()

    for a in 3:Int(lim * 5/4)
        for b in Int(floor(a/5) + 1):Int(floor((a - 1)/2))

            n = (a - b) * (5 * b - a)

            if n >= lim
                break
            end

            counts[n] = get(counts, n, 0) + 1

        end
    end

    println(count(i -> i == 1, values(counts)))
end

count_solns(50000000)
