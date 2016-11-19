#!/usr/bin/env julia

mass_dict = Dict(
    "A" => 71.03711,
    "C" => 103.00919,
    "D" => 115.02694,
    "E" => 129.04259,
    "F" => 147.06841,
    "G" => 57.02146,
    "H" => 137.05891,
    "I" => 113.08406,
    "K" => 128.09496,
    "L" => 113.08406,
    "M" => 131.04049,
    "N" => 114.04293,
    "P" => 97.05276,
    "Q" => 128.05858,
    "R" => 156.10111,
    "S" => 87.03203,
    "T" => 101.04768,
    "V" => 99.06841,
    "W" => 186.07931,
    "Y" => 163.06333
)

# reverse dictionary and round mass to 3 decimal places
mass_dict = Dict(round(mass, 3) => amino for (amino, mass) in mass_dict)

function main(path)=>
    mass_arr = readdlm(path)[:]
    seq = ""
    for i in range(2, length(mass_arr)-1)
        mass = mass_arr[i] - mass_arr[i-1]
        seq *= mass_dict[round(mass, 3)]
    end
    print(seq)
end

main(ARGS[1])
