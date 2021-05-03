function main()
    order = [50,48,46,44,42,40,38,36,34,32,30,31,33,35,37,39,41,43,45,47,49]
    l = order[1] + order[21] + sum(sqrt(200 * (order[i] + order[i+1] - 50)) for i in 1:20)
    println(Int(round(l * 1000)))
end

main()
