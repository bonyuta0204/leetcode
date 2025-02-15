package leetcode

func groupAnagrams(strs []string) [][]string {

	uniqMap := make(map[[26]int][]string)

	for _, word := range strs {
		var encoded [26]int

		for _, r := range word {
			encoded[r-'a'] += 1
		}

		store := uniqMap[encoded]

		uniqMap[encoded] = append(store, word)
	}

	results := make([][]string, 0)

	for _, value := range uniqMap {
		results = append(results, value)
	}

	return results
}
