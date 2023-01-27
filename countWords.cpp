class Solution {
public:
    int countWords(vector<string>& words1, vector<string>& words2) {
    unordered_map<string, int> freqMap1;
    unordered_map<string, int> freqMap2;

    for (string word: words1) {
        freqMap1[word] = freqMap1[word] + 1;
    }
    for (string word: words2) {
        freqMap2[word] = freqMap2[word] + 1;
    }

    int count = 0; 
    for (auto it : freqMap1) {
        auto itMap2 = freqMap2.find(it.first);
        if (it.second == 1 && itMap2 != freqMap2.end() && itMap2->second == 1) {
            ++count;
        }
    }
    return count;
    }
};