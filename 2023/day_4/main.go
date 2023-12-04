package main

import (
	"fmt"
	"os"
	"strings"
)

func readLines(inputFile string) []string {
	myFile, err := os.ReadFile(inputFile)
	if err != nil {
		panic(err)
	}
	return strings.Split(string(myFile), "\n")
}

func main() {
	inputFile := readLines("input")
	totalPoints := 0
	for _, line := range inputFile {
		combinedNumbers := strings.Split(line, ": ")[1]
		numberList := strings.Split(combinedNumbers, " | ")
		winningNumbers := numberList[0]
		scratchedNumbers := numberList[1]
		points := 0
		for _, winningNumber := range strings.Split(winningNumbers, " ") {
			if winningNumber == "" {
				continue
			}
			for _, scratchedNumber := range strings.Split(scratchedNumbers, " ") {
				if scratchedNumber == "" {
					continue
				}
				if winningNumber == scratchedNumber {
					if points == 0 {
						points += 1
					} else {
						points = points*2
					}

				}
			}
		}
		totalPoints += points
	}
	fmt.Printf("%d\n", totalPoints)
}
