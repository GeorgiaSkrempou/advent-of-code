package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func readLines(inputFile string) []string {
	file, _ := os.ReadFile(inputFile)
	splitLines := strings.Split(string(file), "\n")
	return splitLines
}

func main() {
	input := readLines("./input")
	numberOfTimes := 0
	for k, item := range input {
		if k == 0{
			continue
		}
		intItem, _ := strconv.Atoi(item)
		prevItem, _ := strconv.Atoi(input[k-1])
		if intItem > prevItem {
			numberOfTimes++
		}
	}
	fmt.Printf("Times increased %d\n", numberOfTimes)
}