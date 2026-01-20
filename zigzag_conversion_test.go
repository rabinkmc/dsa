package main

import (
	"strings"
	"testing"
)

func convert(s string, numRows int) string {
	if numRows == 1 {
		return s
	}

	n := len(s)
	i := 0
	j := 0
	grid := make([][]byte, numRows)
	for i := 0; i < numRows; i++ {
		grid[i] = make([]byte, n)
	}
	c := 0
	for i < n {
		for i < n && j < numRows {
			grid[j][c] = s[i]
			i++
			j++
		}
		j = numRows - 2
		c = c + 1
		for i < n && j > 0 {
			grid[j][c] = s[i]
			j--
			c++
			i++
		}
	}
	var b strings.Builder
	for i := 0; i < numRows; i++ {
		for j := 0; j < c; j++ {
			if grid[i][j] != 0 {
				b.WriteByte(grid[i][j])
			}
		}
	}
	return b.String()
}

func TestL6(t *testing.T) {
	got := convert("PAYPALISHIRING", 3)
	expected := "PAHNAPLSIIGYIR"
	if got != expected {
		t.Fatalf("got: %s expected: %s\n", got, expected)
	}
}
