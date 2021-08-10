using Primes

function calculate_sum(limit)
	p = primes(5, limit)
	s = 0
	for i in 1:length(p) - 1
		s += find_number(p[i], p[i + 1])
	end
	
	println(s)
end

function find_number(p_1, p_2)
	n = 10 ^ length(string(p_1))
	d, a, b = gcdx(n, p_2)
	a = ((-p_1 * a) % p_2 + p_2) % p_2
	
	return (a * n) + p_1
end

calculate_sum(1000003)
