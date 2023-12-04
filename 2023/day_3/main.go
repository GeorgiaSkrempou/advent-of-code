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

func isValidNumber(inputFile []string, indexRow int, indexItem int) bool {
	// possiblePositions := []int{
	// 	-1,
	// 	-1,
	// 	-1,
	// 	0,
	// 	-1,
	// 	1,
	// 	0,
	// 	-1,
	// 	0,
	// 	1,
	// 	1,
	// 	-1,
	// 	1,
	// 	0,
	// 	1,
	// 	1,
	// }
	// ukelele := ""
	// for i := 0; i < len(possiblePositions); i += 2 {
	// 	rowPossiblePosition := possiblePositions[i]
	// 	itemPossiblePosition := possiblePositions[i+1]
	
	if indexRow == 0 && indexItem == 0 {
		ukelele := string(inputFile[indexRow][indexItem+1]) + string(inputFile[indexRow+1][indexItem+1]) + string(inputFile[indexRow+1][indexItem])
	} else if indexRow == len(inputFile) && indexItem == 0 {

	}



	if indexRow != 0 && indexItem != 0 {
		ukelele += string(inputFile[indexRow-1][indexItem-1])
	} else if indexRow != 0 {
		ukelele += string(inputFile[indexRow-1][indexItem])
		ukelele += string(inputFile[indexRow-1][indexItem+1])
	} else if indexItem != 0 {
		ukelele += string(inputFile[indexRow+1][indexItem-1])
		ukelele += string(inputFile[indexRow][indexItem-1])
	} else if len(inputFile) != indexRow+1 && len(inputFile[indexRow]) != indexItem+1 {
		ukelele += string(inputFile[indexRow+1][indexItem+1])
	} else if len(inputFile) != indexRow+1 {
		ukelele += string(inputFile[indexRow+1][indexItem])
	} else if len(inputFile[indexRow]) != indexItem+1 {
		ukelele += string(inputFile[indexRow][indexItem+1])
	}
	fmt.Printf("ukulele: %s\n", ukelele)

	// }
	for _, char := range ukelele {
		if char != 46 && (char < 48 || char > 57) {
			return true
		}
	}
	return false
}

func main() {

	inputFile := readLines("input")
	for indexRow, row := range inputFile {
		// if indexRow == 0 {
		// 	continue
		// }
		longNum := ""
		for indexItem, item := range row {
			// if indexItem == 0 {
			// 	continue
			// }

			if item >= 48 && item <= 57 {
				longNum += string(item)
				// isItemValid := isValidNumber(inputFile, indexRow, indexItem)

				// return

			}
			if (item < 48 || item > 57) && longNum != "" {
				// normalizedIndexItem := indexItem - 1
				fmt.Printf("num: %v ----", longNum)

				isNumValid := false
				for i := len(longNum); i >= 0; i-- {
					// isNumValid = isValidNumber(inputFile, indexRow, (indexItem-1)-((len(longNum)+i)))
					// fmt.Printf("i: %d, indexRow: %d, prevPos: %d ---- ", i, indexRow, indexItem-i)
					isNumValid  = isValidNumber(inputFile, indexRow, indexItem-i)
					// fmt.Printf("number to check: %s, valid: %v\n", string(longNum[i-1]), isNumValid)
					if isNumValid {
						break
					}
				}
				fmt.Println()

				if isNumValid {
					fmt.Printf("num valid: %v\n", longNum)
				}

				longNum = ""
			}

		}
	}

}
