package main

import (
	"fmt"
)


func main() {
	// Added a large multiple of 100 to keep 'dial' positive.
	// Go truncates negative division (-50/100 = 0), while Python floors (-50//100 = -1).
	// Keeping dial positive forces Go to behave like Python.
	var dial int = 1000000050 
    var num_times_dial_zero int = 0

	for i := 0; i < Count; i++ {
		chunk := DirectionsBits[i >> 6]
		isRight := (chunk >> (i & 63)) & 1 == 1
		dist := Distances[i]

		start_groups := dial / 100

		if isRight {
			dial += dist
		} else {
			dial -= dist
		}

		end_groups := dial / 100

		result := end_groups - start_groups

		if result < 0 {
			result = -result
		}

		num_times_dial_zero += result
	}
	fmt.Println(num_times_dial_zero)
}
