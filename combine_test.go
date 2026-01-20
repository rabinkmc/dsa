package main

import (
	"reflect"
	"testing"
)

func combine(n int, k int) [][]int {
	res := [][]int{}
	var backtrack func(int)
	candidates := []int{}
	backtrack = func(i int) {
		if len(candidates) == k {
			tmp := make([]int, len(candidates))
			copy(tmp, candidates)
			res = append(res, tmp)
			return
		}
		for j := i + 1; j <= n; j++ {
			candidates = append(candidates, j)
			backtrack(j)
			candidates = candidates[:len(candidates)-1]
		}
	}
	backtrack(0)
	return res
}

func TestL77(t *testing.T) {
	got := combine(4, 2)
	expected := [][]int{{1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {3, 4}}
	if !reflect.DeepEqual(got, expected) {
		t.Fatalf("got: %#v , expected: %#v", got, expected)

	}

}
