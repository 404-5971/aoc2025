package main

import (
	"fmt"
)


func main() {
	var dial int = 50
    var num_times_dial_zero int = 0

	for i := 0; i < Count; i++ {
		chunk := DirectionsBits[i >> 6]
		isRight := (chunk >> (i & 63)) & 1 == 1
		dist := Distances[i]

		if isRight {
			dial += dist
			dial = dial % 100
		} else {
			dial -= dist
			dial = dial % -100 
		}

		if dial == 0 {
			num_times_dial_zero += 1
		}
	}
	fmt.Println(num_times_dial_zero)
}
